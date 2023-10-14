from Register import Register

NO_OF_REGISTERS = 32

class RegisterFile:

    def __init__(self) -> None:
        self.program_counter = Register()
        self.gen_registers = list()

        i = 0
        while (i != NO_OF_REGISTERS):
            self.gen_registers.append(Register())
            i += 1
    

    def getReg(self, reg: str) -> Register:
        reg_index = int(reg, 2)
        return self.gen_registers[reg_index]


    def getState(self) -> list:
        reg_values = list()

        for reg in self.gen_registers:
            reg_values.append(reg.value)
        
        reg_values.append(self.program_counter.value)
        return reg_values