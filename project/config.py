# project/config.py


class BaseConfig:
	""" Base configuration """
	DEBUG = False
	TESTING = False

class DevelopmentConfig(BaseConfig):
	"""Development configuration"""
	DEBUG = True



class TestingConfig(BaseConfig)