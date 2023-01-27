from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        return self.db.query(MovieModel).all()

    def get_movie(self, id):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movie_by_category(self, category):
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    def add_movie(self, movie: Movie):
        self.db.add(MovieModel(**movie.dict()))
        self.db.commit()
        return

    def update_movie(self, id: int, movie: Movie):
        result = self.db.query(MovieModel).filter(MovieModel.id == id)
        data = movie.dict(exclude_unset=True)

        exclude_fields = ["id"]
        if all(field in list(data.keys()) for field in exclude_fields):
            raise Exception("Ha agregado campos no editables")
        
        result.update(data)
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()