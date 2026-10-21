# marketdata-client-graphql

A value-at-risk engine on the Tickerline market data **GraphQL** API (v1), in Python with
the standard library only. The operations it sends live in `risk/queries.graphql`.

```sh
pip install -r requirements.txt
pytest
```

When Tickerline releases v2, biject rewrites `risk/queries.graphql` through its syntax
tree (`price` → `last { amount }`, `limit:` → `count:`, `MIN1` → `MINUTE1`), adapts the
code that reads the results, and opens a PR checked against the contract mock.
