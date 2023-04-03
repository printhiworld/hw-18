import calendar
import datetime
import jwt
from const import SECRET, ALGO
from service.user import UserService
from flask import abort


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password):
        user = self.user_service.get_by_email(email)
        if not user:
            abort(400)
        if not self.user_service.compsre_password(user.password, password):
            abort(400)
        data = {
            'email' : user.email
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGO)

        return {'access_token': access_token, 'refresh_token': refresh_token}


    def prove_tokens(self, token):
        data = jwt.decode(jwt=token, key=SECRET, algorithms=[ALGO])
        email = data.get("email")

        return self.generate_tokens(email, None)