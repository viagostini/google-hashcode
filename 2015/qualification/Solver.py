from DataCenter import DataCenter

def read_input(filename):
    with open(filename, 'r') as input:
        dc = DataCenter(*[int(num) for num in input.readline().split()])
        dc.mark_unavailable(input)
        dc.create_servers(input)
        print(str(dc) + '\n')
        for server in dc.servers:
            print(str(server))