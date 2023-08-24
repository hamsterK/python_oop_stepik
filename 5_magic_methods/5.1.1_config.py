class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)
