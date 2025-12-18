# Water Tank Problem – Rainwater Trapping Visualization

## Problem Statement

Given an array of non-negative integers representing the height of blocks, compute the **total units of water trapped between the blocks** after rainfall.

You are required to build a **frontend web application** using **HTML, CSS, and Vanilla JavaScript** that:
- Computes the total trapped water
- Visually represents blocks and trapped water
- Demonstrates the working of the rainwater trapping algorithm

### Example

**Input**
```text
[0, 4, 0, 0, 0, 6, 0, 6, 4, 0]
````

**Output**

```text
18 Units
```

---

## Objective

The goal of this task is to:

* Solve the classic **Trapping Rain Water** algorithmic problem
* Create a **visual, production-level frontend solution**
* Clearly demonstrate **how water is accumulated between blocks**
* Use **SVG-based visualization** for clarity and scalability

---

## Solution Overview

The application accepts a comma-separated list of block heights and performs the following:

1. **Validates input**
2. **Computes trapped water** using an efficient algorithm
3. **Renders a visual diagram** showing:

   * Block heights
   * Trapped water between blocks
4. Displays the **total units of water stored**

---

## Algorithm Used

### Two-Pointer Approach (O(n) Time Complexity)

* Initialize two pointers: `left` and `right`
* Track:

  * `leftMax` → maximum height seen from the left
  * `rightMax` → maximum height seen from the right
* At each step:

  * Water trapped at a position =
    `min(leftMax, rightMax) - currentHeight`
* Accumulate total water units

This approach ensures:

* **Linear time complexity**
* **Constant space usage**
* Optimal performance for large inputs

---

## Visualization Technique

* **SVG (Scalable Vector Graphics)** is used for rendering
* Each block is drawn as a rectangle
* Trapped water is drawn on top of blocks using a different color
* X and Y axes are dynamically generated
* Visualization scales automatically based on maximum height

### Legend

* **Gray blocks** → Building blocks
* **Blue blocks** → Trapped water

---

## Technology Stack

* **HTML5** – Structure
* **CSS3** – Styling and layout
* **Vanilla JavaScript** – Logic and DOM manipulation
* **SVG** – Scalable visualization

No external libraries or frameworks were used.

---

## Project Structure

```text
water-tank/
│
├── index.html     # UI structure
├── style.css      # Styling and layout
├── script.js      # Logic, algorithm & SVG rendering
└── README.md      # Documentation
```

---

## How to Run the Application

### Option 1: Live Server (Recommended)

1. Open the project folder in **VS Code**
2. Right-click on `index.html`
3. Select **Open with Live Server**
4. Enter input values and click **Compute**

### Option 2: Direct Browser Open

1. Double-click `index.html`
2. Open it in any modern browser
3. Enter input values and click **Compute**

---

## Sample Input & Output

### Input

```text
0,4,0,0,0,0,6,0,6,4,0
```

### Output

```text
Total Water Stored: 18 Units
```

### Visualization

* Blocks rendered based on heights
* Water displayed between blocks
* Axes show index and height reference

---

## Key Features

* ✅ Interactive input handling
* ✅ Real-time water calculation
* ✅ SVG-based scalable visualization
* ✅ Clean UI with legends and explanations
* ✅ Efficient O(n) algorithm
* ✅ Production-ready frontend structure

---

## Learning Outcomes

* Deep understanding of the **Rainwater Trapping problem**
* Hands-on experience with **algorithm visualization**
* Improved frontend skills using **pure JavaScript**
* SVG rendering and coordinate mapping
* Writing clean, maintainable UI logic

---

## Conclusion

This project successfully demonstrates how an algorithmic problem can be transformed into a **clear, interactive, and visual web application**.
The solution is efficient, scalable, and aligns with real-world frontend engineering practices.