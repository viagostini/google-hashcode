from Server import Server

class DataCenter:
    def __init__(self, rows, slots, unavailable, pools, num_servers):
        self.rows = rows
        self.slots = slots
        self.unavailable = unavailable
        self.pools = pools
        self.num_servers = num_servers
        self.grid = []
        self.servers = []
        self.build_grid()

    def build_grid(self):
        for i in range(self.rows):
            self.grid.append(['.'] * self.slots)

    def mark_unavailable(self, input):
        line = input.readline()
        row, slot = [int(num) for num in line.split()]
        self.grid[row][slot] = 'x'

    def create_servers(self, input):
        for i in range(self.num_servers):
            line = input.readline()
            size, capacity = [int(num) for num in line.split()]
            self.servers.append(Server(i, size, capacity))

    def __str__(self):
        """ Draw datacenter grid """
        return '\n'.join(['[ %s ]' % ''.join(row) for row in self.grid])

    def info(self):
        """ Display info about datacenter specs """
        print('Rows: {}\nSlots: {}\nUnavailable: {}\nPools: {}\nn_servers: {}'\
            .format(self.rows, self.slots, self.unavailable, self.pools,
                    self.num_servers))