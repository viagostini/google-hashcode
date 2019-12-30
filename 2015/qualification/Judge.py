

def validate(output):
    pass

def get_score(dc, filename):
    pools = []
    sums = []
    for i in range(dc.pools):
        sums.append(0)
        pools.append([])
    for server in dc.servers:
        if server.pool != -1:
            pools[server.pool].append(server.capacity)
            sums[server.pool] += server.capacity

    dc_min = 1000000009
    for i, pool in enumerate(pools):
        pool_min = 1000000009
        for cap in pool:
            pool_min = min(pool_min, sums[i]-cap)
        dc_min = min(dc_min, pool_min)
        
    print(dc_min)
    
    # servers = []
    # pools = []
    # with open(filename) as output:
    #     for i in range(dc.num_servers):
    #         servers.append([int(num) for num in output.readline().split() if num != 'x'])
    #     for i, server in enumerate(servers):
    #         pools[i].append(server)
            
    #     print(servers)