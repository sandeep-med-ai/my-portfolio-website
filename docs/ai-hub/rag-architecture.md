# 🧠 Ayur RAG: Agentic RAG Architecture for Ayurveda

**OCR + Shloka-Aware Chunking + Hybrid Retrieval + Multi-Agent System**

---

## 📌 Overview

Ayur RAG is an **agentic Retrieval-Augmented Generation (RAG) system** designed specifically for **Ayurvedic texts** like:

- Charaka Samhita
- Sushruta Samhita
- Classical Sanskrit Granthas

It handles:

- 📄 Scanned PDFs (OCR)
- 🕉️ Sanskrit Shlokas (structure-aware)
- 🔍 Hybrid Retrieval (semantic + keyword)
- 🤖 Multi-agent reasoning pipeline

---

## ⚙️ System Pipeline

```mermaid
graph TD
A[PDF / Image] --> B[OCR / Parsing]
B --> C[Shloka-aware Chunking]
C --> D[Embedding]
D --> E[Vector DB - FAISS]
E --> F[Retriever Agent]
F --> G[Generator Agent]
G --> H[Verifier Agent]

🧩 Core Components
1. Ingestion Layer
PDF parsing using PyMuPDF
OCR fallback using PaddleOCR
2. Processing Layer
Shloka detection using । and ॥
Separate handling for:
Shloka
Prose
3. Embedding Layer
Sentence Transformers
Semantic vector representation
4. Retrieval Layer
FAISS vector search
Hybrid retrieval (future scope)
5. Agent Layer
🧠 Planner → decides strategy
🔍 Retriever → fetches context
✍️ Generator → creates answer
✅ Verifier → ensures grounding
📂 Project Structure
ayur_rag/
├── data/
│   ├── raw/
│   └── processed/
├── ingestion/
├── processing/
├── indexing/
├── agents/
├── pipeline/
├── prompts/
├── app.py
└── README.md
📊 Sample Ayurvedic Dataset
[
  {
    "id": "CS_Sutra_1",
    "type": "shloka",
    "text": "हिताहितं सुखं दुःखमायुस्तस्य हिताहितम्",
    "translation": "That which is beneficial or harmful for life...",
    "page": 1,
    "source": "Charaka Samhita"
  }
]
🚀 Example Query

Query:
Vataja Shiroroga

Output:

Answer based on retrieved context:
[Page 120] Vataja Shiroroga is caused by aggravated Vata dosha...
🔥 Key Innovations
🕉️ Shloka-aware chunking
🧠 Agent-based reasoning
🔍 Context-grounded answers
📚 Ayurveda-specific data modeling
🛠️ Future Improvements
Hybrid search (BM25 + FAISS)
Sanskrit OCR optimization
Multi-document reasoning
Chat-based UI (ChatGPT style)
Automatic commentary generation
🎯 Use Cases
📚 Ayurveda students (BAMS prep)
🧪 Researchers
🤖 AI healthcare assistants
📖 Digital Grantha indexing
👨‍⚕️ Author

Dr. Sandeep Shrivastva
AI in Healthcare | Ayurveda | RAG Systems
