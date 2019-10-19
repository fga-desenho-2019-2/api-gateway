class BaseConfig:
    TESTING = False


class DevConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True