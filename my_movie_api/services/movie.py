from models.movie import Movie as MovieModel

class MovieService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        return self.db.query(MovieModel).all()

    def get_movie(self, id):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movie_by_category(self, category):
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
