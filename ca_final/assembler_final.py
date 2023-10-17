

#getval --> returns operation's opcode...
#getval(dict_1,ADD) --> returns ("0000") -> opcode of "ADD" operation.


#  instruction: ADD r1, r2, 6
#       l ->     0  1   2   3
class Assembler:
    def __init__(self):
        self.register_dict = {
    "r0":"00000",
    "r1":"00001",
    "r2":"00010",
    "r3":"00011",
    "r4":"00100",
    "r5":"00101",
    "r6":"00110",
    "r7":"00111",
    "r8":"01000",
    "r9":"01001",
    "r10":"01010",
    "r11":"01011",
    "r12":"01100",
    "r13":"01101",
    "r14":"01110",
    "r15":"01111",
    "r16":"10000",
    "r17":"10001",
    "r18":"10010",
    "r19":"10011",
    "r20":"10100",
    "r21":"10101",
    "r22":"10110",
    "r23":"10111",
    "r24":"11000",
    "r25":"11001",
    "r26":"11010",
    "r27":"11011",
    "r28":"11100",
    "r29":"11101",
    "r30":"11110",
    "r31":"11111"
}

        self.type_dict = {
            "SLLI":"0010011",
            "SRLI":"0010011",
            "SRAI":"0010011",
            "ADD":"0010011",
            "SUB":"0010011",
            "SLL":"0010011",
            "SLT":"0010011",
            "SLTU":"0010011",
            "XOR":"0010011",
            "SRL":"0010011",
            "SRA":"0010011",
            "OR":"0010011",
            "AND":"0010011",
            "JALR":"1100111",
            "LB":"0000011",
            "LH":"0000011",
            "LW":"0000011",
            "LBU":"0000011",
            "LHU":"0000011",
            "ADDI":"0010011",
            "SLTI":"0010011",
            "SLTIU":"0010011",
            "XORI":"0010011",
            "ORI":"0010011",
            "ANDI":"0010011",
            "BEQ":"1100011",
            "BNE":"1100011",
            "BLT":"1100011",
            "BGE":"1100011",
            "BLTU":"1100011",
            "BGEU":"1100011",
            "JAL":"1101111",    
            "LUI":"0110111",
            "AUIPC":"0010111",
            "JALR":"1100111",
            "LB":"0000011",
            "LH":"0000011",
            "LW":"0000011",
            "LBU":"0000011",
            "LHU":"0000011",
            "ADDI":"0010011",
            "SLTI":"0010011",
            "SLTIU":"0010011",
            "XORI":"0010011",
            "ORI":"0010011",
            "ANDI":"0010011"


            

            


        }



        self.type_U = {

            "LUI":"0110111",
            "AUIPC":"0010111"
        }

        self.type_R = {
            "SLLI":"0010011",
            "SRLI":"0010011",
            "SRAI":"0010011",
            "ADD":"0010011",   
            "SUB":"0010011",    
            "SLL":"0010011",
            "SLT":"0010011",
            "SLTU":"0010011",
            "XOR":"0010011",
            "SRL":"0010011",
            "SRA":"0010011",
            "OR":"0010011",
            "AND":"0010011"
            
            

        }
        self.I_type = {
            "JALR":"1100111",

            "LB":"0000011",
            "LH":"0000011",
            "LW":"0000011",
            "LBU":"0000011",
            "LHU":"0000011",


            "ADDI":"0010011",
            "SLTI":"0010011",
            "SLTIU":"0010011",
            "XORI":"0010011",
            "ORI":"0010011",
            "ANDI":"0010011"

            
        }

        self.uj_type = {
            "JAL":"1101111"
        }

        self.sb_type = {
            "BEQ":"1100011",
            "BNE":"1100011",
            "BLT":"1100011",
            "BGE":"1100011",
            "BLTU":"1100011",
            "BGEU":"1100011"
        }