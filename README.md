# ⚖️ Gramin-Nyaya: AI Legal Assistant

**Gramin-Nyaya** (Rural Justice) is an offline, privacy-first AI assistant designed to bridge the legal information gap for rural populations in India. By leveraging a dual-model **Agentic RAG** pipeline, the system provides grounded, simplified legal guidance from the **Registration Act, 1908** in high-quality Hindi.

---

## 🚀 Key Features

* **Agentic Dual-Model Pipeline:** Orchestrates two specialized models (**DeepSeek-R1** and **Qwen 2.5**) to separate legal reasoning from linguistic simplification.
* **100% Offline & Private:** Runs entirely on local hardware via Ollama. No data ever leaves the device—crucial for maintaining confidentiality in legal queries.
* **Hindi-First Interface:** A minimalist, "Kiosk-style" web UI designed for high readability and ease of use for non-tech-savvy users.
* **Voice-Ready:** Integrated with **Faster-Whisper** for Hindi speech-to-text, allowing users to ask questions naturally via voice input.
* **Hallucination Control:** Uses Retrieval-Augmented Generation (RAG) to ensure every answer is grounded in official legal documents.

---

## 🤖 Agentic Architecture

Unlike standard AI chatbots, Gramin-Nyaya uses a **Reasoning-to-Generation** workflow:

1.  **The Researcher (DeepSeek-R1 1.5B):** Analyzes the retrieved legal context to extract technical facts, specific sections (dhara), and statutory requirements.
2.  **The Communicator (Qwen 2.5 1.5B):** Translates those technical facts into culturally nuanced, simplified Hindi (Devanagari) that is easy for a village user to understand.

---

## 🛠️ Tech Stack

* **Core Logic:** Python 3.10+
* **LLMs:** DeepSeek-R1 (1.5B) & Qwen 2.5 (1.5B) via **Ollama**
* **API Framework:** FastAPI
* **Vector Database:** ChromaDB
* **Embeddings:** HuggingFace Multilingual-MiniLM (L12-v2)
* **STT:** Faster-Whisper (Base model)
* **Frontend:** Clean HTML5 / CSS3 / JavaScript (Single-file, no-build requirement)

---

## 📂 Project Structure

```text
Gramin-Nyaya/
├── legal_docs/             # Source PDF (Registration Act 1908)
├── api.py                  # FastAPI Backend & Model Orchestration
├── rag_logic.py            # RAG pipeline & Dual-model logic
├── stt_service.py          # Voice-to-Text processing service
├── gramin_nyaya_main.py    # CLI-based controller
├── index.html              # Village-friendly Web Interface
├── requirements.txt        # Python dependencies
└── .gitignore              # Git exclusion rules
