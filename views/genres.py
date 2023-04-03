from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        objs = genre_service.get_all()
        return GenreSchema(many=True).dump(objs), 200

    def post(self):
        obj = genre_service.create(request.json)
        return GenreSchema().dump(obj), 201, {'location':f'/genre/{obj.id}'}


@genre_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        obj = genre_service.get_one(pk)
        return GenreSchema().dump(obj), 200

    def delete(self, pk):
        genre_service.delete(pk)
        return 'удалено', 204

    def update(self, pk):
        obj = genre_service.update(pk, request.json)
        return GenreSchema().dump(obj), 200
