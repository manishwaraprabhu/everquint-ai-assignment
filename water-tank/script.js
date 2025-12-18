function computeWater() {
    const input = document.getElementById("inputHeights").value.trim();

    if (!input) {
        alert("Please enter block heights");
        return;
    }

    const heights = input.split(",").map(Number);
    if (heights.some(isNaN)) {
        alert("Invalid input format");
        return;
    }

    document.getElementById("infoBox").style.display = "none";

    const svg = document.getElementById("tankCanvas");
    svg.style.display = "block";
    svg.innerHTML = "";

    const total = calculateWater(heights);
    document.getElementById("result").innerText =
        `Total Water Stored: ${total} Units`;

    drawVisualization(heights);
}

function calculateWater(arr) {
    let l = 0, r = arr.length - 1;
    let lMax = 0, rMax = 0, water = 0;

    while (l < r) {
        if (arr[l] < arr[r]) {
            lMax = Math.max(lMax, arr[l]);
            water += lMax - arr[l];
            l++;
        } else {
            rMax = Math.max(rMax, arr[r]);
            water += rMax - arr[r];
            r--;
        }
    }
    return water;
}

function drawVisualization(heights) {
    const svg = document.getElementById("tankCanvas");
    const svgHeight = 300;
    const baseY = 260;
    const blockWidth = 40;
    const gap = 10;
    const maxHeight = Math.max(...heights);
    const scale = 180 / maxHeight;

    // ---------- AXES ----------
    drawAxes(svg, heights.length, maxHeight);

    // ---------- WATER PRE-CALC ----------
    const water = [];
    let leftMax = 0;
    const rightMax = Array(heights.length).fill(0);
    let rMax = 0;

    for (let i = heights.length - 1; i >= 0; i--) {
        rMax = Math.max(rMax, heights[i]);
        rightMax[i] = rMax;
    }

    for (let i = 0; i < heights.length; i++) {
        leftMax = Math.max(leftMax, heights[i]);
        water[i] = Math.min(leftMax, rightMax[i]) - heights[i];
    }

    // ---------- DRAW BLOCKS & WATER ----------
    heights.forEach((h, i) => {
        const x = 60 + i * (blockWidth + gap);
        const blockH = h * scale;

        // Block
        drawRect(svg, x, baseY - blockH, blockWidth, blockH, "#6b7280");

        // Water
        if (water[i] > 0) {
            drawRect(
                svg,
                x,
                baseY - blockH - water[i] * scale,
                blockWidth,
                water[i] * scale,
                "#38bdf8"
            );
        }
    });
}

function drawAxes(svg, xCount, yMax) {
    // Y Axis
    drawLine(svg, 50, 20, 50, 260);
    for (let i = 0; i <= yMax; i++) {
        const y = 260 - (i * 180) / yMax;
        drawText(svg, 30, y + 5, i);
    }

    // X Axis
    drawLine(svg, 50, 260, 820, 260);
    for (let i = 0; i < xCount; i++) {
        const x = 60 + i * 50;
        drawText(svg, x + 10, 285, i);
    }
}

function drawRect(svg, x, y, w, h, color) {
    const r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    r.setAttribute("x", x);
    r.setAttribute("y", y);
    r.setAttribute("width", w);
    r.setAttribute("height", h);
    r.setAttribute("fill", color);
    svg.appendChild(r);
}

function drawLine(svg, x1, y1, x2, y2) {
    const l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", x1);
    l.setAttribute("y1", y1);
    l.setAttribute("x2", x2);
    l.setAttribute("y2", y2);
    l.setAttribute("stroke", "#000");
    svg.appendChild(l);
}

function drawText(svg, x, y, text) {
    const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
    t.setAttribute("x", x);
    t.setAttribute("y", y);
    t.setAttribute("font-size", "12");
    t.textContent = text;
    svg.appendChild(t);
}