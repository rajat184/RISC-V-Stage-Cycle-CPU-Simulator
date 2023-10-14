from RegisterFile import RegisterFile
from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from ALU import ALU
from CtrlUnit import CtrlUnit

class CPU:
    def __init__(self, ceil_pc):
        self.reg_file               = RegisterFile()
        self.ctrl_unit              = CtrlUnit(ceil_pc)
        self.alu                    = ALU()
        self.ceil_pc                = ceil_pc
        self.stalls                 = list()
        self.pipelined_instructions = list()
        self.exceptions             = list()
        self.reg_file_states        = list()


    def run(self, no_of_instructions: int, i_mem: InstructionMemory, d_mem: DataMemory):
        
        cycle                 = 0
        instructions_executed = 0

        while (instructions_executed < no_of_instructions):

            self.reg_file_states.append(self.reg_file.getState())
            self.stalls.append(self.ctrl_unit.pipe.stalled)
            self.pipelined_instructions.append(self.ctrl_unit.pipe.in_pipe)
            
            self.ctrl_unit.pipe.stalled = [False, False, False, False, False]
            self.ctrl_unit.pipe.in_pipe = [None, None, None, None, None]

            cycle += 1
            i_mem.decrementResTime()
            d_mem.decrementResTime()
            
            print("\n", cycle)
            state = self.ctrl_unit.pipeline(self.reg_file, self.alu, i_mem, d_mem)
            

            if state['w']:
                instructions_executed += 1

            if type(state['x']) is list:
                
                if (state['x'][1] % 4) != 0:
                    self.exceptions.append("Exception at cycle {}: target address of branch operation will cause a misaligned instruction memory access".format(self.cycles))
                
                else:    
                    self.ctrl_unit.flush(self.reg_file)
                    if state['x'][1] > self.ceil_pc:
                        state['x'][1] = self.ceil_pc

                    diff = (state['x'][0] - state['x'][1]) / 4
                    no_of_instructions += diff + 1
                    
                    self.reg_file.program_counter.value = state['x'][1]
                    continue
            
            if state['f']:
                self.reg_file.program_counter.value += 4
        
        self.reg_file_states.append(self.reg_file.getState())
        self.stalls.append(self.ctrl_unit.pipe.stalled)
        self.pipelined_instructions.append(self.ctrl_unit.pipe.in_pipe)
        print("\n\nExceptions: ")
        print(self.exceptions)
        return no_of_instructions