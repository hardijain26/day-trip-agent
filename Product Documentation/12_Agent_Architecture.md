# 🏗️ DayTrip Planner — Agent Architecture

## 1. Purpose

This document describes the high-level technical architecture supporting the DayTrip Planner MVP.

It is intended to show how the product's AI capabilities are assembled, without documenting implementation details or reproducing application code.

---

## 2. Architecture Overview

DayTrip Planner uses a **single-agent architecture built with Google Agent Development Kit (ADK)**.

The MVP consists of:

- **AI Agent** — Coordinates the planning interaction.
- **AI Model** — Understands the user's request and generates responses.
- **Search Tool** — Provides access to current travel information when required.
- **Session Context** — Maintains relevant information across follow-up interactions.
- **ADK Runtime** — Provides the execution environment for the agent.

The architecture is intentionally lightweight to support rapid MVP development and iteration.

---

## 3. Core Components

### AI Agent

The agent coordinates the planning experience by combining:

- User context
- Agent instructions
- Model capabilities
- Available tools

### AI Model

The model provides natural-language understanding and generation required to interpret travel requests and produce itinerary recommendations.

### Tools

Tools extend the agent beyond information contained in the model.

For the MVP, the primary tool capability is **Google Search** for current travel information.

### Session Context

Session context allows the agent to retain relevant information such as:

- User preferences
- Constraints
- Existing itinerary decisions
- Follow-up changes

This enables iterative planning without requiring the user to repeat information.

---

## 4. Current Information & Search

Travel information can change over time.

The agent can use Google Search when current information is important to the recommendation, such as:

- Opening hours
- Events
- Prices
- Venue information

Search provides information to the agent; the agent remains responsible for interpreting that information in the context of the user's trip.

---

## 5. MVP Architecture Decision

The MVP uses a **single-agent architecture rather than a multi-agent architecture**.

This keeps the system:

- Simpler to build
- Easier to test
- Easier to iterate
- Sufficient for the current planning use case

A more complex architecture can be considered later if product requirements demonstrate a clear need for specialized agents or independent planning capabilities.

---

## 6. Architecture Boundary

This document describes **how the product is technically assembled**.

It does not define:

- **Agent Behavior** — How the AI should interact with users.
- **Decision Framework** — How planning decisions should be made.
- **Product Requirements** — What the product must be capable of doing.
- **Feature Prioritization** — Which capabilities should be built first.

Implementation details remain in the application code and are intentionally not reproduced here.

