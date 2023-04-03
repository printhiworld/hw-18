from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("status") == 'new':
            movies = self.dao.get_by_status()

        else:
            movies = self.dao.get_all()

        if filters.get("page") is not None:
            return movies.limit(12).offset((filters.get("page") - 1) * 12)
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)

    def get_by_page(self, page):
        movies = MovieService.get_all()
        return self.session.query(Movie).group_by(Movie.id).all()

