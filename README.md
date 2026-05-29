# Vasoactive Drug Speed Estimator — Backend

> Course project: Internet Application Development (5th semester), BMSTU

A Django REST API for calculating vasoactive drug administration rates. The service stores drug parameters, computes dosage and infusion speed recommendations, and exposes a documented REST interface.

## Tech Stack

- Python, Django, Django REST Framework
- PostgreSQL
- Swagger / OpenAPI (drf-yasg)

## Features

- Drug catalog with detail pages and parameters
- Administration speed estimation based on patient/dosage input
- Status tracking for each estimation record
- Full CRUD API with Swagger documentation

## Related Repositories

This project is split across three repositories:

| Repository | Description |
|---|---|
| [vasoactive_drug_speed_estimatior](https://github.com/YurchenkoK/vasoactive_drug_speed_estimatior) | Django backend (this repo) |
| [vasoactive_drug_speed_estimatior_async](https://github.com/YurchenkoK/vasoactive_drug_speed_estimatior_async) | Async version with extended features |
| [vasoactive_drug_speed_estimatior_frontend](https://github.com/YurchenkoK/vasoactive_drug_speed_estimatior_frontend) | React frontend |

## Getting Started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

API documentation available at `http://localhost:8000/swagger/`
