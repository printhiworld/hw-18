from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, bid,  user_d):
        user = self.get_one(bid)
        user.email = user_d["email"]
        user.password = user_d["password"]
        user.name = user_d["name"]
        user.surname = user_d["surname"]
        user.favorite_genre = user_d["favorite_genre"]

        self.session.add(user)
        self.session.commit()
