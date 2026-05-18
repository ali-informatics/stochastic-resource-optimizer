# 📊 Stochastic Resource Optimizer: Uncertainty-Aware Decision Support

An elite decision support engine that bridges quantitative research, data engineering, and interactive software to solve resource allocation problems under volatile market conditions.

---

## 💡 The Core Problem (Explained Simply)
Imagine you run a logistics fleet. Every day, two massive variables completely escape your control:
1. **Market Demand:** How many shipments do customers want to move? (Simulated using a Poisson distribution).
2. **Fuel Prices:** How much will it cost to run your fleet? (Simulated using a Mean-Reverting Random Walk).

If you deploy too few assets, you leave money on the table. If you deploy too many, fixed operational overhead and high fuel costs eat your margins alive. This system solves that exact trade-off in real-time.

---

## 🛠️ The Architecture (The "Dreigliedrig" Ecosystem)

The project is modularly isolated into distinct operational layers:

1. **`generator.py` (Quant Research Layer):** Simulates 30 days of "market chaos" using stochastic mathematical frameworks instead of static data points.
2. **`optimizer.py` (Decision Science Engine):** Evaluates every possible deployment scenario to find the absolute maximum mathematical profit for that exact fuel-and-demand combination.
3. **`main.py` (Software Engineering Core):** Wraps the optimization logic inside a high-performance **FastAPI** web service.
4. **`app.py` (The Interactive UI):** A minimalist **Streamlit** dashboard visualizing market trend lines and acting as a tactical decision-making terminal.