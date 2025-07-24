import json

# ✍️ 替换为你这条问题 & 回答
sample = {
    "question": "牛顿三大定律是什么？",
    "answer": "牛顿三大定律是惯性定律、加速度定律和作用力反作用力定律。"
}

# ✅ 加载你刚才保存的 chunk 内容
with open("retrieved_chunks.json", "r", encoding="utf-8") as f:
    sample["retrieved_chunks"] = json.load(f)

# ✅ 把这一条完整样本保存为 rag_eval_sample.json
with open("rag_eval_sample.json", "w", encoding="utf-8") as f:
    json.dump([sample], f, indent=2, ensure_ascii=False)

print("✅ rag_eval_sample.json 创建成功！")
