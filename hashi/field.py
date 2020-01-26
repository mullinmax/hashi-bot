class field():

    def __init__(self, x, y):
        self.grid = [[0 for i in range(x)] for j in range(y)]
        self.bridges = []
        self.x = x
        self.y = y

    def place_bridge(x1, y1, x2, y2):
        if self.grid is None:
            raise 'grid is not initialized'
        if x1 in range(self.x) and x2 in range(self.x):
            raise 'invalid x'
        if y1 in range(self.y) and y2 in range(self.y):
            raise 'invalid y'
        if x1 == x2 and y1 == y2:
            raise 'zero length bridge'
        if x1 != x2 and y1 != y2:
            raise 'diagonal bridge'
        if x1 == x2 and y1 != y2:
            # vertical

        elif x1 != x2 and y1 == y2:
            # horizontal

        else:
            raise 'something weird has happened'
