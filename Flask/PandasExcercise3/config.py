import pandas as pd

class Config():
    TESTING = False

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATA = pd.read_csv("cities.csv")

class TestingConfig(Config):
    TESTING = True
    DATA = pd.read_csv("cities.csv")