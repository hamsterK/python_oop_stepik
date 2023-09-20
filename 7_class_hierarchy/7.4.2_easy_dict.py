class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name):
        if name not in self:
            raise AttributeError(f"'EasyDict' object has no attribute '{name}'")
        return self[name]


easydict = EasyDict({'name': 'Artur', 'city': 'Almetevsk'})

easydict.age = 21
print(easydict)
