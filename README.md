🤖 AI Chatbot with RAG (Retrieval-Augmented Generation)

📌 Overview

This project implements a chatbot powered by a Large Language Model (LLM), enhanced with Retrieval-Augmented Generation (RAG) to answer questions based on custom documents.

Unlike traditional chatbots, this system retrieves relevant information from user-provided data before generating responses, ensuring more accurate and context-aware answers.

⸻

🚀 Features
	•	Conversational chatbot with memory
	•	Document-based Q&A using RAG
	•	Semantic search using embeddings
	•	FAISS-based vector database for fast retrieval
	•	Document chunking for improved accuracy
	•	Context-aware response generation

⸻

🧠 Tech Stack
	•	Python
	•	OpenAI API
	•	FAISS (vector database)
	•	NumPy

⸻

⚙️ How it Works
	1.	Documents are loaded from files
	2.	Text is split into smaller chunks
	3.	Each chunk is converted into embeddings
	4.	Embeddings are stored in a FAISS vector index
	5.	User query is converted into an embedding
	6.	Similar chunks are retrieved using vector search
	7.	Retrieved context is passed to the LLM
	8.	LLM generates a grounded response
