from flask import request
from flask_restx import Resource, Namespace
from decorator import auth_required, admin_required
from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        status = (request.args.get('status'))
        if status == 'new':
            objs = movie_service.get_all(status)
            return MovieSchema(many=True).dump(objs)
        page = (request.args.get('page'))
        if page is not None:
            objs = movie_service.get_by_page(page)
            return MovieSchema(many=True).dump(objs)

        objs = movie_service.get_all()
        return MovieSchema(many=True).dump(objs)


    '''@auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "director_id": director,
            "genre_id": genre
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200'''
    @admin_required

    def post(self):
        req_json = request.json
        movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    @auth_required

    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200

    @admin_required
    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    @admin_required
    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
