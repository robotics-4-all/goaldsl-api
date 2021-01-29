"""Main module."""

import uuid
import os
import base64

from typing import Optional

from goal_dsl.utils import build_model

from fastapi import FastAPI, File, UploadFile

http_api = FastAPI()


@http_api.get("/")
async def root():
    return {"message": "This is the GoalDSL Web API!"}

@http_api.post("/validate/file")
async def validate_file(file: UploadFile = File(...)):
    print(f'Validation for request: file=<{file.filename}>,' + \
          f' descriptor=<{file.file}>')
    resp = {
        'status': 200,
        'message': ''
    }
    fd = file.file
    u_id = uuid.uuid4().hex[0:8]
    fpath = os.path.join(
        '/tmp',
        'model_for_validation.goal'
    )
    with open(fpath, 'w') as f:
        f.write(fd.read().decode('utf8'))
    try:
        model, _ = build_model(fpath)
    except Exception as e:
        resp['status'] = 404
        resp['message'] = e
    return resp

@http_api.get("/validate/base64")
async def validate_b63(fenc: str = ''):
    if len(fenc) == 0:
        return 404
    fdec = base64.b64decode(fenc)
    u_id = uuid.uuid4().hex[0:8]
    fpath = os.path.join(
        '/tmp',
        'model_for_validation-{}.goal'.format(u_id)
    )
    with open(fpath, 'wb') as f:
        f.write(fdec)
    model, _ = build_model(fpath)
    resp = {
        'status': 200,
        'message': ''
    }
    return resp
