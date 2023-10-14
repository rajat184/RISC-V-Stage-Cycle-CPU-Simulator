import sys

import Commons

sys.path.append("../")
log_file = open("log.txt", "w")

def generateLog(d_mem_state, cpu_states):
    stages = ["Fetch", "Decode", "Execute", "Memory", "Writeback"]
    for i in range(len(cpu_states['reg_values'])):
        
        head = "At the end of cycle {}\n\n".format(i)
        log_file.write(head)

        for j in range(len(cpu_states['reg_values'][i]) - 1):
            
            line = "r{}: {}\n".format(j, cpu_states['reg_values'][i][j])
            log_file.write(line)

        line = "pc: {}\n".format(cpu_states['reg_values'][i][32])
        log_file.write(line)

        log_file.write("\n")
        for k in range(len(stages)):

            line = "Stage: {}\nInstruction in stage: {}\n Stalled: {}\n\n".format(stages[k],cpu_states['pipelined'][i][k],cpu_states['stalled'][i][k])
            log_file.write(line)

        log_file.write("\n")
    
    addr = list()
    log_file.write("Final Data Memory State\n\n")
    for i in range(len(cpu_states['reg_values'])): 
        if cpu_states['pipelined'][i][3] and cpu_states['pipelined'][i][3] in cpu_states['mem_instructions']:
            if cpu_states['mem_accesses'][i - 1] not in addr:
                addr.append(cpu_states['mem_accesses'][i - 1])
    
    for i in range(len(addr)):
        data = "".join(d_mem_state[addr[i]:addr[i] + 4])
        line = "Address: {}\nData: {} = {}\n\n".format(str(addr[i]), data, Commons.signExtend(data))
        log_file.write(line)

    log_file.write("No other addresses were modified -> They all store 0")
    log_file.close()