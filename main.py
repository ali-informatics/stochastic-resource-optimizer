from fastapi import FastAPI
from optimizer import allocate_resources

# Initialize the API
app = FastAPI(title="Ali Informatics Decision Support")

@app.get("/")
def home():
    return {"status": "Online", "model": "Stochastic Resource Optimizer v1.0"}

@app.get("/optimize")
def get_optimization(fuel: float, demand: int):
    """
    Step 3: Software Engineering - The API Endpoint
    Exposes the logic to the web.
    """
    units, profit = allocate_resources(fuel, demand)
    
    return {
        "input_parameters": {
            "fuel_price": fuel,
            "market_demand": demand
        },
        "recommendation": {
            "optimal_units_to_deploy": units,
            "expected_profit_usd": profit
        }
    }