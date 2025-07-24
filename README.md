# Graph-RAG Enhanced

This is an enhanced version of [neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder), modified for research purposes by **Chuanyu Ma** at **DeepThink Lab**.

**Graph-RAG Enhanced** is a streamlined and customized version of the original project.
It focuses on reliable knowledge graph generation from unstructured text using **OpenAI models** and **LangChain**, while simplifying configuration and removing unused features like YouTube and GCS integration.

This version is designed for **local development and private use**, with improvements to chunking, environment setup, and evaluation flexibility.

---

## Key Improvements

* Based entirely on OpenAI LLMs (e.g., `gpt-4o`, `gpt-3.5-turbo`)
* YouTube and GCS sources removed for cleaner dependencies
* Simplified `.env` configuration for backend and frontend
* Enhanced chunking and deduplication logic
* Supports graph-based, vector-based, and hybrid QA modes
* Compatible with Neo4j Aura DB/DS or local Neo4j 5.23+

---

## Features

### Knowledge Graph Generation

* Converts text, PDF, DOCX, and web pages into Neo4j knowledge graphs
* Extracts entities and relationships with OpenAI LLMs
* Visualizes results in Neo4j Bloom

### Conversational QA

* Interact with uploaded content through a chat interface
* Supports multiple QA strategies (graph, vector, hybrid)
* Each response includes source traceability

---

## Setup Instructions

### Prerequisites

* Python 3.10+
* Node.js 18+
* Neo4j 5.23+ with APOC installed
* OpenAI API key

### Backend Setup

```bash
cd backend
cp example.env .env
python -m venv envName
source envName/bin/activate      # On Windows: envName\Scripts\activate
pip install -r requirements.txt
uvicorn score:app --reload
```

### Frontend Setup

```bash
cd frontend
cp example.env .env
yarn
yarn run dev
```

### Docker Deployment (Optional)

```bash
docker-compose up --build
```

---

## Environment Variables

### Example backend `.env`

```env
OPENAI_API_KEY=your-openai-api-key
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password
NEO4J_DATABASE=neo4j
```

### Example frontend `.env`

```env
VITE_BACKEND_API_URL=http://localhost:8000
VITE_LLM_MODELS=openai_gpt_4o
VITE_CHAT_MODES=vector,graph,graph_vector
VITE_REACT_APP_SOURCES=local,web
```

---

## Usage

1. Start the backend and frontend
2. Upload files (TXT, PDF, DOCX, or web links)
3. Select model and graph extraction method
4. Generate and visualize graphs in Neo4j Bloom
5. Use the chat interface to ask questions about your data

---

## Reference

* Original repo: [neo4j-labs/llm-graph-builder](https://github.com/neo4j-labs/llm-graph-builder)
* Demo video (original version): [YouTube](https://www.youtube.com/watch?v=LlNy5VmV290)

---

## License

This project inherits the same license as the upstream repository.
See `LICENSE` for more information.

---

## Maintainer

Created and maintained by [@UBELIVA](https://github.com/UBELIVA)
