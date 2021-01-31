goaldsl-api
===========

Web API for goal-dsl


* Free software: MIT license
* Documentation: https://goaldsl-api.readthedocs.io.

# Install

```bash
pip install .
```

# Run on host

Run with:

`
uvicorn goaldsl_api:http_api --reload --port 8000
`

Look at https://www.uvicorn.org/ for more information about the Uvicorn
ASGI server and how to use it.

# Build docker image and run in a container

**Build Docker Image**:

First clone [goal-dsl](https://github.com/robotics-4-all/goal-dsl) repo in `./third_parties` directory.

```
docker build -t goaldsl-api .
```

**Run Container**:

```
docker run -it -p 8080:80 goaldsl-api
```

# API Endpoints

`GET /validate/base64`

`POST /validate/file`

Deploy and go to `http://localhost:8000/docs` for more information.
