"""Tickerline market data over GraphQL (stdlib only)."""

import json
import os
import urllib.request
from pathlib import Path

ENDPOINT = "https://tickerline-api.fly.dev/api/v1/graphql"
DOCUMENTS = (Path(__file__).parent / "queries.graphql").read_text()


class TickerlineError(RuntimeError):
    pass


def query(operation: str, variables: dict) -> dict:
    body = json.dumps({"query": DOCUMENTS, "operationName": operation, "variables": variables}).encode()
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"content-type": "application/json", "x-tickerline-key": os.environ.get("TICKERLINE_KEY", "demo")},
    )
    with urllib.request.urlopen(req, timeout=20) as res:
        payload = json.load(res)
    if payload.get("errors"):
        raise TickerlineError("; ".join(e["message"] for e in payload["errors"]))
    return payload["data"]


def latest_price(symbol: str) -> tuple[float, str]:
    q = query("Quote", {"symbol": symbol})["quote"]
    if q is None:
        raise TickerlineError(f"unknown symbol {symbol}")
    return q["price"], q["currency"]


def daily_closes(symbol: str, days: int) -> list[float]:
    return [c["c"] for c in query("DailyCloses", {"symbol": symbol, "days": days})["candles"]]


def intraday_closes(symbol: str) -> list[float]:
    return [c["c"] for c in query("IntradayCloses", {"symbol": symbol})["candles"]]
