from risk import tickerline
from risk.var import historical_var, position_var


def test_historical_var_of_a_rising_series_is_zero():
    assert historical_var([1, 2, 3, 4]) == 0.0


def test_historical_var_picks_the_tail_loss():
    closes = [100, 90, 99, 100, 101, 102, 103, 104, 105, 106, 107]
    assert round(historical_var(closes, 0.9), 2) == 0.10


def test_position_var_uses_live_prices():
    v = position_var("ORBT", 100, days=60)
    assert v["symbol"] == "ORBT"
    assert v["exposure"] > 0
    assert 0 <= v["var"] <= v["exposure"]
    assert v["currency"] in ("USD", "EUR")


def test_intraday_series_has_two_hours():
    assert len(tickerline.intraday_closes("TLX")) == 120
