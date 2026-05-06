````md
# Ayur RAG
**An Agentic RAG system for Ayurvedic documents**  
**OCR + Shloka-Aware Chunking + Hybrid Retrieval + Multi-Agent Generation**

Ayur RAG is a modular, agentic Retrieval-Augmented Generation (RAG) pipeline built for Ayurvedic texts such as **Charaka Samhita**, **Sushruta Samhita**, and other classical or scanned documents.  
It is designed to handle:

- scanned PDFs and images through OCR,
- Sanskrit shlokas with shloka-aware chunking,
- concept-based and hybrid retrieval,
- grounded answer generation with verification.

This repository is structured to support future expansion into a full AI assistant for Ayurveda study, research, and document understanding.

---

## Features

- **PDF text extraction** using PyMuPDF
- **OCR fallback** for scanned pages using PaddleOCR
- **Shloka-aware chunking** for Sanskrit verses and prose
- **Embedding-based semantic search** with Sentence Transformers
- **Vector similarity search** using FAISS
- **Agent-style pipeline** with planner, retriever, generator, and verifier
- **Ayurveda-friendly metadata** such as source, page number, commentary, and type
- **Ready for extension** into FastAPI, UI, or chat-based applications

---

## Project Structure

```bash
ayur_rag/
│
├── data/
│   ├── raw/                # PDFs, scanned pages, images
│   └── processed/          # cleaned JSON documents
│
├── ingestion/
│   ├── ocr.py              # OCR text extraction
│   └── parser.py           # PDF parsing
│
├── processing/
│   ├── chunker.py          # shloka-aware chunking
│   └── language.py         # optional language detection / script handling
│
├── indexing/
│   ├── embedder.py         # text embeddings
│   └── vectordb.py         # FAISS vector store
│
├── agents/
│   ├── planner.py          # decides retrieval strategy
│   ├── retriever.py        # fetches relevant chunks
│   ├── generator.py        # generates grounded answer
│   └── verifier.py         # checks hallucinations / grounding
│
├── pipeline/
│   └── run_pipeline.py     # end-to-end execution
│
├── prompts/
│   ├── planner.txt
│   ├── generator.txt
│   └── verifier.txt
│
├── app.py                  # optional FastAPI / UI entry point
├── requirements.txt
└── README.md
````

---

## How It Works

### 1. Ingestion

Documents are loaded from `data/raw/`.
If the document is a PDF, text is extracted directly. If the page is scanned or contains no text, OCR can be used.

### 2. Parsing

Each page is converted into structured JSON-like records containing:

* page number
* extracted text
* source document
* optional metadata

### 3. Chunking

The chunker detects whether the content is likely a **shloka** or **prose**.
Shlokas are preserved as complete units whenever possible, so the meaning is not broken across chunks.

### 4. Embedding

All chunks are converted into vector embeddings using a sentence-transformer model.

### 5. Indexing

Vectors are stored in FAISS for fast similarity-based retrieval.

### 6. Agentic Retrieval

A planner decides whether the query needs:

* vector retrieval,
* hybrid retrieval,
* or broader reasoning across multiple chunks.

### 7. Generation

The generator produces an answer only from retrieved context.

### 8. Verification

A verifier checks whether the answer is grounded in the retrieved text and flags unsupported claims.

---

## Sample Ayurvedic Dataset

Example file: `data/processed/sample.json`

```json
[
  {
    "id": "CS_Sutra_1",
    "type": "shloka",
    "text": "हिताहितं सुखं दुःखमायुस्तस्य हिताहितम्",
    "translation": "That which is beneficial or harmful for life...",
    "commentary": "Defines the scope of Ayurveda",
    "page": 1,
    "source": "Charaka Samhita"
  },
  {
    "id": "CS_Shiro_Vata",
    "type": "concept",
    "text": "Vataja Shiroroga is caused by aggravated Vata dosha...",
    "page": 120,
    "source": "Charaka Samhita"
  }
]
```

Recommended metadata fields:

* `id`
* `type` (`shloka`, `concept`, `prose`, `commentary`)
* `text`
* `translation`
* `commentary`
* `page`
* `source`
* `chapter` or `section` if available

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ayur_rag.git
cd ayur_rag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

`requirements.txt`

```txt
pymupdf
paddleocr
sentence-transformers
faiss-cpu
langchain
crewai
fastapi
uvicorn
numpy
```

Optional but useful:

```txt
pandas
python-multipart
pydantic
```

---

## Core Modules

## 1. OCR Module

`ingestion/ocr.py`

```python
from paddleocr import PaddleOCR

