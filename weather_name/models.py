from os import access
from weather_name.database import Column, PkModel, db


class User(PkModel):
    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255), unique=True, nullable=False)
    # トークン・暗号化する必要ある?
    access_token = Column(db.String(60), nullable=False)
    access_token_secret = Column(db.String(60), nullable=False)
    # 座標
    location = Column(db.String(255))
    latitude = Column(db.Float())
    longitude = Column(db.Float())

    def __init__(self, name, token, token_secret, **kwargs):
        """Create instance."""
        super().__init__(
            name=name, access_token=token, access_token_secret=token_secret, **kwargs
        )
        # self.set_password(token)
        # self.set_token(token_secret)

    # TODO: 下記をトークン用に変更する
    def set_token(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)
