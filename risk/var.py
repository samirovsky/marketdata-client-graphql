"""Historical value at risk of a position, from Tickerline daily closes."""

from risk import tickerline


def returns(closes: list[float]) -> list[float]:
    return [b / a - 1 for a, b in zip(closes, closes[1:])]


def historical_var(closes: list[float], confidence: float = 0.95) -> float:
    """The loss (as a fraction) not exceeded with the given confidence."""
    r = sorted(returns(closes))
    if not r:
        return 0.0
    index = max(0, int((1 - confidence) * len(r)) - 1)
    return max(0.0, -r[index])


def position_var(symbol: str, shares: float, days: int = 250, confidence: float = 0.95) -> dict:
    price, currency = tickerline.latest_price(symbol)
    loss = historical_var(tickerline.daily_closes(symbol, days), confidence)
    return {"symbol": symbol, "exposure": round(price * shares, 2), "var": round(price * shares * loss, 2), "currency": currency}
