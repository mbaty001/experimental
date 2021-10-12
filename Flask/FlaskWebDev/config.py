class Config(object):
	POSTS_PER_PAGE = 10

class ProdConfig(Config):
	SECRET_KEY = b'\x1e\xb1q%\xd4\x80\xe7\xc3\xd1}-\xfcI\xbb\x95\x12\x04\xacm\nJt\xee\x06'

class DevConfig(Config):
	debug = True
	SECRET_KEY = b'3\x8a?\xa5\xcf#\xdd\xcepVash\xdf\xac\x00\x01gm\x0e?DQ\xf4'
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

