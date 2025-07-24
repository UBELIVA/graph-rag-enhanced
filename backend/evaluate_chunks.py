import json
import os
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# 路径定义
retrieved_path = "logs/retrieved_chunks_log.jsonl"
ground_truth_path = "logs/eval/ground_truth_answers.json"
output_path = "logs/eval/rag_eval_result_sentence_transformer.json"

# 加载数据
with open(retrieved_path, "r", encoding="utf-8") as f:
    retrieved_logs = [json.loads(line) for line in f if line.strip()]

with open(ground_truth_path, "r", encoding="utf-8") as f:
    ground_truth_data = json.load(f)

# ground truth 转为 dict 方便索引
ground_truth = {item["question"]: item["reference_answer"] for item in ground_truth_data}

# 相似度计算函数
def compute_cosine_similarity(ref, ans):
    emb1 = model.encode(ref, convert_to_tensor=True)
    emb2 = model.encode(ans, convert_to_tensor=True)
    return util.pytorch_cos_sim(emb1, emb2).item()

results = []

for log in retrieved_logs:
    question = log["question"].strip()
    model_answer = log["model_answer"].strip()

    if question not in ground_truth:
        print(f"[警告] 未找到标准答案：{question}")
        continue

    reference_answer = ground_truth[question].strip()
    similarity = compute_cosine_similarity(reference_answer, model_answer)

    results.append({
        "question": question,
        "reference_answer": reference_answer,
        "model_answer": model_answer,
        "similarity": round(similarity, 4)
    })

# 保存结果
Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ SentenceTransformer 相似度评估完成，结果已保存至 {output_path}")

