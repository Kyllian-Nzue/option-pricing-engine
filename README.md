
/


















Readme · MD
# Option Pricing Engine
 
A Python implementation of European option pricing, built from scratch using two independent methods: the closed form Black Scholes formula and Monte Carlo simulation. This project was built as a way to develop a genuine, defensible understanding of option pricing, rather than to produce the widest possible feature set.
 
## Motivation and Scope
 
This project intentionally covers Black Scholes and Monte Carlo pricing for European options only. American options, which allow early exercise, are not included. This was a deliberate trade off: rather than spreading effort across a broader but shallower set of features, the scope was kept narrow so that every design decision, from input validation to the structure of the simulation, could be fully understood and explained.
 
The two pricing methods were chosen specifically because they can validate each other. Black Scholes gives an exact, instant answer through a formula. Monte Carlo arrives at an approximate answer by simulating a large number of possible outcomes and averaging them. When both methods agree closely on the same inputs, it is strong evidence that both are implemented correctly, since they reach the same conclusion through entirely different means.
 
## Features
 
- An `Option` class representing a European call or put, with input validation on construction
- A closed form Black Scholes pricer
- A vectorized Monte Carlo pricer using numpy
- An automated test suite covering input validation, payoff calculations, and both pricing methods
- A notebook containing exploratory analysis: convergence behavior, sensitivity to volatility and strike price, and a put call parity check
## Project Structure
 
```
option-pricing-engine/
├── src/
│   ├── option.py           # Option class and payoff logic
│   ├── black_scholes.py    # Closed form pricer
│   └── monte_carlo.py      # Simulation based pricer
├── tests/
│   └── test_models.py      # Automated test suite
├── notebooks/
│   └── analysis.ipynb      # Convergence, sensitivity, and parity analysis
├── requirements.txt
└── README.md
```
 
## Installation
 
Clone the repository and install the required dependencies:
 
```bash
pip install -r requirements.txt
```
 
## Running the Tests
 
The project includes an automated test suite built with pytest. From the project root:
 
```bash
pytest tests/test_models.py -v
```
 
This verifies input validation, payoff calculations for both call and put options, and that both pricing methods produce results consistent with known reference values.
 
## Example Usage
 
```python
from src.option import Option
from src.black_scholes import black_scholes_price
from src.monte_carlo import monte_carlo_price
 
call = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type="call")
 
print(black_scholes_price(call))   # closed form price
print(monte_carlo_price(call))     # simulation based price, should be close
```
 
## Key Results
 
The notebook walks through four analyses in detail:
 
**Convergence.** As the number of Monte Carlo simulations increases, the simulated price converges toward the Black Scholes price, consistent with the Law of Large Numbers. The error shrinks proportionally to the square root of the number of simulations, so the largest accuracy gains happen early, with diminishing returns beyond a certain point.
 
**Volatility sensitivity.** Both call and put prices increase as volatility rises. This follows from the shape of the payoff itself: losses are floored at zero, but gains are not capped, so a wider range of possible outcomes adds value without adding equivalent downside cost.
 
**Strike sensitivity.** As the strike price increases, call prices fall and put prices rise, crossing near the point where the strike is close to the current stock price.
 
**Put call parity.** A call price minus a put price, for options sharing the same strike, maturity, and rate, should always equal the stock price minus the discounted strike, regardless of volatility. This relationship was verified across multiple combinations of strike and volatility, and held in every case, serving as an independent check on the correctness of the Black Scholes implementation.
 
## Possible Extensions
 
This project was kept deliberately narrow in scope. Natural next steps, left out for now, include:
 
- Pricing for American options, which allow early exercise and require a different numerical approach
- Sensitivity measures beyond volatility and strike, computed directly rather than through manual sweeps
- Support for dividend paying stocks
## Notes
 
This project was built with a focus on understanding over completeness. Every formula, validation rule, and design choice in the codebase was worked through individually, with the goal of being able to explain the reasoning behind it, not just produce working code.
 
