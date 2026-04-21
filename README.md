🤖 AI Chatbot with RAG (Retrieval-Augmented Generation)

📌 Overview

This project implements a chatbot powered by an LLM, enhanced with Retrieval-Augmented Generation (RAG) to answer questions based on custom documents.

🚀 Features
	•	Conversational chatbot using LLM
	•	Context-aware responses
	•	Document-based Q&A using vector search
	•	FAISS-based retrieval system

🧠 Tech Stack
	•	Python
	•	OpenAI API
	•	FAISS (vector database)

⚙️ How it Works
	1.	Documents are split into chunks
	2.	Chunks are converted into embeddings
	3.	Stored in FAISS index
	4.	User query → embedding → similarity search
	5.	Relevant context sent to LLM
	6.	Final answer generated

👤 Author

Bhanu Bhadouria
