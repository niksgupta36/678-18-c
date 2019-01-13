class Base(object):
   

    def __init__(self, options):
        self.options = options

    def run(self):
        raise NotImplementedError('Error occurred!')

