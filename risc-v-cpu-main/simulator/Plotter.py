import sys

from matplotlib import pyplot as plt

def plotIMemAccesses(cpu_states):
    cycles = list()
    i_mem_access = list()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][0]:
            cycles.append(i)
            addr = (cpu_states['pipelined'][i][0] - 1) * 4
            i_mem_access.append(addr)

    fig, ax = plt.subplots()

    ax.scatter(cycles, i_mem_access, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Instruction Address")
    plt.title("Instruction Memory Access Pattern")
    plt.xticks(cycles)
    plt.yticks(i_mem_access)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("imem.jpg", dpi=1000)

def plotDMemAccesses(cpu_states):
    cycles = list()
    d_mem_access = list()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][3] and cpu_states['pipelined'][i][3] in cpu_states['mem_instructions']:
            cycles.append(str(i))
            addr = cpu_states['mem_accesses'][i - 1]
            d_mem_access.append(str(addr))

    fig, ax = plt.subplots()
    ax.scatter(cycles, d_mem_access, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Data Address")
    plt.title("Data Memory Access Pattern")
    plt.xticks(cycles)
    plt.yticks(d_mem_access)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("dmem.jpg", dpi=1000)


def plotStalls(cpu_states):
    cycles = list()
    stage = list()
    stages = ["Fetch", "Decode", "Execute", "Memory", "Writeback", "No stall"]
    
    fig, ax = plt.subplots()

    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['stalled'][i][0]:
            cycles.append(i)
            stage.append(0)
        if cpu_states['stalled'][i][1]:
            cycles.append(i)
            stage.append(1)
        if cpu_states['stalled'][i][2]:
            cycles.append(i)
            stage.append(2)
        if cpu_states['stalled'][i][3]:
            cycles.append(i)
            stage.append(3)
        if cpu_states['stalled'][i][4]:
            cycles.append(i)
            stage.append(4)
        if not(cpu_states['stalled'][i][0] or cpu_states['stalled'][i][1] or cpu_states['stalled'][i][2] or cpu_states['stalled'][i][3] or cpu_states['stalled'][i][4]):
            cycles.append(i)
            stage.append(5)    
    
    ax.scatter(cycles, stage, marker='o')
    plt.xlabel("Cycles")
    plt.ylabel("Stage")
    plt.title("Stalls vs Cycles")
    plt.xticks(cycles)
    plt.yticks([0,1,2,3,4,5], stages)
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("stalls.jpg", dpi=1000)

def plotInstructionTypes(cpu_states, no_of_instructions):

    no_mem = len(cpu_states['mem_instructions'])
    no_reg = cpu_states['no_of_instructions'] - no_mem
    mem = list()
    reg = list()
    cycles = list()

    for i in range(len(cpu_states['reg_values'])): 
        cycles.append(i)
        n_mem = 0
        n_reg = 0
        for k in range(len(cpu_states['pipelined'][i])):
            if cpu_states['pipelined'][i][k]:
                if cpu_states['pipelined'][i][k] in cpu_states['mem_instructions']:
                    n_mem += 1
                else:
                    n_reg += 1
        mem.append(n_mem)
        reg.append(n_reg)

    fig, ax = plt.subplots()
    ax.scatter(cycles, mem, label="Memory Instructions")
    ax.scatter(cycles, reg, label="Register Instructions")
    plt.xlabel("Cycles")
    plt.legend()
    plt.ylabel("No of Instructions")
    plt.title("Plot for number of instructions of each type")
    plt.xticks(cycles)
    plt.yticks([0,1,2,3,4,5])
    plt.gcf().set_size_inches(20, 7)
    plt.tight_layout()
    plt.savefig("types.jpg", dpi=1000)
    
    sys.path.append("../")
    log_file = open("log.txt", "a")
    line = "\n\nNo of memory instructions executed: {}\nNo of register instructions executed: {}".format(no_mem, int(no_reg))
    print(line)
    log_file.write(line)
    log_file.close()
    