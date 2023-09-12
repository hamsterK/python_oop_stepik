class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.obj.close()
        except AttributeError:
            print('Незакрываемый объект')
        return True


with Closer(5) as i:
    i += 1

print(i)
