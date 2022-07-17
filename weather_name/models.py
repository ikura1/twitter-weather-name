from weather_name.database import Column, PkModel, db


class User(PkModel):
    __tablename__ = "users"

    user_id = Column(db.BigInteger, unique=True, nullable=False)
    # トークン・暗号化する必要ある?
    access_token = Column(db.String(60), nullable=False)
    access_token_secret = Column(db.String(60), nullable=False)
    # 座標
    location = Column(db.String(255))
    latitude = Column(db.Float())
    longitude = Column(db.Float())

    def __init__(self, user_id, token, token_secret, **kwargs):
        """Create instance."""
        super().__init__(
            user_id=user_id,
            access_token=token,
            access_token_secret=token_secret,
            **kwargs
        )
