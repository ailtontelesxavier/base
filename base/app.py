from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='base/static'), name='static')
app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory='base/templates')



@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})
