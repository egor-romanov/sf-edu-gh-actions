# sf-edu-gh-actions

sf-education practice for github actions learning

## About the project

This is a repo for practicing GitHub actions and CI/CD for python projects built for sf education platform.

## Developing

### Poetry

To work with this project start with installing Poetry and then run:

```bash
poetry install
```

### To run an app

```bash
poetry run uvicorn app.main:app --reload --host localhost --port 9090
```

After that app will be available at `localhost:9090`

- Swagger UI at `localhost:9090/docs`

### To run tests

```bash
poetry run pytest .
```

### To run format

```bash
poetry run black
```
