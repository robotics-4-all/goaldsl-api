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
uvicorn goaldsl_api:http_api --reload --port 8080
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

or 

```
docker run -it --network=host goaldsl-api
```

to also enable execution of goal checkers.

# API Endpoints

`GET /validate/base64`

`POST /validate/file`

`POST /generate`

`POST /execute`


Deploy and go to `http://localhost:8080/docs` for more information.
