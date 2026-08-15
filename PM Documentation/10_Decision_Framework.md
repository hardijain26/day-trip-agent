# 🧭 DayTrip Planner — Decision Framework

## 1. Purpose

This document defines how DayTrip Planner makes and revises planning decisions when transforming a user's intent, preferences, and constraints into a practical day-trip itinerary.

The framework is concerned with **planning decisions**, not feature prioritization.

It defines how the agent should:

- Understand the user's intent.
- Identify constraints and preferences.
- Evaluate feasible options.
- Manage trade-offs.
- Select combinations of activities.
- Sequence the selected options into a practical day.
- Validate the complete itinerary.
- Revise affected decisions when the user changes a requirement.
- Explain meaningful decisions to the user.

The objective is to produce the **best-fit plan for the specific user and context**, rather than an objectively "best" collection of activities.

---

## 2. Decision-Making Objective

The agent should optimize for overall itinerary fit across:

- 🎯 User intent
- 📍 Practical feasibility
- 💰 Budget
- ⏰ Time
- 🧘 Desired pace and mood
- 🎨 Interests
- 🔎 Information reliability
- 🔗 Dependencies between activities

A recommendation should only be considered successful when it works as part of the **complete itinerary**, not merely when it is attractive as an individual option.

---

## 3. Decision Hierarchy

When evaluating competing options, the agent should use the following hierarchy:

1. **Hard constraints**
2. **Feasibility**
3. **Core user intent**
4. **Explicit preferences**
5. **Itinerary coherence**
6. **Value and quality**
7. **Secondary preferences**

### 3.1 Hard Constraints

Hard constraints are requirements that should not be violated without user agreement.

Examples include:

- Maximum budget
- Required location
- Available time window
- Explicit exclusions
- Group-specific requirements
- Other constraints explicitly stated by the user

If a hard constraint cannot be satisfied, the agent should not silently ignore it.

It should either:

- Adjust the recommendation,
- Explain the limitation, or
- Ask the user for clarification.

---

## 4. Feasibility Before Preference Optimization

The agent should first determine whether an option is practically viable.

An option should be filtered out when it creates a material conflict with:

- Opening hours
- Available time
- Travel requirements
- Budget constraints
- Geographic practicality
- Dependencies
- Other known hard constraints

Only options that remain feasible should be compared based on preference fit.

This prevents the agent from selecting a highly relevant activity that cannot realistically fit into the day.

---

## 5. Candidate Evaluation

For each feasible candidate, the agent should consider:

### 5.1 Intent Fit

How strongly does the option support what the user is trying to accomplish?

Examples:

- Relaxation
- Exploration
- Food-focused experience
- Arts and culture
- Outdoor experience
- Social activity

### 5.2 Preference Fit

How well does the option match the user's stated interests and preferences?

### 5.3 Practical Fit

How easily can the option fit into the available day?

Consider:

- Location
- Opening hours
- Travel time
- Duration
- Required reservations or dependencies

### 5.4 Budget Fit

How does the option affect the overall trip cost?

The agent should consider the cost of the **combined itinerary**, not only the cost of individual activities.

### 5.5 Information Reliability

How confident is the agent in the information used to evaluate the option?

Current or uncertain information should be treated accordingly.

---

## 6. Combination-Level Decision Making

The agent should select the **best-fit combination of options**, rather than independently selecting the highest-ranked activity in each category.

A combination should be evaluated for:

- Overall intent fit
- Total cost
- Total time
- Travel efficiency
- Pacing
- Opening-hour compatibility
- Activity dependencies
- Overall experience coherence

An individually strong recommendation should be rejected when including it makes the complete itinerary materially worse.

---

## 7. Trade-off Management

Trade-offs should be resolved according to the decision hierarchy.

When two desirable options cannot both be included, the agent should prefer the option that better preserves:

1. Hard constraints
2. Feasibility
3. Core user intent
4. Explicit preferences
5. Overall itinerary coherence

The agent should avoid optimizing a secondary preference at the expense of a higher-priority requirement.

