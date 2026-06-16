# 🚀 Agentic SQL Assistant

An AI-powered multi-agent system that enables users to interact with PostgreSQL databases using natural language instead of SQL.

Built with LangGraph, FastAPI, Chainlit, PostgreSQL, and OpenAI, the system dynamically discovers database schemas, generates SQL queries, executes them safely, self-corrects failures, and explains results in plain English.

---

## 🎯 Business Problem

Business users often need insights from databases but lack SQL expertise.

Traditional BI workflows require:

* Writing SQL manually
* Understanding database schemas
* Troubleshooting query errors
* Interpreting raw database results

Agentic SQL Assistant eliminates these barriers by allowing users to ask questions in natural language and receive database insights instantly.

Examples:

* Show all customers
* Who are the top customers?
* Show customer distribution
* What did we discuss earlier?
* Show revenue by region

---

## 💡 Solution

Agentic SQL Assistant combines multiple AI agents that collaborate to understand user intent, generate SQL, execute queries, recover from failures, maintain conversational context, and explain results.

The system automatically:

* Discovers PostgreSQL schemas
* Converts natural language into SQL
* Executes queries safely
* Fixes SQL errors automatically
* Maintains conversation memory
* Generates business-friendly explanations

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Chainlit Interface
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph Router Agent
 ├── SQL Agent
 ├── Analytics Agent
 └── Memory Agent
 │
 ▼
PostgreSQL Database
```

---

## 🔄 LangGraph Workflow

```text
User Question
      │
      ▼
Router Agent
      │
      ▼
Generate SQL
      │
      ▼
Execute SQL
      │
      ▼
Success?
 ┌────┴────┐
 │         │
No        Yes
 │         │
 ▼         ▼
Fix SQL  Explain Result
 │         │
 └────┬────┘
      ▼
   Response
```

---

## 🤖 Multi-Agent Design

### Router Agent

Classifies user intent and routes requests to the appropriate specialized agent.

### SQL Agent

Generates PostgreSQL queries from natural language and executes them against the database.

### Analytics Agent

Handles business intelligence and analytical requests.

Examples:

* Top customers
* Revenue trends
* Customer distribution
* Sales insights

### Memory Agent

Maintains conversation history and enables context-aware interactions.

Example:

"What did we discuss earlier?"

---

## ✨ Key Features

### Natural Language to SQL

Ask database questions using plain English.

### Dynamic Schema Discovery

Automatically reads PostgreSQL schemas and adapts to new databases without code changes.

### Self-Healing SQL

Automatically fixes invalid SQL and retries execution.

### SQL Safety Guard

Prevents execution of dangerous database operations.

Blocked operations include:

* DROP
* DELETE
* TRUNCATE
* UPDATE
* ALTER
* CREATE

Only safe read-only queries are permitted.

### Conversational Memory

Maintains context across multiple interactions.

### Business-Friendly Explanations

Transforms raw database results into clear and understandable insights.

---

## 🛠️ Technology Stack

| Category        | Technology         |
| --------------- | ------------------ |
| Language        | Python             |
| Agent Framework | LangGraph          |
| LLM             | OpenAI GPT-4o-mini |
| Backend         | FastAPI            |
| Frontend        | Chainlit           |
| Database        | PostgreSQL         |
| ORM             | SQLAlchemy         |
| Validation      | Pydantic           |

---

## 📂 Project Structure

```text
SQL-Agent/
│
├── app/
│   ├── agents/
│   ├── database/
│   ├── graph/
│   ├── memory/
│   ├── services/
│   └── api/
│
├── chainlit_app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 💬 Example Queries

### Customer Analysis

* Show all customers
* Show top 10 customers
* Show customer distribution

### Revenue Analysis

* Show total revenue
* Show revenue by region
* Show highest revenue customers

### Memory

* What did we discuss earlier?
* Summarize our conversation

---

## 🚀 Future Enhancements

* Data Visualization Agent
* Chart Generation
* Multi-Database Support
* Azure Deployment
* Role-Based Access Control
* Persistent Conversation Memory
* Enterprise Authentication
* Dashboard Analytics

---

## 📈 Skills Demonstrated

* Agentic AI Design
* LangGraph Workflow Orchestration
* Tool Calling
* Multi-Agent Systems
* SQL Generation
* Self-Healing Agents
* Conversational Memory
* FastAPI Development
* PostgreSQL Integration
* Prompt Engineering
* AI Application Architecture

---

## 👨‍💻 Author

Sifat Ullah Khan

AI Engineer | Generative AI | Agentic AI | LangGraph | FastAPI | PostgreSQL
