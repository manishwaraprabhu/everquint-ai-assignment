# Multi-Step Reasoning Agent with Self-Checking

## Overview

This project implements a **Multi-Step Reasoning Agent with Self-Checking**, designed as part of the **Gen AI Engineer – Multistep Reasoning** assignment.  

The agent mimics **human-like structured reasoning** by breaking down a problem into multiple internal phases — **planning, execution, and verification** — and only exposing a **clean final answer** and **short explanation** to the user.

The solution is intentionally built with **agentic architecture principles**, focusing on correctness, reliability, and debuggability rather than raw text generation.

---

## Objective

The goal of this task is to build a reasoning agent that:

- Solves **structured word problems**
- Reasons through **multiple internal steps**
- **Verifies its own solution**
- Returns results in a **strict JSON schema**
- **Hides raw chain-of-thought** from the user

---

## Problem Types Supported

The agent is capable of solving:

- ⏱️ **Time difference problems**
- ➗ **Arithmetic and counting problems**
- 🧠 **Logic & constraint-based reasoning**
- 📅 **Scheduling and duration validation**

### Example Questions

- *If a train leaves at 14:30 and arrives at 18:05, how long is the journey?*
- *Alice has 3 red apples and twice as many green apples as red. How many apples does she have in total?*
- *A meeting needs 60 minutes. Which time slots can fit it?*

---

## Output Format (Strict JSON)

The agent always returns a response in the following schema:

```json
{
  "answer": "<final short answer>",
  "status": "success | failed",
  "reasoning_visible_to_user": "<concise explanation>",
  "metadata": {
    "plan": "<internal plan>",
    "checks": [
      {
        "check_name": "<string>",
        "passed": true,
        "details": "<string>"
      }
    ],
    "retries": <integer>
  }
}
````

> 🔒 **Important:**
> Raw chain-of-thought reasoning is never exposed to the user.

---

## Agent Architecture

The system follows a **three-phase reasoning pipeline**:

### 1️⃣ Planner

* Reads the user question
* Produces a concise step-by-step plan
* Focuses on **what needs to be done**, not how

### 2️⃣ Executor

* Executes the plan
* Computes intermediate values internally
* Outputs **only the final answer** in a strict format

### 3️⃣ Verifier

* Re-checks the solution
* Validates:

  * Arithmetic correctness
  * Time boundaries
  * Logical constraints
* Marks the solution as **PASS** or **FAIL**

If verification fails, the system is designed to retry or fail safely.

---

## Technology Stack

* **Python**
* **Ollama (LLM backend)**
* **phi-3-mini model**
* **Streamlit** (frontend UI)
* **Regex-based answer extraction**

> No external agent frameworks were required, keeping the system lightweight and transparent.

---

## Project Structure

```text
reasoning-agent/
│
├── agent.py                  # Core planner–executor–verifier logic
├── llm_client_ollama.py      # LLM abstraction layer
├── streamlit_reasoning_app.py# Streamlit frontend
├── tests/                    # (Optional) test cases
└── README.md                 # Documentation
```

---

## Prompt Design

Separate prompts were designed for each phase:

### Planner Prompt

* Produces **numbered steps only**
* No explanations
* Forces structured planning

### Executor Prompt

* Solves the problem internally
* **Explicitly hides reasoning**
* Outputs only:

  ```
  FINAL ANSWER: <answer>
  ```

### Verifier Prompt

* Independently validates the solution
* Responds with strict `PASS` or `FAIL`

This separation improves:

* Reliability
* Debugging
* Future extensibility

---

## How to Run the Agent

### Option 1: Streamlit UI (Recommended)

```bash
streamlit run streamlit_reasoning_app.py
```

Then open the local URL shown in the terminal.

---

### Option 2: Python API Usage

```python
from agent import ReasoningAgent

agent = ReasoningAgent()
result = agent.run("Alice has 3 red apples and twice as many green apples.")
print(result)
```

---

## Example Output

### Input

```
If a train leaves at 14:30 and arrives at 18:05, how long is the journey?
```

### Output

```json
{
  "answer": "3 hours 35 minutes",
  "status": "success",
  "reasoning_visible_to_user": "The journey duration is calculated by comparing the departure and arrival times, resulting in a total travel time of three hours and thirty-five minutes.",
  "metadata": {
    "plan": "Parse times → convert to minutes → subtract → format duration",
    "checks": [
      {
        "check_name": "Primary Verification",
        "passed": true,
        "details": "PASS"
      }
    ],
    "retries": 0
  }
}
```

---

## Test Coverage

The agent was tested against:

* ✅ Basic arithmetic questions
* ✅ Multi-step logic problems
* ✅ Time boundary edge cases
* ✅ Scheduling constraints

Each test logs:

* Question
* Final JSON output
* Verification status
* Retry count

---

## Key Learnings

* Designing **agentic workflows** instead of single-shot prompts
* Separating reasoning phases improves correctness
* Self-verification significantly reduces hallucinations
* Chain-of-Thought should be **managed**, not exposed

---

## Future Improvements

* Retry loop with capped attempts
* Parallel verifier agents
* Tool-calling for deterministic arithmetic
* REST API deployment
* Improved natural-language explanations

---

## Conclusion

This project demonstrates a **production-oriented reasoning agent** that goes beyond simple question answering. By integrating planning, execution, and verification into a structured pipeline, the agent delivers **accurate, reliable, and explainable outputs**, aligning closely with real-world **agentic AI system design principles**.
