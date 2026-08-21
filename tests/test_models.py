import pytest 
import numpy as np 
from src.option import Option
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price

def test_option_rejects_negative_spot():
    with pytest.raises(ValueError):
        Option(S=-100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")

def test_option_price_rejects_invalid_type():
    with pytest.raises(ValueError):
        Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="")

def test_call_payoff_in_the_money():
    call = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
    assert call.payoff(110) == 10
def test_call_payoff_out_of_the_money():
    call = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
    assert call.payoff(90) == 0

def test_put_payoff_in_the_money():
    put = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="put")
    assert put.payoff(90) == 10

def test_put_payoff_out_of_the_money():
    put = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="put")
    assert put.payoff(100) == 0

def test_black_scholes_call_matches_known_value():
    call = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
    assert black_scholes_price(call) == pytest.approx(10.450583572185565, rel=0.0001)

def test_monte_carlo_call_matches_black_scholes():
    np.random.seed(42)
    call = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
    mc_price = monte_carlo_price(call)
    bs_price = black_scholes_price(call)
    assert mc_price == pytest.approx(bs_price, rel=0.02)
    

    