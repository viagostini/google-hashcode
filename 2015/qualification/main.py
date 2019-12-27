import sys
import Solver

def main():
    """ Driver for the program """
    
    if len(sys.argv) < 3:
        sys.exit('Usage: %s <input> <output>' % sys.argv[0])
    
    # read input data and create datacenter
    datacenter = Solver.read_input(sys.argv[1])

    # write solution to output



if __name__ == '__main__':
    main()
