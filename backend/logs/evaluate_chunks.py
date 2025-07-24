import json
from sentence_transformers import SentenceTransformer, util

# 配置路径（根据你的目录结构自行调整）
retrieved_path = "logs/retrieved_chunks_log.jsonl"
ground_truth_path = "logs/ground_truth.json"
output_path = "logs/eval/rag_eval_result_sentence_transformer.json"

# 加载 SentenceTransformer 模型
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# 加载模型回答（logs）
with open(retrieved_path, "r", encoding="utf-8") as f:
    retrieved_logs = [json.loads(line) for line in f if line.strip()]

# 加载 ground truth
with open(ground_truth_path, "r", encoding="utf-8") as f:
    ground_truth_data = json.load(f)

# 转换 ground truth 为字典：{question: reference_answer}
ground_truth = {item["question"]: item["reference_answer"] for item in ground_truth_data}

# 相似度计算函数
def compute_cosine_similarity(ref, ans):
    emb1 = model.encode(ref, convert_to_tensor=True)
    emb2 = model.encode(ans, convert_to_tensor=True)
    return util.pytorch_cos_sim(emb1, emb2).item()

# 计算每个问题的相似度
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
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ SentenceTransformer 相似度评估完成，结果已保存至 {output_path}")
