# Max Profit Problem

## Problem Overview

This task focuses on solving the **Max Profit Problem**, where the objective is to determine the **optimal combination of properties** that maximizes total earnings within a given time constraint.

Mr. X owns an infinite strip of land on Mars. He can develop the land by constructing one of the following properties:

- Theatre
- Pub
- Commercial Park

Only **one property can be constructed at a time**, and earnings start **only after the construction of a property is completed**.

The goal is to compute the **maximum possible earnings** for a given number of time units and display the possible construction combinations that achieve this maximum profit.

---

## Property Details

| Property Type | Build Time (Units) | Land Used | Earnings per Unit Time |
| :--- | :--- | :--- | :--- |
| Theatre | 5 | 2 × 1 | $1500 |
| Pub | 4 | 1 × 1 | $1000 |
| Commercial Park | 10 | 3 × 1 | $2000 |

---

## Constraints and Assumptions

- Only **one construction** can happen at any given time.
- Land availability is **unlimited**.
- Earnings are calculated **only after a property becomes operational**.
- The construction order impacts total earnings since earlier completion results in longer earning duration.
- Input is a single integer `n` representing total available time units.

---

## Approach and Logic

To solve this problem, a **brute-force optimization approach** is used:

1. All possible combinations of theatres, pubs, and commercial parks that fit within the given time limit are generated.
2. For each valid combination:
   - Properties are constructed sequentially.
   - After each construction, earnings are accumulated for the remaining time units.
3. The algorithm tracks:
   - The **maximum total earnings** obtained.
   - All combinations that achieve this maximum earning.
4. Multiple solutions may exist for the same maximum profit, and all such solutions are reported.

This approach ensures that the optimal mix of properties is identified based on time constraints.

---

## Implementation

The solution is implemented in Python.  
The core logic is contained in the function `find_max_profit`.

### Source Code

```python
def find_max_profit(total_time):
    # Time required to build each type
    theatre_time = 5
    pub_time = 4
    commercial_time = 10

    # Earnings per unit time
    theatre_earning = 1500
    pub_earning = 1000
    commercial_earning = 2000

    max_earning = 0
    best_solutions = []

    # Try all combinations
    for t in range((total_time // theatre_time) + 1):
        for p in range((total_time // pub_time) + 1):
            for c in range((total_time // commercial_time) + 1):

                build_time = (
                    t * theatre_time +
                    p * pub_time +
                    c * commercial_time
                )

                if build_time > total_time:
                    continue

                current_time = 0
                total_earning = 0

                # Build theatres first
                for _ in range(t):
                    current_time += theatre_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * theatre_earning

                # Then pubs
                for _ in range(p):
                    current_time += pub_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * pub_earning

                # Then commercial parks
                for _ in range(c):
                    current_time += commercial_time
                    if current_time <= total_time:
                        total_earning += (total_time - current_time) * commercial_earning

                if total_earning > max_earning:
                    max_earning = total_earning
                    best_solutions = [{
                        "T": t,
                        "P": p,
                        "C": c
                    }]
                elif total_earning == max_earning:
                    best_solutions.append({
                        "T": t,
                        "P": p,
                        "C": c
                    })

    return max_earning, best_solutions


if __name__ == "__main__":
    n = int(input("Enter total time units: "))

    earnings, solutions = find_max_profit(n)

    print(f"\nEarnings: ${earnings}")
    print("Solutions:")
    for i, sol in enumerate(solutions, start=1):
        print(f"{i}. T: {sol['T']} P: {sol['P']} C: {sol['C']}")

```

### Sample Test Cases

#### Test Case 1

**Input:** 7

**Output:** Earnings: $3000

Solutions:

1. T: 0 P: 1 C: 0
2. T: 1 P: 0 C: 0

#### Test Case 2

**Input:** 8

**Output:** Earnings: $4500

Solutions:

1. T: 1 P: 0 C: 0

#### Test Case 3

**Input:** 13

**Output:** Earnings: $16500

Solutions:

1. T: 2 P: 0 C: 0

---

## How to Run the Program

1. Navigate to the `max-profit` directory.
2. Ensure Python is installed on your system.
3. Run the Python script using the command below:

```bash
python max_profit.py

```

4. Enter the total time units when prompted.
5. The program will display the maximum earnings and all valid construction combinations.

## Conclusion

This solution evaluates all feasible construction combinations within the given time constraint and determines the optimal strategy that maximizes total earnings. By considering build time, earning duration, and construction order, the algorithm ensures accurate and optimal results.