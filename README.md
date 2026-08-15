# DayTrip Planner 🗺️

## 1. Introduction

DayTrip Planner is an AI-powered day-trip planning agent designed to help users turn a travel idea into a practical, realistic itinerary.

The project explores how an AI agent can combine user preferences, constraints, and current information to support travel planning and decision-making.

The primary focus of this project is **AI product thinking and agent design**, supported by a lightweight working prototype built using Google ADK and Gemini.

---

## 2. What the Product Does

DayTrip Planner helps users plan a single-day trip by considering:

- 📍 Origin and destination
- 📅 Date of travel
- ⏰ Available time
- 👥 Group size
- ❤️ Interests and preferences
- 💰 Budget
- 🚆 Travel time and transportation
- 🏛️ Attractions and activities
- 🍽️ Food options
- 🌦️ Other time-sensitive information

The agent can use Google Search when current or location-specific information is required.

The goal is not simply to provide a list of places.

It is to help answer:

> **"What is a realistic and enjoyable day trip for me, given my constraints?"**

The agent is designed to distinguish between verified information and estimates and avoid presenting uncertain or outdated information as fact.

---

## 3. Product Approach

The project was developed from a **Product Management perspective**, with the product thinking defined before expanding the technical implementation.

The work covers:

- 🎯 Product goal
- 👤 User needs and flow
- 🧩 Agent responsibilities
- 📋 Product requirements
- ⚖️ Feature prioritization
- 🛡️ AI guardrails
- 📊 Success metrics
- 🧠 Decision framework
- 🤖 Agent behavior
- 🏗️ Agent architecture
- 🚀 Future roadmap

Detailed thinking and decisions are documented in:

**`Product Documentation/`**

---

## 4. Demo 🖥️

The prototype can be explored through the Google ADK web interface.

### 💬 Day-Trip Planning

![Day-trip planning demo](demo/day-trip-planning.png)

### 🗺️ Generated Itinerary

![Generated itinerary](demo/generated-itinerary.png)

---

## 5. Prototype & Technology

The product concept is supported by a lightweight working prototype using:

- Google Agent Development Kit (ADK)
- Gemini
- Google Search
- Python

The implementation is intentionally lightweight. The focus of the project is on **product design, agent behavior, decision-making, and AI product considerations** rather than software engineering.

---

## 6. What I Learned From This Project 💡

This project helped me understand that building an AI product is different from simply building a feature powered by an LLM.

### 🎯 1. Start with the problem, not the technology

An AI model can generate many possible answers, but that does not automatically mean the product is solving the right problem.

Defining the user problem and desired outcome first helped determine what the agent should actually do.

### 🧠 2. AI products require decision design

The challenge is not only generating information.

The product needs to decide:

- What information matters?
- What should be prioritized?
- What constraints should be considered?
- When should the agent ask the user for more information?
- When should it search for current information?
- When should it communicate uncertainty?

### 🛡️ 3. Guardrails are part of the product

For an AI travel product, incorrect information can directly affect a user's plans.

This made accuracy, uncertainty, current information, and hallucination prevention **product requirements**, rather than purely technical considerations.

### ⚖️ 4. More features do not necessarily create a better MVP

It was important to distinguish between what the product could eventually do and what it actually needs to prove its core value.

This helped me think more clearly about MVP boundaries and prioritization.

### 🔄 5. Product thinking continues after the first prototype

Building the initial prototype exposed gaps that were difficult to identify during the conceptual stage.

The process reinforced the importance of iterating between:

**Product thinking → Prototype → Observation → Refinement**

### 🤖 6. Building with AI changed how I think about PM execution

Using AI development tools allowed me to move from product concept to a working prototype without relying on a traditional engineering team for every iteration.

It helped me understand how Product Managers can become more hands-on in validating AI product ideas while still focusing on user problems, product decisions, and outcomes.

---

## Project Status

**MVP — Active Development**

This project is being iteratively refined as the product concept, agent behavior, and decision framework evolve.
