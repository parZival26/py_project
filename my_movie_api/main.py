from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(ErrorHandler)
app.include_router(movie_router, prefix='/movies')
app.include_router(user_router, prefix='/users')

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get('/', tags = ['Home'])
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

