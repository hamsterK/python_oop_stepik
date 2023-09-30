import re


def snake_case(attrs=False):
    def decorator(cls):
        for method_name in dir(cls):
            if not method_name.startswith('__') and callable(getattr(cls, method_name)):
                if method_name.startswith('_'):
                    snake_case_name = '_' + re.sub(r'(?<!^)(?=[A-Z])', '_', method_name[1:]).lower()
                else:
                    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', method_name).lower()
                setattr(cls, snake_case_name, getattr(cls, method_name))

        if attrs:
            for attr_name in dir(cls):
                if not attr_name.startswith('__'):
                    snake_case_name = re.sub(r'(?<!^)(?=[A-Z])', '_', attr_name).lower()
                    setattr(cls, snake_case_name, getattr(cls, attr_name))
                    delattr(cls, attr_name)

        return cls

    return decorator


@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2


print(MyClass.first_attr)
print(MyClass.super_second_attr)
