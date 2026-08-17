# imports 
from src.option import Option
import math 
from scipy.stats import norm

def black_scholes_price(option):
    d1 = ((math.log(option.spot_price / option.strike_price)) + (option.risk_free_rate + (option.volatility ** 2)/2) * option.time_to_maturity)/ (option.volatility * math.sqrt(option.time_to_maturity))
    d2 = d1 - (option.volatility * math.sqrt(option.time_to_maturity))

    if option.option_type == "call":
        price = (option.spot_price * norm.cdf(d1)) - (option.strike_price * math.exp(-1 * option.risk_free_rate * option.time_to_maturity) * norm.cdf(d2))
    else:
        price = (option.strike_price * math.exp(-1 * option.risk_free_rate * option.time_to_maturity) * norm.cdf(-d2)) - (option.spot_price * norm.cdf(-d1))
    return price