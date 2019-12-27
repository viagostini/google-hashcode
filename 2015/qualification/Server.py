
class Server:
    def __init__(self, id, size, capacity):
        self.id = id
        self.size = size
        self.capacity = capacity
        self.ratio = float(self.capacity) / float(self.size)
        self.row = -1
        self.slot = -1
        self.pool = -1

    def __str__(self):
        return '[Server %d] size: %d, capacity: %d, ratio: %.02f, pos: (%d, %d), pool: %d'\
            % (self.id, self.size, self.capacity, self.ratio, self.row, self.slot, self.pool)