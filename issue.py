# Issue class used for testing
class Issue():
    def __init__(self, title, labels, closed):
        self.title = title
        self.labels = labels
        self.closed = closed

    def __repr__(self):
        return str(self.__class__) + ': ' + str(self.__dict__)

    def __str__(self):
        return f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}'

    def __add__(x, y):
        return [ x, y ]

    def print(self):
        if isinstance(self,list):
            for mine in self:
                mine.print
        else:
            print (f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}')
