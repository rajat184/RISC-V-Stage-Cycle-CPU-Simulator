from RegisterFile import RegisterFile
from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from Register import Register
from ALU import ALU

import Buffer
import Commons

class Pipeline:
    def __init__(self, ceil_pc):
        self.FD_Buffer      = Buffer.FD_Buffer()
        self.DX_Buffer      = Buffer.DX_Buffer()
        self.XM_Buffer      = Buffer.XM_Buffer()
        self.MW_Buffer      = Buffer.MW_Buffer()
        self.i_mem_response = None
        self.d_mem_response = None
        self.branch         = None
        self.ceil_pc        = ceil_pc
        self.in_pipe        = [None, None, None, None, None]
        self.stalled        = [False, False, False, False, False]
        self.mem_instructions = list()
        self.d_mem_accesses = list()


    def fetch(self, reg_file: RegisterFile, i_mem: InstructionMemory) -> bool:
        
        pc = reg_file.program_counter.value
        if pc >= self.ceil_pc:
            return False
        
        self.in_pipe[0] = (pc // 4) + 1
        
        response = None

        if not self.i_mem_response:
            response = i_mem.readData(pc)

        if not response:
            if not self.i_mem_response:
                self.stalled[0] = True
                print("F")
                return False

        self.imem_response = response

        if not self.FD_Buffer.empty:
            self.stalled[0] = True
            print("F")
            return False
        
        self.FD_Buffer.pc             = pc
        self.FD_Buffer.instruction    = response
        self.FD_Buffer.instruction_no = self.in_pipe[0]
        self.FD_Buffer.empty          = False
        self.i_mem_response           = None
        print("F")
        return True


    def decode(self, reg_file: RegisterFile):

        if self.FD_Buffer.empty:
            return False

        self.in_pipe[1] = self.FD_Buffer.instruction_no
        
        if not self.DX_Buffer.empty:
            self.stalled[1] = True
            print("D")
            return False

        self.DX_Buffer.instruction_no = self.FD_Buffer.instruction_no
        self.DX_Buffer.pc             = self.FD_Buffer.pc

        self.DX_Buffer.opcode         = self.FD_Buffer.instruction[-7:]

        def decodeSrcReg(reg: Register):
            if reg_file.getReg(reg).awaits_write:
                if reg == self.XM_Buffer.forwarding_reg:
                    return self.XM_Buffer.forwarding_data
                elif reg == self.MW_Buffer.forwarding_reg:
                    return self.MW_Buffer.forwarding_data
                else:
                    return None
            
            return reg_file.getReg(reg).value

        if self.DX_Buffer.opcode in ["0000011", "0100011", "0101010", "1010101"]:
            self.mem_instructions.append(self.DX_Buffer.instruction_no)

        if self.DX_Buffer.opcode in ["0110011", "1100011", "0100011", "0101010"]:
            rs2                         = self.FD_Buffer.instruction[-25:-20]
            rs1                         = self.FD_Buffer.instruction[-20:-15]
            self.DX_Buffer.rs1_val      = decodeSrcReg(rs1)
            self.DX_Buffer.rs2_val      = decodeSrcReg(rs2)
            self.DX_Buffer.rd           = self.FD_Buffer.instruction[-12:-7]
            self.DX_Buffer.funct7       = self.FD_Buffer.instruction[-32:-25]
            self.DX_Buffer.funct3       = self.FD_Buffer.instruction[-15:-12]
            self.DX_Buffer.beq_offset   = Commons.signExtend(self.FD_Buffer.instruction[-32] + 
                                           self.FD_Buffer.instruction[-8] + 
                                           self.FD_Buffer.instruction[-31:-25] + 
                                           self.FD_Buffer.instruction[-12:-8], 12)
            self.DX_Buffer.store_offset = Commons.signExtend(self.FD_Buffer.instruction[-32:-25] + 
                                           self.FD_Buffer.instruction[-12:-7], 12)

            print("D")
            if (type(self.DX_Buffer.rs1_val) is int) and (type(self.DX_Buffer.rs2_val) is int):
                if (self.DX_Buffer.opcode in ["0100011", "1100011", "0101010"]):
                    self.DX_Buffer.rd     = None
                    self.DX_Buffer.funct7 = ""
                    self.DX_Buffer.empty  = False
                    return True
                
                reg_file.getReg(self.DX_Buffer.rd).using.append(self.DX_Buffer.instruction_no)
                self.DX_Buffer.empty            = False
                return True
            else:
                self.stalled[1] = True
                return False

        if self.DX_Buffer.opcode in ["0010011", "0000011"]: 
            rs1                         = self.FD_Buffer.instruction[-20:-15]
            self.DX_Buffer.rs1_val      = decodeSrcReg(rs1)
            self.DX_Buffer.rd           = self.FD_Buffer.instruction[-12:-7]
            self.DX_Buffer.funct3       = self.FD_Buffer.instruction[-15:-12]
            self.DX_Buffer.funct7       = ""
            self.DX_Buffer.immediate    = Commons.signExtend(self.FD_Buffer.instruction[-32:-20], 12)

            print("D")
            if (type(self.DX_Buffer.rs1_val) is int):
                reg_file.getReg(self.DX_Buffer.rd).using.append(self.DX_Buffer.instruction_no)
                self.DX_Buffer.empty            = False
                return True
            else:
                self.stalled[1] = True
                return False
        
        self.DX_Buffer.empty = False
        print("D")
        return True


    def execute(self, alu: ALU, reg_file: RegisterFile):

        if self.DX_Buffer.empty:
            return False

        self.in_pipe[2] = self.DX_Buffer.instruction_no

        if not self.XM_Buffer.empty:
            print("X")
            self.stalled[2] = True
            return False
        
        self.XM_Buffer.empty          = False
        self.XM_Buffer.instruction_no = self.DX_Buffer.instruction_no
        self.XM_Buffer.pc             = self.DX_Buffer.pc

        self.XM_Buffer.opcode         = self.DX_Buffer.opcode

        if self.XM_Buffer.opcode == "1010101":
            print ("X")
            return True

        alu.in_1         = self.DX_Buffer.rs1_val
        alu.in_2         = self.DX_Buffer.rs2_val
        alu.pc           = self.DX_Buffer.pc
        alu.beq_offset   = self.DX_Buffer.beq_offset
        alu.store_offset = self.DX_Buffer.store_offset
        alu.immediate    = self.DX_Buffer.immediate
        alu.opcode       = self.DX_Buffer.opcode
        alu.funct        = self.DX_Buffer.funct7 + self.DX_Buffer.funct3
        
        self.XM_Buffer.prev_output = alu.execute()
        
        if alu.opcode == "1100011" and self.XM_Buffer.prev_output:
            print("X")
            return [self.DX_Buffer.pc, self.XM_Buffer.prev_output]

        self.XM_Buffer.rd               = self.DX_Buffer.rd

        if alu.opcode == "0110011" or alu.opcode == "0010011":
            self.XM_Buffer.forwarding_data = self.XM_Buffer.prev_output
            self.XM_Buffer.forwarding_reg  = self.XM_Buffer.rd

        if alu.opcode == "0100011" or alu.opcode == "0101010":
            self.XM_Buffer.rs2_val  = self.DX_Buffer.rs2_val

        print("X")
        return True


    def memory(self, d_mem: DataMemory):
        
        self.d_mem_accesses.append(self.XM_Buffer.prev_output)

        if self.XM_Buffer.empty:
            return False
        
        self.in_pipe[3] = self.XM_Buffer.instruction_no

        if self.XM_Buffer.opcode == "1010101":
            self.d_mem_accesses.pop()
            self.d_mem_accesses.append(16400)
            write_complete = None

            if not self.d_mem_response:
                write_complete = d_mem.writeData(16400, 1)
            
            if not write_complete:
                if not self.d_mem_response:
                    print("M")
                    self.stalled[3] = True
                    return False

            self.d_mem_response = write_complete
        
        if self.XM_Buffer.opcode == "0100011" or self.XM_Buffer.opcode == "0101010":
            write_complete = None

            if not self.d_mem_response:
                write_complete = d_mem.writeData(self.XM_Buffer.prev_output, self.XM_Buffer.rs2_val)
            
            if not write_complete:
                if not self.d_mem_response:
                    print("M")
                    self.stalled[3] = True
                    return False

            self.d_mem_response = write_complete
        
        if self.XM_Buffer.opcode == "0000011":
            read_response = None

            if not self.d_mem_response:
                read_response = d_mem.readData(self.XM_Buffer.prev_output)
            
            if not read_response:
                if not self.d_mem_response:
                    print("M")
                    self.stalled[3] = True
                    return False

            self.d_mem_response = read_response
        
        if not self.MW_Buffer.empty:
            print("M")
            self.stalled[3] = True
            return False

        self.MW_Buffer.empty            = False
        self.MW_Buffer.instruction_no   = self.XM_Buffer.instruction_no
        self.in_pipe[3]                 = self.MW_Buffer.instruction_no
        self.MW_Buffer.pc               = self.XM_Buffer.pc
        
        self.MW_Buffer.opcode           = self.XM_Buffer.opcode
        self.MW_Buffer.rd               = self.XM_Buffer.rd

        if self.XM_Buffer.opcode == "0110011" or self.XM_Buffer.opcode == "0010011":
            self.MW_Buffer.forwarding_data = self.XM_Buffer.forwarding_data
            self.MW_Buffer.forwarding_reg  = self.XM_Buffer.forwarding_reg
            self.MW_Buffer.prev_output     = self.XM_Buffer.prev_output
        
        if self.XM_Buffer.opcode == "0000011":
            self.MW_Buffer.prev_output     = int(self.d_mem_response, 2)
            self.MW_Buffer.forwarding_data = self.MW_Buffer.prev_output
            self.MW_Buffer.forwarding_reg  = self.MW_Buffer.rd

        self.d_mem_response = None
        print("M")
        return True


    def writeback(self, reg_file: RegisterFile):

        if self.MW_Buffer.empty:
            return False
        
        self.in_pipe[4] = self.MW_Buffer.instruction_no

        if self.MW_Buffer.opcode in ["0110011", "0010011", "0000011"]:
            rd = reg_file.getReg(self.MW_Buffer.rd)
            rd.value = self.MW_Buffer.prev_output
            rd.using.pop(0)
        
        print("W")
        return True