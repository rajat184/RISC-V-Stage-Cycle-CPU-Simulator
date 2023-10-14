register_dict = {
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


U_type = {

    "LUI":"0110111",
    "AUIPC":"0010111"
}

R_type = {
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
I_type = {
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

uj_type = {
    "JAL":"1101111"
}

sb_type = {
    "BEQ":"1100011",
    "BNE":"1100011",
    "BLT":"1100011",
    "BGE":"1100011",
    "BLTU":"1100011",
    "BGEU":"1100011"
}

def getval(d,i):
  return d[i]


def encode_U_type(instruction, rd, imm):
    opcode_binary = getval(U_type, instruction)
    rd_binary = getval(register_dict, rd)
    imm_binary = format(int(imm), '020b')

    machine_code = opcode_binary + imm_binary[:12] + rd_binary + opcode_binary[:2]

    return machine_code

# Example usage:
u_type_machine_code = encode_U_type("LUI", "r1", 100)
print(f"Machine code for LUI r1, 100: {u_type_machine_code}")


def encode_R_type(instruction, rd, rs1, rs2, funct7="0000000"):
    opcode_binary = "0110011"
    funct3_binary = getval(R_type, instruction)
    funct7_binary = funct7
    rd_binary = getval(register_dict, rd)
    rs1_binary = getval(register_dict, rs1)
    rs2_binary = getval(register_dict, rs2)

    machine_code = opcode_binary + funct7_binary + funct3_binary + rs2_binary + rs1_binary + funct3_binary + rd_binary

    return machine_code

# Example usage:
r_type_machine_code = encode_R_type("ADD", "r0", "r1", "r2")
print(f"Machine code for ADD r0, r1, r2: {r_type_machine_code}")


def encode_I_type(instruction, rd, rs1, imm):
    opcode_binary = getval(I_type, instruction)
    rd_binary = getval(register_dict, rd)
    rs1_binary = getval(register_dict, rs1)
    imm_binary = format(int(imm), '012b')

    machine_code = opcode_binary + imm_binary + rs1_binary + opcode_binary[:3] + rd_binary

    return machine_code

# Example usage:
i_type_machine_code = encode_I_type("ADDI", "r3", "r4", 50)
print(f"Machine code for ADDI r3, r4, 50: {i_type_machine_code}")

def encode_UJ_type(instruction, rd, imm):
    opcode_binary = getval(uj_type, instruction)
    rd_binary = getval(register_dict, rd)
    imm_binary = format(int(imm), '020b')

    machine_code = opcode_binary + imm_binary[0] + imm_binary[10:20] + imm_binary[9] + imm_binary[1:9] + rd_binary + opcode_binary[:2]

    return machine_code

# Example usage:
uj_type_machine_code = encode_UJ_type("JAL", "r2", 1000)
print(f"Machine code for JAL r2, 1000: {uj_type_machine_code}")


def encode_SB_type(instruction, rs1, rs2, label):
    opcode_binary = getval(sb_type, instruction)
    funct3_binary = getval(R_type, instruction)
    imm_binary = format(label_dict[label] - (pc + 1), '012b')  # Calculate the relative offset
    imm_binary = imm_binary[0] + imm_binary[2:8] + imm_binary[11] + imm_binary[1] + imm_binary[3:11]
    rs1_binary = getval(register_dict, rs1)
    rs2_binary = getval(register_dict, rs2)

    machine_code = opcode_binary + imm_binary[0] + imm_binary[10] + imm_binary[1:5] + funct3_binary + imm_binary[5:10] + rs2_binary + rs1_binary + imm_binary[10] + imm_binary[11]

    return machine_code

# Example usage:
sb_type_machine_code = encode_SB_type("BEQ", "r1", "r2", "label1")
print(f"Machine code for BEQ r1, r2, label1: {sb_type_machine_code}")
