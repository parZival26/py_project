from fastapi import FastAPI, Request, Body, Path, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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

@app.get('/movies', tags = ['Movies'])
def get_moives():
    return movies

@app.get('/movies/{id}', tags = ['Movies'])
def get_movie(id: int = Path(ge= 1, le=2000)):
	movie = list(filter(lambda m: m["id"] == id, movies))
	return movie if len(movie) > 0 else {"message": "Movie not found"}

@app.get('/movies/', tags = ['Movies'])
def get_movie_category(category: str = Query(max_length=30)):
	movie = list(filter(lambda x: x["category"] == category, movies))
	return movie

@app.post('/movies/', tags = ['Movies'])
def create_movie(movie: Movie):
	movies.append(movie)
	return movies

@app.put('/movies/{id}', tags=['Movies'])
def modify_movies(id: int, movie: Movie):
	for i in movies:
		if i["id"] == id:
			i["title"] = movie.title
			i["overview"] = movie.overview
			i["year"] = movie.year
			i["rating"] = movie.rating
			i["category"] = movie.category
			return movies
		else:
			return {"message": "Movie not found"}

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
	for i in movies:
		if i['id'] == id:
			movies.remove(i)
			return movies, {'movie deleted'}
		else:
			return {"message": "Movie not found"}
