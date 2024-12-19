# TheSettlements

```bash
docker run --name settlements-postgres -e POSTGRES_DB=settlements -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -p 15432:5432 -d postgres:17-bookworm
```

`export $(xargs < .env)`
