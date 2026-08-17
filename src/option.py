class Option:
    def __init__(self, S, K, T, r, sigma, option_type):
        if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
            raise ValueError(
                "Spot price, strike price, time to maturity, and volatility must all be strictly positive."
            )
        if option_type not in ("call", "put"):
            raise ValueError(f"Invalid option_type '{option_type}': must be 'call' or 'put'.")

        self.spot_price = S
        self.strike_price = K
        self.time_to_maturity = T
        self.risk_free_rate = r          # can be negative (e.g. ECB/BOJ negative rate periods)
        self.volatility = sigma
        self.option_type = option_type

    def payoff(self, S_T):
        """Payoff at maturity given a realized final price S_T."""
        if self.option_type == "call":
            return max(S_T - self.strike_price, 0)
        elif self.option_type == "put":
            return max(self.strike_price - S_T, 0)
        else:
            raise ValueError(f"Invalid option_type '{self.option_type}': must be 'call' or 'put'.")