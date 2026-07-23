# Voyager AI

An autonomous, multi-agent travel planner built with LangGraph, LangChain, and FastAPI.

> **Live App:** [Voyager AI App](https://voyager-ai-i2jg.onrender.com/)

Planning a trip usually means juggling a dozen open tabs, bouncing between flight search engines, hotel aggregators, and manual itinerary spreadsheets. Voyager AI streamlines that entire process. Give it a natural-language request, and a coordinated network of AI agents will find flights, discover hotels, and construct a practical day-by-day travel plan for you.

---

## How It Works

Instead of relying on a single AI model to guess everything, Voyager AI splits the workload across dedicated agents orchestrated through a LangGraph workflow:

1. **Flight Research Agent:** Leverages the AviationStack API to retrieve relevant flight information.
2. **Hotel Research Agent:** Queries the web using Tavily search to find tailored accommodation options.
3. **Itinerary Agent:** Takes the gathered flight and hotel data and structures a practical, budget-conscious daily schedule.
4. **Synthesis Agent:** Consolidates everything into a clean, formatted final response.

---

## Key Features

* **Multi-Agent Orchestration:** Powered by LangGraph to handle multi-step planning logic smoothly.
* **Real-Time Flight Search:** Integrates AviationStack for accurate flight routes and schedules.
* **Live Web Research:** Uses Tavily search to uncover dynamic hotel and stay suggestions.
* **Fast Engine:** Driven by Groq LLMs for low-latency responses.
* **Persistent Sessions:** Uses PostgreSQL to save and maintain conversation state across queries.
* **Clean UI & Backend:** Ships with a lightweight FastAPI server and an easy-to-use web interface.

---

## Tech Stack

* **Core Frameworks:** Python 3.13, LangGraph, LangChain
* **Backend & Web:** FastAPI, Jinja2, HTML/CSS/JavaScript
* **Database:** PostgreSQL
* **Inference Engine:** Groq
* **External APIs:** Tavily Search, AviationStack

---

## Project Structure

```text
.
├── app.py                 # Entry for the FastAPI server
├── backend.py             # LangGraph workflow and multi-agent logic
├── requirements.txt       # Python dependencies
├── static/                # Frontend static assets (CSS, JS)
├── templates/             # HTML templates
└── tools/                 # Flight & web search tool implementations
```

---

## Prerequisites

Make sure you have the following installed and available:

- Python 3.10 or higher
- A running instance of PostgreSQL
- Valid API keys for Groq, Tavily, and AviationStack

---

## Environment Setup

Create a .env file in the root directory and populate it with your configuration:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=DEL
```
---

## Installation
1. Clone the repository to your local machine.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

Start the server using Python:

```bash
python app.py
```

Once running, navigate to  ```text http://127.0.0.1:8000/ ``` in your web browser.