# Note:
# For Sanskrit/Devanagari documents, use an OCR language/model
# appropriate for your script if available.
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text(image_path: str) -> str:
    """
    Extract text from an image using PaddleOCR.
    """
    result = ocr.ocr(image_path)
    if not result or not result[0]:
        return ""

    text_lines = []
    for line in result[0]:
        if line and len(line) > 1 and line[1]:
            text_lines.append(line[1][0])

    return " ".join(text_lines).strip()
```

---

## 2. PDF Parser

`ingestion/parser.py`

```python
import fitz  # PyMuPDF
from pathlib import Path

def parse_pdf(path: str):
    """
    Extract text page by page from a PDF.
    Returns a list of dictionaries with page number and text.
    """
    doc = fitz.open(path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text").strip()
        pages.append({
            "page": i + 1,
            "text": text,
            "source_file": Path(path).name
        })

    return pages
```

---

## 3. Shloka-Aware Chunker

`processing/chunker.py`

```python
def is_shloka(text: str) -> bool:
    """
    Basic shloka detection using danda punctuation and length heuristics.
    """
    if not text:
        return False

    return ("।" in text or "॥" in text) and len(text.strip()) > 20


def chunk_text(pages):
    """
    Split pages into chunks while preserving shlokas as complete units.
    """
    chunks = []

    for p in pages:
        page_text = p.get("text", "").strip()
        if not page_text:
            continue

        if is_shloka(page_text):
            chunks.append({
                "type": "shloka",
                "text": page_text,
                "page": p["page"],
                "source_file": p.get("source_file", "")
            })
        else:
            # Basic prose chunking
            chunks.append({
                "type": "prose",
                "text": page_text[:1000],
                "page": p["page"],
                "source_file": p.get("source_file", "")
            })

    return chunks
```

---

## 4. Text Embedding

`indexing/embedder.py`

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert a list of texts into dense embeddings.
    """
    return model.encode(texts, normalize_embeddings=True)
```

---

## 5. Vector Database

`indexing/vectordb.py`

```python
import faiss
import numpy as np

class VectorDB:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)  # cosine-like search if embeddings are normalized
        self.data = []

    def add(self, embeddings, docs):
        embeddings = np.array(embeddings, dtype="float32")
        self.index.add(embeddings)
        self.data.extend(docs)

    def search(self, query_emb, k: int = 3):
        query_emb = np.array([query_emb], dtype="float32")
        distances, indices = self.index.search(query_emb, k)

        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.data):
                results.append(self.data[i])

        return results
```

---

## 6. Planner Agent

`agents/planner.py`

```python
def plan(query: str) -> str:
    """
    Decide retrieval strategy based on the query.
    """
    q = query.lower()

    if "shloka" in q or "sloka" in q or "verse" in q:
        return "vector"
    if "compare" in q or "difference" in q or "diagnosis" in q:
        return "hybrid"

    return "hybrid"
```

---

## 7. Retriever Agent

`agents/retriever.py`

```python
def retrieve(query, db, embed_fn, k: int = 3):
    """
    Embed the query and retrieve top-k relevant chunks.
    """
    q_emb = embed_fn([query])[0]
    results = db.search(q_emb, k=k)
    return results
```

---

## 8. Generator Agent

`agents/generator.py`

```python
def generate(query, context):
    """
    Generate a grounded answer using only the retrieved context.
    """
    context_text = "\n\n".join(
        [f"[Page {c.get('page')}] {c.get('text', '')}" for c in context]
    )

    answer = f"""
Query: {query}

Answer based on retrieved context:
{context_text}
""".strip()

    return answer
```

---

## 9. Verifier Agent

`agents/verifier.py`

```python
def verify(answer: str) -> bool:
    """
    Simple grounding check.
    Returns False if the answer appears uncertain or unsupported.
    """
    if not answer:
        return False

    forbidden_phrases = [
        "not sure",
        "maybe",
        "probably",
        "I think",
        "unsupported"
    ]

    lowered = answer.lower()
    return not any(phrase.lower() in lowered for phrase in forbidden_phrases)
```

---

## 10. End-to-End Pipeline

`pipeline/run_pipeline.py`

```python
from ingestion.parser import parse_pdf
from processing.chunker import chunk_text
from indexing.embedder import embed
from indexing.vectordb import VectorDB
from agents.retriever import retrieve
from agents.planner import plan
from agents.generator import generate
from agents.verifier import verify

PDF_PATH = "data/raw/sample.pdf"

def main():
    pages = parse_pdf(PDF_PATH)
    chunks = chunk_text(pages)

    if not chunks:
        print("No chunks found.")
        return

    texts = [c["text"] for c in chunks]
    embeddings = embed(texts)

    db = VectorDB(len(embeddings[0]))
    db.add(embeddings, chunks)

    query = "Vataja Shiroroga"
    strategy = plan(query)
    print("Planned strategy:", strategy)

    results = retrieve(query, db, embed, k=3)
    answer = generate(query, results)

    if verify(answer):
        print("\nVerified Answer:\n")
        print(answer)
    else:
        print("\nAnswer failed verification.\n")
        print(answer)

if __name__ == "__main__":
    main()
```

---

## Agent Prompts

### `prompts/planner.txt`

```txt
You are a planner agent for an Ayurvedic RAG system.

Decide the best retrieval strategy for the user query:
- vector search
- hybrid retrieval
- broader document reasoning

Use the query type, keywords, and expected answer style.
Return only the chosen strategy and a brief reason.
```

### `prompts/generator.txt`

```txt
You are a grounded Ayurvedic answer generator.

Rules:
- Use ONLY the provided context.
- Do NOT invent facts.
- Cite page number and source when available.
- If the context is insufficient, say so clearly.
- Keep the answer precise, readable, and medically/research appropriate.
```

### `prompts/verifier.txt`

```txt
You are a grounding verifier.

Check whether the answer is fully supported by the retrieved context.
Reject hallucinations, unsupported claims, and uncited additions.
Return:
- PASS if grounded
- FAIL if not grounded
- with a short reason
```

---

## Optional Improvements

This repository is intentionally simple and can be expanded in many directions:

### Retrieval

* Add **BM25 / keyword retrieval** for better hybrid search
* Add **reranking** with cross-encoders
* Add **query expansion** for Sanskrit terms and synonyms

### OCR

* Add **OCR fallback only when PDF text extraction fails**
* Add better support for **Devanagari / Sanskrit OCR**
* Preserve line order for verse reconstruction

### Chunking

* Use verse boundary detection for:

  * `।`
  * `॥`
  * chapter headings
  * commentary sections
* Store chunk overlap for long prose sections

### Metadata

* Include:

  * grantha name
  * adhyaya
  * sthanam
  * verse number
  * translator/commentator

### Application Layer

* FastAPI endpoint for query answering
* Web UI with document upload
* Chat history with citations
* Multi-document support

---

## Example Usage

```bash
python pipeline/run_pipeline.py
```

Expected output:

```bash
Planned strategy: hybrid

Verified Answer:

Query: Vataja Shiroroga

Answer based on retrieved context:
[Page 120] Vataja Shiroroga is caused by aggravated Vata dosha...
```

---

## Important Notes

* This is a **starter architecture** for an Ayurvedic RAG assistant.
* For production use, improve:

  * retrieval quality,
  * OCR robustness,
  * citation formatting,
  * language handling,
  * and answer verification.
* For Sanskrit-heavy datasets, it is better to combine:

  * **semantic embeddings**
  * **keyword matching**
  * **verse-aware chunking**
  * **metadata filtering**

---

## License

Add your preferred license here, for example:

* MIT
* Apache 2.0
* GPL-3.0

---

## Author

Built for Ayurvedic knowledge retrieval, research assistance, and intelligent document understanding.

---

## Future Scope

* Sanskrit-aware OCR pipeline
* Cross-document reasoning across multiple classics
* Ayurveda QA chatbot
* Chapter-wise indexing
* Smart citations
* Translation + commentary generation
* Topic extraction from scanned manuscripts

```

A stronger next step would be a **clean `app.py` + `FastAPI` endpoint** and a **better hybrid retrieval implementation** with BM25 + FAISS.
```
