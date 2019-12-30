from Server import Server

class DataCenter:
    def __init__(self, input):
        params = [int(num) for num in input.readline().split()]
        self.rows = params[0]
        self.slots = params[1]
        self.unavailable = params[2]
        self.pools = params[3]
        self.num_servers = params[4]
        self.grid = []
        self.free = []
        self.servers = []
        self.build_grid(input)
        self.create_servers(input)

    def build_grid(self, input):
        for row in range(self.rows):
            self.grid.append(['.'] * self.slots)
            self.free.append([])
        self.mark_unavailable(self.unavailable, input)
        # find free blocks
        for j, row in enumerate(self.grid):
            i = 0
            blocks = ''.join(row).split('x')
            for block in blocks:
                if len(block) > 0:
                    self.free[j].append([i, len(block)])
                i += len(block) + 1

    def mark_unavailable(self, n, input):
        for i in range(n):
            line = input.readline()
            row, slot = [int(num) for num in line.split()]
            self.grid[row][slot] = 'x'

    def create_servers(self, input):
        for i in range(self.num_servers):
            line = input.readline()
            size, capacity = [int(num) for num in line.split()]
            self.servers.append(Server(i, size, capacity))
        self.servers.sort(key=lambda server: server.ratio, reverse=True)

    def find_free_block(self, server, row):
        for i, block in enumerate(self.free[row]):
            #print(row, block)
            if block[1] >= server.size:
                return [i, block]
        return -1

    def put_server(self, server, row, block_idx, block, pool):
        #print(row)
        server.row = row
        #print(self.free)
        server.slot = block[0]
        server.pool = pool
        if block[1] > server.size:
            self.free[row].append([block[0]+server.size, block[1]-server.size])
        del self.free[row][block_idx]
        for i in range(server.size):
            self.grid[row][block[0]+i] = str(server.id)
        #print(self.free)

    def assign_servers(self):
        row, pool = 0, 0
        for server in self.servers:
            #print(self.free)
            for i in range(self.rows):
                curr_row = (row + i) % self.rows
                block = self.find_free_block(server, curr_row)
                if block != -1:               
                    self.put_server(server, curr_row, block[0], block[1], pool)
                    pool = (pool + 1) % self.pools
                    break
            row = (row + 1) % self.rows
                
    def print_output(self, output):
        for server in sorted(self.servers, key=lambda server: server.id):
            if server.row != -1:
                string = f'{server.row} {server.slot} {server.pool}\n'
                output.write(string)
            else:
                output.write('x\n')

    def __str__(self):
        """ Draw datacenter grid """
        return '\n'.join(['[ %s ]' % ''.join(row) for row in self.grid])

    def info(self):
        """ Display info about datacenter specs """
        print('Rows: {}\nSlots: {}\nUnavailable: {}\nPools: {}\nn_servers: {}'\
            .format(self.rows, self.slots, self.unavailable, self.pools,
                    self.num_servers))