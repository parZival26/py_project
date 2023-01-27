from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags = ['Movies'], response_model= List[Movie], status_code = 200, )
#se borro dependencies=[Depends(JWTBearer())] esta line va despues de staus code arriba fue eliminada porque su funcion es de añadir un seguro que te pide inicar session
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
        MovieService(db).add_movie(movie)
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
		MovieService(db).update_movie(id, movie)
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
		MovieService(db).delete_movie(id)
		return {"message": "movie deleted successfully"}
	except SQLAlchemyError as e:
		return JSONResponse(status_code=400, content={"error": str(e)})