goaldsl-api
===========

Web API for goal-dsl


* Free software: MIT license
* Documentation: https://goaldsl-api.readthedocs.io.

# Install

```bash
pip install .
```

# Usage

Run with:

`
uvicorn goaldsl_api:http_api --reload --port 8000
`

Look at https://www.uvicorn.org/ for more information about the Uvicorn
ASGI server and how to use it.

# API Endpoints

`GET /validate/base64`

`POST /validate/file`

Deploy and go to `http://localhost:8000/docs` for more information.
