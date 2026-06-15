# Agentic SQL Assistant

An AI-powered multi-agent SQL assistant that allows users to interact with PostgreSQL databases using natural language.

Built with LangGraph, FastAPI, Chainlit, PostgreSQL, and OpenAI.

## Features

### Natural Language to SQL

Convert user questions into executable PostgreSQL queries.

### Multi-Agent Architecture

* SQL Agent
* Analytics Agent
* Memory Agent
* Router Agent

### Conversation Memory

Maintains context across multiple interactions.

### Analytics Engine

Supports business intelligence queries such as:

* Top customers
* Revenue analysis
* Customer distribution
* Sales insights

### Self-Healing SQL

Automatically attempts to fix SQL errors and retry execution.

### SQL Safety Guard

Blocks potentially dangerous operations:

* DROP
* DELETE
* TRUNCATE
* UPDATE
* ALTER

Only safe SELECT-based queries are allowed.

### FastAPI Backend

REST API for integration with external applications.

### Chainlit Frontend

ChatGPT-style conversational interface.

## Architecture

User
→ Chainlit
→ FastAPI
→ LangGraph Router
→ SQL Agent / Analytics Agent / Memory Agent
→ PostgreSQL

## Tech Stack

* Python
* LangGraph
* OpenAI
* FastAPI
* Chainlit
* PostgreSQL
* SQLAlchemy
* Pydantic

## Example Queries

Show all customers

Who are the top customers?

Show customer distribution

What did we discuss?

## Future Enhancements

* Chart generation
* Multi-database support
* Azure deployment
* Role-based access control
* Advanced analytics dashboard

## Author

Sifat Ullah Khan
