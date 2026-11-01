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

## Try biject on your own copy

1. **Use this template** (top right) → create the repository in your own account.
2. Open Tickerline's [migration guide](https://biject-demo.vercel.app/migrate/samirovsky/tickerline-marketdata) → **Migrate my client** → install biject
   on your copy only.
3. biject opens a setup PR adding its `verify` workflow, then runs the migration **in your
   own GitHub Actions** (your code never leaves your CI) and opens a pull request: every
   changed call site labelled, your tests run against Tickerline's v2 contract mock, and the
   patch re-checked by `api-migrations verify`.
