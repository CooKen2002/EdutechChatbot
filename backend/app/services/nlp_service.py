# backend/app/nlp_engine.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import nltk
from nltk.tokenize import sent_tokenize

# Đảm bảo tải punkt đúng cách
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

class NLPModel:
    def __init__(self, model_name="vinai/phobert-base", num_labels=2):
        """
        Khởi tạo mô hình PhoBERT từ Hugging Face
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "vinai/phobert-base-v2", 
            num_labels=2
        )

    def preprocess(self, text):
        """
        Tiền xử lý văn bản (tách câu, làm sạch văn bản, v.v.)
        """
        text = text.strip().lower()
        sentences = sent_tokenize(text)  # Đảm bảo gọi đúng hàm tách câu
        return sentences

    def predict(self, text):
        """
        Thực hiện dự đoán cho văn bản nhập vào
        """
        # Tiền xử lý văn bản
        sentences = self.preprocess(text)
        encoded_input = self.tokenizer(
            sentences, 
            return_tensors="pt", 
            padding=True, 
            truncation=True, 
            max_length=128  # Độ dài tối đa của mỗi câu
        )

        # Chuyển mô hình sang chế độ đánh giá
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**encoded_input)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=-1)

        # Trả về kết quả dự đoán
        return {
            "text": text,
            "predictions": predictions.cpu().numpy().tolist()
        }

# Kiểm tra mô hình PhoBERT
if __name__ == "__main__":
    nlp_model = NLPModel()
    text = "Xin chào! Bạn có khỏe không?"
    result = nlp_model.predict(text)
    print("Kết quả dự đoán:", result)
