import json

INPUT_LOG_FILE = 'logs/retrieved_chunks_log.jsonl'
OUTPUT_FILE = 'rag_eval_sample.json'

questions = set()
samples = []

with open(INPUT_LOG_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        question = data.get("question", "").strip()
        model_answer = data.get("model_answer", "").strip()

        # 避免重复
        if question and question not in questions:
            questions.add(question)
            samples.append({
                "question": question,
                "model_answer": model_answer
            })

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(samples, f, ensure_ascii=False, indent=2)

print("✅ rag_eval_sample.json 已成功生成！")