### Example: Trade-off Resolution

If the user wants an inexpensive and relaxing day, the agent should not add a highly rated but expensive activity merely because it is popular.

---

## 8. Itinerary Sequencing

Once the selected activities are determined, the agent should sequence them into a practical day.

Sequencing should consider:

- Opening hours
- Travel time
- Activity duration
- Geographic proximity
- Natural transitions
- Meal timing
- Breaks
- Desired pace
- Dependencies between activities

The goal is not to maximize the number of activities.

The goal is to create a **comfortable and coherent day**.

---

## 9. Itinerary Validation

The complete itinerary should be validated after sequencing.

Validation should check:

- ⏰ Time feasibility
- 📍 Geographic feasibility
- 💰 Budget alignment
- 🧘 Pace and experience fit
- 🔎 Information reliability
- 🔗 Activity dependencies
- 🚫 Explicit user constraints

If validation identifies a problem, the affected decision should be reconsidered rather than simply presenting the invalid itinerary.

---

## 10. Iterative Refinement

The agent should treat follow-up requests as modifications to the existing planning state.

When the user changes a preference or constraint, the agent should:

1. Identify what changed.
2. Determine which decisions are affected.
3. Preserve unaffected valid decisions where possible.
4. Re-evaluate affected options.
5. Re-sequence the itinerary if necessary.
6. Re-validate the complete itinerary.

The agent should avoid restarting the entire planning process when only part of the itinerary needs to change.

---

## 11. Decision Reversal

A previous decision should be reconsidered when:

- A hard constraint changes.
- New information invalidates an assumption.
- A selected activity becomes infeasible.
- The user changes a meaningful preference.
- A downstream dependency is affected.
- Validation identifies a material problem.

The agent should revise the **smallest affected portion of the plan** while preserving valid decisions where possible.

---

## 12. Decision Transparency

When a recommendation involves a meaningful trade-off or constraint, DayTrip Planner should make the reasoning understandable to the user.

The explanation should communicate:

- The key factors that influenced the decision.
- Any important trade-off that affected the selection.
- Any constraint that limited the alternatives.
- Any significant assumption made during planning.

The agent does not need to expose:

- Internal scoring
- Implementation details
- Every candidate considered
- Internal reasoning traces

The goal is to provide enough context for the user to understand **why the selected plan fits and where compromises were made**.

---

## 13. Decision Framework Summary

DayTrip Planner's planning decisions follow this sequence:

1. Understand the user's intent.
2. Identify hard constraints, feasibility requirements, and preferences.
3. Filter out options that are not viable.
4. Evaluate the remaining options for intent, preference, practical, and value fit.
5. Manage trade-offs according to the decision hierarchy.
6. Select the best-fit combination rather than optimizing individual options independently.
7. Sequence the selected options into a practical day.
8. Validate the complete itinerary.
9. Revise affected decisions when validation identifies a problem.
10. Explain meaningful trade-offs and assumptions when presenting the recommendation.

The objective is not to find the objectively "best" collection of activities, but to produce the **best-fit plan for the specific user, context, and constraints**.

---

## 14. Boundary With Other Documents

This document owns the logic used to make and revise **planning decisions**.

Other documents retain ownership of their respective concerns:

- **Product Goal** — Defines why DayTrip Planner exists and the user value it aims to create.
- **Agent Responsibilities** — Defines what the agent is responsible for doing.
- **User Flow** — Defines how the user and agent progress through the planning journey.
- **MVP Scope** — Defines what is included in the MVP.
- **Product Requirements** — Defines the capabilities the product must provide.
- **Feature Prioritization** — Defines which capabilities should be built first.
- **Guardrails** — Defines the boundaries and behaviors the agent must follow.
- **Success Metrics** — Defines how planning and product outcomes are measured.
- **Future Roadmap** — Defines capabilities that may be considered beyond the MVP.

The Decision Framework should be **referenced by other documents when they need to describe how a planning decision is made**, rather than reproducing the decision logic.
