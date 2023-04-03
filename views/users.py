from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service
from dao.model.user import UserSchema

user_ns = Namespace('user')


@user_ns.route('/<int:bid>')
class UserView(Resource):

    def get(self, bid):
        user = user_service.get_one(bid)
        return UserSchema(many=True).dump(user)

    def update(self, bid):
        user_service.update(bid, request.json)
        return "", 204

@user_ns.route('/password/<int:bid>')
class UserView(Resource):
    def update(self, bid):
        user_service.update(bid, request.json)
        return "", 204

#,