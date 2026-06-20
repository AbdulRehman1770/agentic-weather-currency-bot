# 🤖 Agent-007: Live Weather & Currency Converter AI Agent

Welcome to **Agent-007**, an intelligent multi-tool AI assistant powered by the **Gemini 2.0 Flash** model (via the OpenAI-compatible wrapper). 

This agent uses function calling (tool-use) to dynamically decide whether it needs to fetch real-time global weather updates or look up the latest live financial currency exchange rates to answer user queries.

---

## 🧠 How It Works

Instead of just chatting, this agent acts as a smart brain or controller. When a user asks a question, the agent evaluates the intent automatically:
1. **Weather Query?** 🌦️ It triggers the `get_weather` tool which fetches data via the WeatherAPI.
2. **Currency Query?** 💱 It triggers the `currency_converter` tool which hits the ExchangeRate-API for real-time pair conversions.
3. **General Response?** It handles it directly using Gemini's built-in reasoning capabilities.

---

## 🛠️ Tech Stack & Integration

- **LLM Core:** Gemini 2.0 Flash (`gemini-2.0-flash`)
- **Framework:** Custom OpenAI-Compatible Async Agentic Framework
- **External APIs:** - [WeatherAPI](https://www.weatherapi.com/) for live meteorology data.
  - [ExchangeRate-API](https://v6.exchangerate-api.com/) for up-to-the-minute conversion rates.

---

## 💻 Getting Started

### 1. Clone & Install Dependencies
Clone this repository to your local machine and install the required modules:
```bash
pip install -r requirements.txt
