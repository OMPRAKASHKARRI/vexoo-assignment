# 🚀 Vexoo Labs – AI Engineer Assignment

## 📌 Overview

This project implements an end-to-end AI pipeline that transforms unstructured text into structured, queryable knowledge using a hierarchical Knowledge Pyramid and enables semantic retrieval.

The system is designed with a strong focus on **modularity, scalability, and reasoning-based architecture**.

---

## 🧠 Key Features

### 🔹 1. Document Ingestion (Sliding Window)

* Splits large documents into overlapping chunks
* Preserves context across boundaries
* Improves downstream retrieval quality

---

### 🔹 2. Knowledge Pyramid (4 Layers)

Each document chunk is transformed into:

* **Raw Text** – Original chunk
* **Summary** – Condensed version
* **Category** – Rule-based classification
* **Keywords** – Extracted important terms

👉 This enables structured and hierarchical knowledge representation

---

### 🔹 3. Semantic Retrieval (TF-IDF)

* Converts summaries into vector representations
* Uses similarity scoring to find relevant results
* Lightweight alternative to embeddings

---

### 🔹 4. GSM8K Training Pipeline

* Dataset loaded using HuggingFace
* Train/Test split (3000 / 1000 samples)
* Simulated training loop with logging
* Evaluation using accuracy metric

---

### 🔹 5. Reasoning Router (Bonus)

* Classifies query intent (math, general, technical)
* Routes queries to appropriate processing modules
* Demonstrates extensible system design

---

## ⚙️ Tech Stack

* Python
* Scikit-learn (TF-IDF)
* NumPy
* HuggingFace Datasets

---

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Ingestion + Retrieval System

```bash
python main.py
```

### 3. Run Training Pipeline

```bash
python training.py
```

---

## 📊 Example Output

```
Enter your query: What is sliding window?

[Router] Query routed to: general

Result:
Summary: ...
Category: general
Keywords: [...]
```

---

## 🧠 Design Decisions

* Used **TF-IDF** for efficient semantic search
* Avoided heavy models to focus on system design
* Built **modular architecture** for scalability
* Simulated training to demonstrate ML workflow

---

## ⚠️ Limitations

* Summarization is placeholder-based
* No real embeddings used
* Training is simulated

---

## 🔮 Future Improvements

* Integrate embeddings (BERT / OpenAI)
* Use vector databases (FAISS)
* Implement real fine-tuning (LoRA)
* Add advanced summarization models

---

## 📄 Report

Detailed explanation is available in:
👉 [report.pdf](https://github.com/user-attachments/files/26626828/report.pdf)


---

## 👨‍💻 Author

Omprakash Karri
