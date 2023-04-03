from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        objs = director_service.get_all()
        return DirectorSchema(many=True).dump(objs)

    def post(self):
        obj = director_service.create(request.json)
        return DirectorSchema().dump(obj), 201, {'location':f'/genre/{obj.id}'}


@director_ns.route('/<int:pk>')
class DirectorsView(Resource):
    def get(self, pk):
        obj = director_service.get_one(pk)
        return DirectorSchema().dump(obj)

    def delete(self, pk):
        director_service.delete(pk)
        return 'удалено'

    def update(self, pk):
        obj = director_service.update(pk, request.json)
        return DirectorSchema().dump(obj)
