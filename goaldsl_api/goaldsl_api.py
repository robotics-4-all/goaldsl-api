"""Main module."""

import uuid
import os
import base64
from typing import Optional

import tarfile

from goal_dsl.utils import build_model
from goal_gen.generator import generate as generate_model

from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import HTMLResponse, FileResponse


http_api = FastAPI()


@http_api.get("/", response_class=HTMLResponse)
async def root():
    return """
<html>
<head>
<style>
html,body{
    margin:0;
    height:100%;
}
img{
  display:block;
  width:100%; height:100%;
  object-fit: cover;
}
</style>
</head>
<body>
 <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fnews.images.itv.com%2Fimage%2Ffile%2F492835%2Fimg.jpg&f=1&nofb=1" alt="">
</body>
</html>
    """


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
        f'model_for_validation-{u_id}.goal'
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
async def validate_b64(fenc: str = ''):
    if len(fenc) == 0:
        return 404
    resp = {
        'status': 200,
        'message': ''
    }
    fdec = base64.b64decode(fenc)
    u_id = uuid.uuid4().hex[0:8]
    fpath = os.path.join(
        '/tmp',
        'model_for_validation-{}.goal'.format(u_id)
    )
    with open(fpath, 'wb') as f:
        f.write(fdec)
    try:
        model, _ = build_model(fpath)
    except Exception as e:
        resp['status'] = 404
        resp['message'] = e
    return resp


@http_api.post("/generate")
async def generate(model_file: UploadFile = File(...)):
    print(f'Generate for request: file=<{model_file.filename}>,' + \
          f' descriptor=<{model_file.file}>')
    resp = {
        'status': 200,
        'message': ''
    }
    fd = model_file.file
    u_id = uuid.uuid4().hex[0:8]
    model_path = os.path.join(
        '/tmp',
        f'model-{u_id}.goal'
    )
    tarball_path = os.path.join(
        '/tmp',
        f'{u_id}.tar.gz'
    )
    gen_path = os.path.join(
        '/tmp',
        f'gen-{u_id}'
    )
    with open(model_path, 'w') as f:
        f.write(fd.read().decode('utf8'))
    try:
        out_dir = generate_model(model_path, gen_path)
        make_tarball(tarball_path, out_dir)
        print(f'Sending tarball {tarball_path}')
        return FileResponse(tarball_path,
                            filename=os.path.basename(tarball_path),
                            media_type='application/x-tar')
    except Exception as e:
        print(e)
        resp['status'] = 404
        return resp


def make_tarball(fout, source_dir):
    with tarfile.open(fout, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
