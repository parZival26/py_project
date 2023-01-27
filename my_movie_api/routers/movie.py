from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService

movie_router = APIRouter()

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

@movie_router.get('/movies', tags = ['Movies'], response_model= List[Movie], status_code = 200, dependencies=[Depends(JWTBearer())])
def get_moives() -> List[Movie]:
	db = Session()
	result = MovieService(db).get_movies()
	return JSONResponse(status_code = 200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags = ['Movies'], response_model = Movie)
def get_movie(id: int = Path(ge= 1, le=2000)) -> Movie:
	try:
		db = Session()
		result = MovieService(db).get_movie(id)
		if not result:
			return JSONResponse(status_code=404, content={"error": "Movie not found"})
		return JSONResponse(content=jsonable_encoder(result), status_code=200) 
	except SQLAlchemyError as e:
		return JSONResponse(status_code=400, content={"error": str(e)})

@movie_router.get('/movies/', tags = ['Movies'], response_model = Movie)
def get_movie_category(category: str = Query(max_length=30)) -> Movie:
	db = Session()
	result = MovieService(db).get_movie_by_category(category)
	if not result:
		return JSONResponse(status_code=404, content={"message": "Movie not found"})
	return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies/', tags = ['Movies'], response_model = dict, status_code= 201)
def create_movie(movie: Movie) -> dict:
	try:
		db = Session()
		new_movie = MovieModel(**movie.dict())
		db.add(new_movie)
		db.commit()
		return JSONResponse(status_code = 201, content={"message": "Movie created successfully"})
	except SQLAlchemyError as e:
		return JSONResponse(status_code=400, content={"error": str(e)})


@movie_router.put('/movies/{id}', tags=['Movies'], response_model = dict, status_code=200)
def modify_movies(id: int, movie: Movie) -> dict:
	try:
		db = Session()
		result = MovieService(db).get_movie(id)
		if not result:
			return JSONResponse(status_code=404, content={"messa": "movie not found"})
		result.title = movie.title
		result.overview = movie.overview
		result.year = movie.year
		result.rating = movie.rating
		result.category = movie.category
		db.commit()
		return {"message": "movie modified successfully"}
	except SQLAlchemyError as e:
		return JSONResponse(status_code=400, content={"error": str(e)})

@movie_router.delete('/movies/{id}', tags=['Movies'], response_model = dict, status_code=200)
def delete_movie(id: int) -> dict:
	try:
		db = Session()
		result = MovieService(db).get_movie(id)
		if not result:
			return JSONResponse(status_code=404, content={"messa": "movie not found"})
		db.delete(result)
		db.commit()
		return {"message": "movie deleted successfully"}
	except SQLAlchemyError as e:
		return JSONResponse(status_code=400, content={"error": str(e)})