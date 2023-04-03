import base64
import hashlib
import hmac
from const import PWD_HASH_ITERATIONS, PWD_HASH_SALT
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        user_d["password"] = self.get_hash(user_d["password"])

        return self.dao.create(user_d)

    def update(self, bid, user_d):
        self.dao.update(bid, user_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)


    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
        #.decode("utf-8", "ignore")

    def compsre_password(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )