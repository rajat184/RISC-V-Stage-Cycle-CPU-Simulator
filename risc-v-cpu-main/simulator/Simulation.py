from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from CPU import CPU

INSTRUCTION_SIZE = 32

def begin(binary: str, i_mem_delay: int, d_mem_delay):
    global i_mem, d_mem, cpu, noi

    no_of_instructions = len(binary) // INSTRUCTION_SIZE
    ceil_pc = no_of_instructions * 4

    i_mem   = InstructionMemory(binary, i_mem_delay)
    d_mem   = DataMemory(d_mem_delay)
    cpu     = CPU(ceil_pc)

    noi = cpu.run(no_of_instructions, i_mem, d_mem)

def getPerCycleCPUState():
    cpu_states = {
        'reg_values' : cpu.reg_file_states,
        'stalled'    : cpu.stalls,
        'pipelined'  : cpu.pipelined_instructions,
        'mem_instructions': cpu.ctrl_unit.pipe.mem_instructions,
        'mem_accesses' : cpu.ctrl_unit.pipe.d_mem_accesses,
        'no_of_instructions': noi
    }
    return cpu_states

def getFinalDMemState():
    return d_mem.data


