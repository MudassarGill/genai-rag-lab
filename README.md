# GenAI RAG Lab 🚀

Welcome to the **GenAI RAG Lab**! This project is a hands-on exploration of **Retrieval-Augmented Generation (RAG)** concepts using **LangChain** and the blazing fast **Groq API** (powered by Meta's Llama 3 models). 

The goal of this project is to demonstrate how large language models (LLMs) can be grounded with external knowledge from various data sources to provide accurate, context-aware answers.

## 📂 Features & Document Loaders

This repository includes custom loaders to extract and process different data formats:

1. **`textloader.py`** 📝
   - Loads content from plain text files (e.g., `sample_data.txt`).
   - Uses LangChain's `TextLoader` to ingest the data and queries Llama 3 to explain concepts like RAG from the provided text.

2. **`webloader.py`** 🌍
   - Scrapes and processes data directly from live websites.
   - Powered by `WebBaseLoader` (and BeautifulSoup), it can read articles (like Wikipedia) and answer user questions directly based on the scraped content.

3. **`pdfloader.py`** 📄
   - Extracts text from PDF documents (e.g., personal resumes, reports).
   - Utilizes `PyPDFLoader` to parse the PDF and uses the LLM to extract specific, targeted details like contact information, profile headlines, and links.

## 🛠️ Tech Stack
* **Framework:** LangChain
* **LLM Provider:** Groq API (`llama-3.3-70b-versatile`)
* **Environment:** `python-dotenv` for managing API keys securely
* **Language:** Python

## 🚀 Quick Start / How to Run

1. Clone or download this project.
2. Install the necessary Python packages:
   ```bash
   pip install langchain-groq langchain-community python-dotenv pypdf beautifulsoup4
   ```
3. Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=gsk_your_api_key_here
   ```
4. Run any of the specific loaders from your terminal:
   ```bash
   python textloader.py
   python pdfloader.py
   python webloader.py
   ```

---

## 👨‍💻 About the Developer

### **M Mudassar Hussain** 
*AI | ML | GenAI | RAG | Backend Developer (FastAPI)*

This lab environment was developed by **M Mudassar Hussain** as part of an exploration into Advanced Generative AI and RAG architectures. Mudassar is highly passionate about building intelligent, scalable AI systems, integrating modern UI/UX workflows, and deploying robust backend services.

**Let's Connect!**
* The `pdfloader.py` in this repo is specifically configured to load my resume. Run it to uncover my email, phone number, LinkedIn, and GitHub profiles directly via AI!
* *Alternatively, you can reach me at:* `mudassarjutt65030@gmail.com`
