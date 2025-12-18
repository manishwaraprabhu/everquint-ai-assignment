# Max Profit Problem

## Problem Overview

This task focuses on solving the **Max Profit Problem**, where the objective is to determine the **optimal combination of properties** that maximizes total earnings within a given time constraint.

Mr. X owns an infinite strip of land on Mars. He can develop the land by constructing one of the following properties:

* Theatre
* Pub
* Commercial Park

Only **one property can be constructed at a time**, and earnings start **only after the construction of a property is completed**.

The goal is to compute the **maximum possible earnings** for a given number of time units and present the **optimal construction strategy**.

---

## Property Details

| Property Type   | Build Time (Units) | Land Used | Earnings per Unit Time |
| --------------- | ------------------ | --------- | ---------------------- |
| Theatre         | 5                  | 2 × 1     | $1500                  |
| Pub             | 4                  | 1 × 1     | $1000                  |
| Commercial Park | 10                 | 3 × 1     | $2000                  |

---

## Constraints and Assumptions

* Only **one construction** can happen at any given time.
* Land availability is **unlimited**.
* Earnings are calculated **only after a property becomes operational**.
* The order of construction impacts total earnings.
* Input is a single integer `n` representing total available time units.

---

## Approach and Logic

A **brute-force optimization approach** is used:

1. Generate all possible combinations of theatres, pubs, and commercial parks that fit within the given time limit.
2. For each valid combination:

   * Properties are constructed sequentially.
   * After each construction, earnings are accumulated for the remaining time units.
3. Track:

   * The **maximum total earnings** obtained.
   * The construction mix that produces this maximum profit.

This guarantees the optimal solution under the given constraints.

---

## Earnings Formula

The total earnings are calculated using the following logic:

**Earnings = Σ (Remaining Time After Construction × Earning Rate)**

Where:

* Remaining Time = Total Time − Cumulative Construction Time
* Earning Rate:

  * Theatre → $1500 per unit time
  * Pub → $1000 per unit time
  * Commercial Park → $2000 per unit time

Since **only one property can be constructed at a time**, constructions occur sequentially.

---

## Implementation

The solution is implemented in Python and consists of two parts:

1. **Core optimization logic** (`max_profit.py`)
2. **Interactive user interface** using Streamlit (`maxprofit_streamlit_app.py`)

---

## Core Algorithm (`max_profit.py`)

```python
def find_max_profit(total_time):
    theatre_time = 5
    pub_time = 4
    commercial_time = 10

    theatre_earning = 1500
    pub_earning = 1000
    commercial_earning = 2000

    max_earning = 0
    best_solutions = []

    for t in range((total_time // theatre_time) + 1):
        for p in range((total_time // pub_time) + 1):
            for c in range((total_time // commercial_time) + 1):

                build_time = (t * theatre_time + p * pub_time + c * commercial_time)
                if build_time > total_time:
                    continue

                current_time = 0
                total_earning = 0

                for _ in range(t):
                    current_time += theatre_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * theatre_earning

                for _ in range(p):
                    current_time += pub_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * pub_earning

                for _ in range(c):
                    current_time += commercial_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * commercial_earning

                if total_earning > max_earning:
                    max_earning = total_earning
                    best_solutions = [{"T": t, "P": p, "C": c}]
                elif total_earning == max_earning:
                    best_solutions.append({"T": t, "P": p, "C": c})

    return max_earning, best_solutions
```

---

## Streamlit User Interface (`maxprofit_streamlit_app.py`)

An interactive UI was built using **Streamlit** (optional but recommended in the orientation).

### UI Features

* **Available Properties section** displaying build time, land usage, earnings, and efficiency
* **Time Input** field to enter total available time units
* **Calculate Maximum Profit** button
* **Optimal Solution panel** showing:

  * Maximum profit
  * Optimal construction mix
* **Earnings Breakdown** for each property type
* **Formula explanation** for clarity

This UI makes the algorithm easy to understand and demonstrate during evaluation.

---

## Sample Test Cases

### Test Case 1

**Input:** 7
**Output:** Earnings: $3000

Solutions:

* T: 1 P: 0 C: 0
* T: 0 P: 1 C: 0

### Test Case 2

**Input:** 8
**Output:** Earnings: $4500

Solution:

* T: 1 P: 0 C: 0

### Test Case 3

**Input:** 13
**Output:** Earnings: $16500

Solution:

* T: 2 P: 0 C: 0

---

## How to Run

### Run via Terminal (CLI)

```bash
python max_profit.py
```

### Run Streamlit UI

```bash
streamlit run maxprofit_streamlit_app.py
```

Then open the browser URL shown in the terminal.

---

## Conclusion

This project demonstrates a complete solution to the **Max Profit Problem** using a clear optimization algorithm and an intuitive user interface. It strictly follows the problem constraints and orientation guidelines, making it suitable for technical evaluation, demonstration, and real-world reasoning scenarios.