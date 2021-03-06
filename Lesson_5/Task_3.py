class MyCon:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'a+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
