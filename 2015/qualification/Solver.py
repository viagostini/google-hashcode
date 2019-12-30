from DataCenter import DataCenter
import Judge

def read_input(filename):
    with open(filename, 'r') as input:
        dc = DataCenter(input)
        #dc.mark_unavailable(input)
        #dc.create_servers(input)
        dc.assign_servers()
        #print(str(dc) + '\n')
        #for server in dc.servers:
        #    print(str(server))
        
        with open('out.txt', 'w') as output:
            dc.print_output(output)
            Judge.validate(output)
        
        Judge.get_score(dc, 'out.txt')