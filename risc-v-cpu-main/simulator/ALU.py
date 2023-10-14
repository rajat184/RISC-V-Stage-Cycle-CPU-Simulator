CEIL = (2 ** 31)
MAX = (2 ** 31) - 1
MIN = -(2 ** 31)




class ALU:
    def __init__(self) -> None:
        self.in_1           = None
        self.in_2           = None
        self.pc             = None
        self.beq_offset     = None
        self.store_offset   = None
        self.immediate      = None
        self.opcode         = None
        self.funct          = None


    def resolveOverflow(self, val: int) -> int:
        '''Returns the mod CEIL value if the computed value is out of range'''

        if (val > MAX or val < MIN):
            return val % CEIL
        
        return val


    def ADD(self) -> int:
        '''Returns the sum of input values (sum % CEIL in case of overflow)'''
        
        sum = self.in_1 + self.in_2
        sum = self.resolveOverflow(sum)
        return sum

    
    def BEQ(self) -> int:
        if self.in_1 == self.in_2:
            sum = self.pc + self.beq_offset
            sum = self.resolveOverflow(sum)
            return sum
        return None

    def SW(self) -> int:
        sum = self.in_1 + self.store_offset
        sum = self.resolveOverflow(sum)
        return sum
    
    def ADDI(self) -> int:
        sum = self.in_1 + self.immediate
        sum = self.resolveOverflow(sum)
        return sum
    
    def SUB(self) -> int:
        '''Returns the difference of input values (diff % CEIL in case of overflow)'''
        
        diff = self.in_2 - self.in_1 
        diff = self.resolveOverflow(diff)
        return diff


    def OR(self) -> int:
        '''Returns the bitwise OR of input values'''

        return self.in_1 | self.in_2 


    def AND(self) -> int:
        '''Returns the bitwise AND of input values'''

        return self.in_1 & self.in_2 


    def SLL(self) -> int:
        '''
        Returns the result of applying logical left shift to in_1, (in_2 % 32) number of times (result % CEIL in case of overflow)
        in_2 % 32 corresponds to the value given by least 5 bits of in_2
        '''

        shift = self.in_2 % 32
        res = self.in_1 << shift
        res = self.resolveOverflow(res)
        return res


    def SRA(self) -> int:
        '''
        Returns the result of applying arithmetic right shift to in_1, in_2 % 32 number of times
        in_2 % 32 corresponds to the value given by least 5 bits of in_2
        '''

        shift = self.in_2 % 32
        res = self.in_1 >> shift
        return self.in_1 >> shift


    def execute(self) -> int:
        '''Maps opcode + funct bits to the function of the operation they represent'''
        op_id = self.opcode + self.funct
        op_id_dict     = {
            '01100110100000000' : self.SUB,
            '01100110000000001' : self.SLL,
            '01100110000000000' : self.ADD,
            '01100110100000101' : self.SRA,
            '01100110000000110' : self.OR,
            '01100110000000111' : self.AND,
            '0010011000'        : self.ADDI,
            '0100011010'        : self.SW,
            '0101010101'        : self.SW,
            '0000011010'        : self.ADDI,
            '1100011000'        : self.BEQ
        }

        return op_id_dict[op_id]()
    

