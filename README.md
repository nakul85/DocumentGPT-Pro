# 📄 DocumentGPT Pro

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-blueviolet)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.2-black)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-Embeddings-orange)
![License](https://img.shields.io/badge/License-MIT-success)

</div>

> **AI-powered Retrieval-Augmented Generation (RAG) assistant for chatting with documents completely offline.**

DocumentGPT Pro is a production-ready AI document assistant that enables users to upload PDF, DOCX, or TXT files and interact with them using natural language. The application combines semantic search, Retrieval-Augmented Generation (RAG), and local large language models to provide accurate, context-aware responses without requiring an internet connection.

Built using **Ollama**, **LangChain**, **ChromaDB**, **Sentence Transformers**, and **Streamlit**, the application performs document indexing, semantic retrieval, AI-powered summarization, question generation, and conversational search entirely on your local machine.

---

## ✨ Features

- 📄 Upload PDF, DOCX and TXT documents
- 🤖 AI-powered document question answering
- 🧠 AI-generated executive summaries
- 💡 Suggested questions generated automatically
- 🔍 Semantic search using ChromaDB
- ⚡ Streaming LLM responses
- 💬 Multi-turn conversation memory
- 📚 Retrieved source references
- 🎯 Confidence score based on retrieval similarity
- 📊 Document analytics dashboard
- ⏱️ Retrieval and LLM response timing
- 📤 Export chat as TXT, Markdown and PDF
- 🔒 Fully offline using Ollama
- 🧩 Modular architecture for easy extension

---

# 🏗️ System Architecture

```text
                    Upload Document
                           │
                           ▼
                  Document Loader
                           │
                           ▼
                    Text Chunking
                           │
                           ▼
            Sentence Transformer Embeddings
                           │
                           ▼
                      ChromaDB
                           │
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
  Semantic Retrieval                  AI Summary
         │                            Suggested Questions
         │                                   │
         └──────────────┬────────────────────┘
                        ▼
                 Llama 3.2 (Ollama)
                        │
                        ▼
                  Streamlit Interface
```

---

# 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| LLM | Ollama (Llama 3.2) |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Frontend | Streamlit |
| Document Parsing | PyPDF, python-docx |
| PDF Export | ReportLab |

---

# 📂 Project Structure

```text
DocumentGPT-Pro/

├── app.py
├── config.py
├── requirements.txt

├── assets/
│   └── style.css

├── components/
│   ├── chat.py
│   ├── sidebar.py
│   ├── workspace.py
│   ├── uploader.py
│   ├── summary.py
│   ├── source_view.py
│   ├── confidence_card.py
│   └── ...

├── utils/
│   ├── vector_store.py
│   ├── document_processor.py
│   ├── summarizer.py
│   ├── question_generator.py
│   ├── confidence.py
│   └── ...

├── uploads/
├── chroma_db/

└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
cd DocumentGPT-Pro
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Ollama

Download Ollama from:

https://ollama.com

Pull the required model

```bash
ollama pull llama3.2:3b
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run app.py
```

---

# 💻 Usage

1. Upload a PDF, DOCX or TXT document.
2. Click **Process Document**.
3. Wait for indexing and AI analysis.
4. Review the generated summary.
5. Ask questions about the document.
6. View retrieved sources.
7. Export conversations if needed.

---

# ⭐ Key Features

✅ AI Executive Summary

✅ Suggested Questions

✅ Semantic Search

✅ Streaming Responses

✅ Conversation Memory

✅ Confidence Score

✅ Source Attribution

✅ Chat Export

✅ Offline Inference

---

# 🔮 Future Improvements

- Multi-document search
- OCR support
- Image understanding
- Citation highlighting
- User authentication
- Multi-user workspaces
- Cloud deployment
- REST API

---

# 👨‍💻 Author

**Nakul Firodiya**

AI Engineer | Machine Learning | Generative AI | RAG | Python

If you found this project useful, consider giving it a ⭐ on GitHub.