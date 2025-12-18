import streamlit as st
from max_profit import find_max_profit

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Max Profit Problem",
    layout="wide"
)

# ---------------- CONSTANTS ----------------
THEATRE_TIME = 5
PUB_TIME = 4
PARK_TIME = 10

THEATRE_EARN = 1500
PUB_EARN = 1000
PARK_EARN = 2000

# ---------------- TITLE ----------------
st.title("🏗️ Max Profit Problem")
st.markdown(
    "Find the optimal combination of properties to maximize earnings on Mr. X's infinite Martian land."
)

st.divider()

# ---------------- AVAILABLE PROPERTIES ----------------
st.subheader("🏘️ Available Properties")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎭 Theatre")
    st.write("**Build Time:** 5 units")
    st.write("**Land:** 2 × 1")
    st.write("**Earning / Unit:** $1500")
    st.write("**Efficiency:** $300 per time unit")

with col2:
    st.markdown("### 🍺 Pub")
    st.write("**Build Time:** 4 units")
    st.write("**Land:** 1 × 1")
    st.write("**Earning / Unit:** $1000")
    st.write("**Efficiency:** $250 per time unit")

with col3:
    st.markdown("### 🏢 Commercial Park")
    st.write("**Build Time:** 10 units")
    st.write("**Land:** 3 × 1")
    st.write("**Earning / Unit:** $2000")
    st.write("**Efficiency:** $200 per time unit")

st.divider()

# ---------------- INPUT & OUTPUT SECTION ----------------
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("⏱️ Time Input")
    total_time = st.number_input(
        "Enter Total Time Units",
        min_value=1,
        step=1
    )

    calculate = st.button("💰 Calculate Maximum Profit")

with right_col:
    st.subheader("📊 Optimal Solution")

    if calculate:
        earnings, solutions = find_max_profit(total_time)

        # Show maximum profit
        st.success(f"**Maximum Profit:** ${earnings}")

        # Use only the first optimal solution
        sol = solutions[0]

        st.markdown("**Optimal Construction Mix:**")
        st.write(
            f"- Theatre: {sol['T']} | Pub: {sol['P']} | Commercial Park: {sol['C']}"
        )

        # ---------------- Earnings Breakdown ----------------
        st.markdown("### 💵 Earnings Breakdown")

        current_time = 0
        theatre_earnings = 0
        pub_earnings = 0
        park_earnings = 0

        # Build theatres
        for _ in range(sol["T"]):
            current_time += THEATRE_TIME
            if current_time <= total_time:
                theatre_earnings += (total_time - current_time) * THEATRE_EARN

        # Build pubs
        for _ in range(sol["P"]):
            current_time += PUB_TIME
            if current_time <= total_time:
                pub_earnings += (total_time - current_time) * PUB_EARN

        # Build commercial parks
        for _ in range(sol["C"]):
            current_time += PARK_TIME
            if current_time <= total_time:
                park_earnings += (total_time - current_time) * PARK_EARN

        if sol["T"] > 0:
            st.write(f"Theatre × {sol['T']} → **${theatre_earnings}**")
        if sol["P"] > 0:
            st.write(f"Pub × {sol['P']} → **${pub_earnings}**")
        if sol["C"] > 0:
            st.write(f"Commercial Park × {sol['C']} → **${park_earnings}**")

        st.divider()

        # ---------------- Formula Explanation ----------------
        st.markdown("### 📐 Earnings Formula")

        st.markdown(
            """
            **Earnings = Σ (Remaining Time After Construction × Earning Rate)**

            **Where:**
            - Remaining Time = Total Time − Cumulative Construction Time  
            - Earning Rate depends on the property type:
                - Theatre → $1500 per unit time  
                - Pub → $1000 per unit time  
                - Commercial Park → $2000 per unit time  

            The calculation is done sequentially since **only one property
            can be constructed at a time**.
            """
        )

    else:
        st.info("Enter time units and click **Calculate Maximum Profit**.")