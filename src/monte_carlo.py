import numpy as np
import math
from src.option import Option

def monte_carlo_price(option, num_simulations=100000):
    Z = np.random.normal(0, 1, size=num_simulations)
    S_T = option.spot_price * np.exp((option.risk_free_rate - option.volatility**2 / 2)* option.time_to_maturity + (option.volatility * np.sqrt(option.time_to_maturity) * Z)) 
    payoffs = np.maximum(S_T - option.strike_price, 0) if option.option_type == "call" else np.maximum(option.strike_price - S_T, 0)
    price = sum(payoffs) * (math.exp(-option.risk_free_rate * option.time_to_maturity)/num_simulations)  
    return price