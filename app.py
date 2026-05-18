import streamlit as st
import pandas as pd
import plotly.express as px
from generator import generate_market_chaos
from optimizer import allocate_resources

# Page Config
st.set_page_config(page_title="Ali Informatics Decision Support", layout="wide")

st.title("Stochastic Resource Optimizer")
st.caption("🔬 Mode: Advanced Stochastic Simulation & Articulated Data Environment")
st.markdown("---")

# Sidebar - Controls
st.sidebar.header("Simulation Parameters")
days_to_sim = st.sidebar.slider("Simulation Horizon (Days)", 7, 90, 30)

# Generate Data
df = generate_market_chaos(days=days_to_sim)

# Layout: Metric Row
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Avg Fuel Price", f"${df['fuel_price_usd'].mean():.2f}")
with col2:
    st.metric("Max Demand Record", int(df['resource_demand'].max()))
with col3:
    st.metric("Model Status", "Online")

# Layout: Visualizing "Market Chaos"
st.subheader("Synthetic Market Environment")
fig = px.line(df, x='day', y=['fuel_price_usd', 'resource_demand'], 
              title="Stochastic Trends: Fuel vs. Demand",
              labels={"value": "Scale", "variable": "Metric"})
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("🎯 Real-Time Decision Support")

# Explicit notice to user about model framework
st.info("💡 **Simulation Note:** This system models an asset fleet capped at **50 units**. Each unit handles a maximum capacity of **12 demand points**.")

input_col, result_col = st.columns(2)

with input_col:
    st.write("Input Live Parameters (Press Enter to update):")
    fuel_input = st.number_input("Current Fuel Price ($)", value=float(df['fuel_price_usd'].iloc[-1]), min_value=0.0)
    # Adding strict upper boundaries to enforce rationality
    demand_input = st.number_input("Forecasted Demand (Max: 500)", value=int(df['resource_demand'].iloc[-1]), min_value=0)

# Dynamic Validation & Immediate Execution (No button required)
with result_col:
    if demand_input > 500:
        st.error("⚠️ **System Boundary Exception:** The entered demand exceeds the rational capacity limits of our operational fleet model (Max: 500). Please input a realistic operational volume.")
    else:
        # Executes automatically when parameters change
        units, profit = allocate_resources(fuel_input, demand_input)
        
        st.success(f"**Recommendation:** Deploy **{units}** Units")
        if profit >= 0:
            st.info(f"**Expected Profit:** ${profit:,}")
        else:
            st.error(f"**Projected Net Loss:** ${profit:,} (Overhead exceeds margins)")
            
        st.write(f"At {units} units, the fleet safely handles {min(units * 12, demand_input)} units of market demand.")