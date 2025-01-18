## Run alembic migrations

### Configuration

```bash
$ cp alembic.ini.example alembic.ini
```
- update the `sqlalchemy.url` in the `alembic.ini` file to point to your database

### (Optional) Create a new migration

```bash
$ alembic revision --autogenerate -m "migration_name"
```

### Run migrations

```bash
$ alembic upgrade head
```