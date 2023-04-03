from flask_restx import Resource, Namespace
from flask import request
from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}

@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get('email')
        password = req_json.get('password')

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.prove_tokens(token)
        return tokens, 201



