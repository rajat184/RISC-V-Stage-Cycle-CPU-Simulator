import argparse

import Simulation
import Logger
import Plotter


def getCmdLineArgs():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--binary', help="Enter the binary for the program to be executed")
    parser.add_argument('--ddelay', help="Sets the delay cycles for data memory")
    parser.add_argument('--idelay', help="Sets the delay cycles for instruction memory")

    args = parser.parse_args()

    if not args.ddelay:
        args.ddelay = 0
    else:
        args.ddelay = int(args.ddelay)
    
    if not args.idelay:
        args.idelay = 0
    else:
        args.idelay = int(args.idelay)
    
    if not args.binary:
        args.binary = "final_evaluation_test_binary"
    
    return args


def getBinaryString(file_name: str) -> str:
    
    input_file      = open(file_name, "r")
    file_content    = input_file.read()
    content_list    = file_content.split()
    input_binary    = "".join(content_list)

    return input_binary


def main():

    args            = getCmdLineArgs()
    input_binary    = getBinaryString(args.binary)
    
    Simulation.begin(input_binary, args.idelay, args.ddelay)
    
    d_mem_state     = Simulation.getFinalDMemState()

    cpu_states      = Simulation.getPerCycleCPUState()
        
    Logger.generateLog(d_mem_state, cpu_states)
    # Logger.summarizeLog(log)

    # Plotter.plotStalls(cpu_states)
    # Plotter.plotIMemAccesses(cpu_states)
    # Plotter.plotDMemAccesses(cpu_states)
    # Plotter.plotInstructionTypes(cpu_states, len(input_binary) // 32)


main()