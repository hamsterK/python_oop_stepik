import functools
import re


def snake_case(attrs=False):
    def decorator(cls):
        old_init = cls.__init__

        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            for method_name in dir(cls):
                if not method_name.startswith('__') and callable(getattr(cls, method_name)):
                    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', method_name).lower()
                    setattr(self, snake_case_name, getattr(self, method_name))

            if attrs: # MAPPINGPROXY! CANNOT ISE DICT!
                for attr_name, attr_value in cls.__dict__.items():
                    if not attr_name.startswith('__'):
                        snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', attr_name).lower()
                        delattr(self, attr_name)
                        setattr(self, snake_case_name, attr_value)

            old_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls
    return decorator
