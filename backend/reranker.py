# reranker.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class Reranker:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-reranker-base")
        self.model = AutoModelForSequenceClassification.from_pretrained("BAAI/bge-reranker-base")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def rerank(self, query, docs, top_k=5):
        if not docs:
            return []
        
        pairs = [[query, doc] for doc in docs]
        inputs = self.tokenizer(pairs, padding=True, truncation=True, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            scores = self.model(**inputs).logits.squeeze(-1)
        
        top_indices = torch.topk(scores, k=min(top_k, len(docs))).indices
        return [docs[i] for i in top_indices]
