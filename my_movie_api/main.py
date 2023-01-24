from fastapi import FastAPI, Request, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class User(BaseModel):
	email:str
	password:str

class Movie(BaseModel):
	id: Optional[int] = None
	title: str = Field(max_length=15, min_length=1)
	overview: str = Field(max_length=50, min_length=5)
	year: int = Field(le=2023)
	rating: float = Field(ge=1, le=10)
	category: str = Field(max_length=30)

	class Config:
         schema_extra = {
			"example":{
				"id": 0,
                "title": "My movie",
				"overview": "Description of the movie",
				"year": 2023,
				"rating": 10,
				"category": "Familiar"
			}
		 }

movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": 2009,
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": 2009,
		"rating": 7.8,
		"category": "Acción"
	}
]

@app.get('/', tags = ['Home'])
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post('/login', tags=['auth'])
def login(user: User):
    return user

@app.get('/movies', tags = ['Movies'], response_model= List[Movie], status_code = 200)
def get_moives() -> List[Movie]:
    return JSONResponse(status_code = 200, content=movies)

@app.get('/movies/{id}', tags = ['Movies'], response_model = Movie)
def get_movie(id: int = Path(ge= 1, le=2000)) -> Movie:
	movie = list(filter(lambda m: m["id"] == id, movies))
	return JSONResponse(content=movie) if len(movie) > 0 else JSONResponse(status_code= 404,content={"message": "Movie not found"})

@app.get('/movies/', tags = ['Movies'], response_model = Movie)
def get_movie_category(category: str = Query(max_length=30)) -> Movie:
	movie = list(filter(lambda x: x["category"] == category, movies))
	return JSONResponse(content=movie) if len(movie) > 0 else JSONResponse(status_code= 404,content= {"message": "Movie not found"})

@app.post('/movies/', tags = ['Movies'], response_model = dict, status_code= 201)
def create_movie(movie: Movie) -> dict:
	movies.append(movie)
	return JSONResponse(status_code = 201, content={"message": "Movie created successfully"})

@app.put('/movies/{id}', tags=['Movies'], response_model = dict, status_code=200)
def modify_movies(id: int, movie: Movie) -> dict:
	for i in movies:
		if i["id"] == id:
			i["title"] = movie.title
			i["overview"] = movie.overview
			i["year"] = movie.year
			i["rating"] = movie.rating
			i["category"] = movie.category
			return JSONResponse(status_code = 200, content = movies)
		else:
			return JSONResponse(status_code = 404, content = {"message": "Movie not found"})

@app.delete('/movies/{id}', tags=['Movies'], response_model = dict, status_code=200)
def delete_movie(id: int) -> dict:
	for i in movies:
		if i['id'] == id:
			movies.remove(i)
			return JSONResponse(status_code = 200, content = {'movie deleted'})
		else:
			return JSONResponse(status_code = 404, content = {"message": "Movie not found"})