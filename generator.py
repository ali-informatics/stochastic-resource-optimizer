import numpy as np
import pandas as pd

def generate_market_chaos(days=30):
    """
    Step 1: Quant Research - Stochastic Data Generation
    Simulates volatile fuel prices and demand using a random walk.
    """
    np.random.seed(42) # For reproducibility
    
    # Simulating Fuel Prices (Mean-reverting stochastic process)
    fuel_base = 3.50
    fuel_prices = fuel_base + np.cumsum(np.random.normal(0, 0.05, days))
    
    # Simulating Resource Demand (Poisson distribution for randomness)
    demand = np.random.poisson(lam=100, size=days)
    
    df = pd.DataFrame({
        'day': range(1, days + 1),
        'fuel_price_usd': fuel_prices,
        'resource_demand': demand
    })
    
    return df

if __name__ == "__main__":
    chaos_data = generate_market_chaos()
    print("--- Synthetic Market Environment Loaded ---")
    print(chaos_data.head())