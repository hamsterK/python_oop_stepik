def is_context_manager(obj):
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')


class ContextManager:
    def __init__(self):
        self.inside = False

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.inside = False
        return True


print(is_context_manager(ContextManager()))
