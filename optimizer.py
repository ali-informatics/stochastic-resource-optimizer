import numpy as np

def allocate_resources(fuel_price, demand):
    # --- ADJUSTED CONSTANTS ---
    max_units = 50             # Increase fleet size
    revenue_per_demand = 25.0  # Increase revenue (was $5, now $25)
    operating_cost_fixed = 50  # Lower the barrier to entry
    
    best_profit = -float('inf')
    optimal_units = 0
    
    for units in range(1, max_units + 1):
        capacity = units * 12
        met_demand = min(capacity, demand)
        
        total_revenue = met_demand * revenue_per_demand
        # Each unit uses '10' fuel units
        total_cost = (units * operating_cost_fixed) + (units * fuel_price * 10)
        profit = total_revenue - total_cost
        
        if profit > best_profit:
            best_profit = profit
            optimal_units = units
            
    return optimal_units, round(best_profit, 2)

if __name__ == "__main__":
    # Test with Day 4 data from your image: Price 3.62, Demand 94
    units, profit = allocate_resources(3.62, 94)
    print(f"--- Optimization Logic Test ---")
    print(f"Optimal Units to Deploy: {units}")
    print(f"Projected Profit: ${profit}")