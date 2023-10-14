

#getval --> returns operation's opcode...
#getval(dict_1,ADD) --> returns ("0000") -> opcode of "ADD" operation.


#  instruction: ADD r1, r2, 6
#       l ->     0  1   2   3

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

type_dict = {
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




def getval(d,i):
  return d[i]
def encode_instruction(instruction):
    l = instruction.split()
    # if (getval(type_dict,l[0]) == "0"+"1"*2+"0"*2): #add
    #     if l[0] in dict_1.keys(): #add R-type
    #         return getval(dict_1,l[0]) + "00" +  str(getval(register_dict,l[3])) + str(getval(register_dict,l[2])) + "000" + str(getval(register_dict,l[1])) + "0110011"
    #         #0000000+00+110+00010+000+00001+0110011 = 0000000+00+110+00010+000+00001+0110011
    #     elif l[0] in dict_2.keys(): #l[0] = ADD in dict_2
    #         return "0"*5 + "0"*2 + str(getval(register_dict,l[3])) + str(getval(register_dict,l[2])) + str(getval(dict_2,l[0])) + str(getval(register_dict,l[1]))+ "0"+"1"*2+"0"*2+"1"*2
    #         #000000+00+110+00010+00010+
    #     else:
    #         return "01"+"0"*5+ str(getval(register_dict,l[3]))+ str(getval(register_dict,l[2])) + "101" + str(getval(register_dict,l[1])) + "0"+"1"*2+"0"*2+"1"*2
    #         #01+00000+110+
    # elif (getval(type_dict,l[0]) == "1"*2+"0"*3):  #beq r30, r31, 8
    #     offset = l[3] #8
    #     offset = label_dict[offset]
    #     offset = format(offset,'012b') #1000
    #     return offset[0] + offset[2:8] + getval(register_dict,l[2]) + getval(register_dict,l[1]) + "0"*3 + offset[8:] + offset[1] + "1"*2+"0"*3+"1"*2
    # elif (getval(type_dict,l[0]) == "0"*2+"1"+"0"*2):
    #     imm = l[3]
    #     var=format(int(imm),'012b') #01100
    #     string = str(var) + str(getval(register_dict,l[2])) + "0"*3 + str(getval(register_dict,l[1])) + "0"*2+"1"+"0"*2+"1"*2
    #     return string
    # elif (getval(type_dict,l[0]) == "0"*5):
    #     offset = (l[2]).split("(")[0]
    #     offset = format(int(offset),'012b')
    #     r1 = (l[2]).split("(")[1].replace(")","")
    #     return str(offset) + str(getval(register_dict,r1)) + "010" + str(getval(register_dict,l[1])) + "0"*5+"1"*2
    # elif (getval(type_dict,l[0]) =="01"+"0"*3):
    #     offset = (l[2]).split("(")[0]
    #     offset = format(int(offset),'012b')
    #     r1 = (l[2]).split("(")[1].replace(")","")
    #     return str(offset[:7]) + str(getval(register_dict,l[1])) + str(getval(register_dict,r1)) + "010" + str(offset[7:]) + "01"+"0"*3+"1"*2
    # elif (getval(type_dict,l[0]) == "1"*2+"0"+"1"*2):
    #     return "0"*25 + "1"*2+"0"+"1"*4
    # elif (getval(type_dict,l[0]) == "1"*2+"0"*2+"1"):
    #     offset = l[3]
    #     offset = format(int(offset),'012b')
    #     return str(offset) + str(getval(register_dict,l[2])) + "0"*3 + str(getval(register_dict,l[1])) + "1"*2+"0"*2+"1"*3
    #added by vikrant
    if l[0] == "SLLI":
        shamt_binary = format(int(l[3]), '05b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLLI"]
        funct3 = "001"
        return "0000000"+str(shamt_binary) + rs1_binary + funct3 + rd_binary + opcode
    elif l[0] == "SRLI":
        shamt_binary = format(int(l[3]), '05b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SRLI"]
        funct3 = "101"  # Funct3 for SRLI
        return "0000000"+str(shamt_binary) + rs1_binary + funct3 + rd_binary + opcode
    elif l[0] == "SRAI":
        shamt_binary = format(int(l[3]), '05b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SRAI"]
        funct3 = "101"  # Funct3 for SRAI
        return "0100000"+str(shamt_binary) + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SLL":

        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLL"]
        funct3 = "001"  # Funct3 for SLL
        return "0100000" + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SLT":
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLT"]
        funct3 = "010"  # Funct3 for SLT
        return "0000000"  + rs1_binary + funct3 + rd_binary + opcode
    elif l[0] == "SLTU":
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLTU"]
        funct3 = "011"  # Funct3 for SLTU
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "XOR":
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["XOR"]
        funct3 = "100"  # Funct3 for XOR
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SRL":
        shamt_binary = "00000"  # For SRL, shamt is always zero
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SRL"]
        funct3 = "101"  # Funct3 for SRL
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SRA":
        shamt_binary = "00000"  # For SRA, shamt is always zero
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SRA"]
        funct3 = "101"  # Funct3 for SRA
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "OR":
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["OR"]
        funct3 = "110"  # Funct3 for OR
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "AND":
        rs1_binary = getval(register_dict, l[2])
        rs2_binary = getval(register_dict, l[3])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["AND"]
        funct3 = "111"  # Funct3 for AND
        return "0000000" + rs2_binary + rs1_binary + funct3 + rd_binary + opcode


    # i type
    elif l[0] == "ANDI":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["ANDI"]
        funct3 = "111"  # Funct3 for ANDI
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "ADDI":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["ADDI"]
        funct3 = "000"  # Funct3 for ADDI
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode
    elif l[0] == "SLTI":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLTI"]
        funct3 = "010"  # Funct3 for SLTI
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SLTIU":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["SLTIU"]
        funct3 = "011"  # Funct3 for SLTIU
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "XORI":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["XORI"]
        funct3 = "100"  # Funct3 for XORI
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "ORI":
        imm_binary = format(int(l[3]), '012b')
        rs1_binary = getval(register_dict, l[2])
        rd_binary = getval(register_dict, l[1])
        opcode = type_dict["ORI"]
        funct3 = "110"  # Funct3 for ORI
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "SB":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        opcode = type_dict["SB"]  # Opcode for SB
        funct3 = "000"  # Funct3 for SB
        return imm_binary[11:5] + rs2_binary + rs1_binary + funct3 +  + imm_binary[4:0]  + opcode

    elif l[0] == "SH":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        opcode = type_dict["SH"]  # Opcode for SH
        funct3 = "001"  # Funct3 for SH
        return imm_binary[11:5] + rs2_binary + rs1_binary + funct3 + imm_binary[4:0] + opcode

    elif l[0] == "SW":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        opcode = type_dict["SW"]  # Opcode for SW
        funct3 = "010"  # Funct3 for SW
        return imm_binary[11:5] + rs2_binary + rs1_binary + funct3 + imm_binary[4:0] + opcode

    elif l[0] == "LB":
        imm_binary = format(int(l[2]), '012b')  # Convert immediate to 12-bit binary
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        rd_binary = getval(register_dict, l[3])  # Get the binary representation of rd
        opcode = type_dict["LB"]  # Opcode for LB
        funct3 = "000"  # Funct3 for LB
        return imm_binary[11:0] + rs1_binary + funct3 + rd_binary + opcode
    elif l[0] == "LH":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        rd_binary = getval(register_dict, l[2])  # Get the binary representation of rd
        opcode = type_dict["LH"]  # Opcode for LH
        funct3 = "001"  # Funct3 for LH
        return imm_binary[11:0] + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "LW":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        rd_binary = getval(register_dict, l[2])  # Get the binary representation of rd
        opcode = type_dict["LW"]  # Opcode for LW
        funct3 = "010"  # Funct3 for LW
        return imm_binary[11:0] + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "LBU":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        rd_binary = getval(register_dict, l[2])  # Get the binary representation of rd
        opcode = type_dict["LBU"]  # Opcode for LBU
        funct3 = "100"  # Funct3 for LBU
        return imm_binary[11:0] + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "LHU":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1
        rd_binary = getval(register_dict, l[2])  # Get the binary representation of rd
        opcode = type_dict["LHU"]  # Opcode for LHU
        funct3 = "101"  # Funct3 for LHU
        return imm_binary[11:0] + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "BEQ":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BEQ"]  # Opcode for BEQ
        funct3 = "000"  # Funct3 for BEQ

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode


    elif l[0] == "BNE":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[2:8]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[8:] + imm_binary[1]  # Bits 4 to 1 and bit 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BNE"]  # Opcode for BNE
        funct3 = "001"  # Funct3 for BNE

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BLT":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[2:8]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[8:] + imm_binary[1]  # Bits 4 to 1 and bit 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BLT"]  # Opcode for BLT
        funct3 = "100"  # Funct3 for BLT

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BGE":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[2:8]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[8:] + imm_binary[1]  # Bits 4 to 1 and bit 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BGE"]  # Opcode for BGE
        funct3 = "101"  # Funct3 for BGE

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BLTU":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[2:8]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[8:] + imm_binary[1]  # Bits 4 to 1 and bit 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BLTU"]  # Opcode for BLTU
        funct3 = "110"  # Funct3 for BLTU

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BGEU":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary
        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[2:8]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[8:] + imm_binary[1]  # Bits 4 to 1 and bit 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BGEU"]  # Opcode for BGEU
        funct3 = "111"  # Funct3 for BGEU

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "LUI":
        imm_binary = format(int(l[2]), '032b')  # Convert immediate to 32-bit binary

        rd_binary = getval(register_dict, l[1])  # Get the binary representation of rd

        opcode = type_dict["LUI"]  # Opcode for LUI

        # Combine the fields to form the instruction
        return imm_binary[0:20] + rd_binary + opcode

    elif l[0] == "AUIPC":
        imm_binary = format(int(l[2]), '032b')  # Convert immediate to 32-bit binary

        rd_binary = getval(register_dict, l[1])  # Get the binary representation of rd

        opcode = type_dict["AUIPC"]  # Opcode for AUIPC

        # Combine the fields to form the instruction
        return imm_binary[0:20] + rd_binary + opcode

    elif l[0] == "JAL":
        imm_binary = format(int(l[2]), '032b')  # Convert immediate to 32-bit binary

        imm_20 = imm_binary[0]  # Bit 20 (most significant bit)
        imm_10_1 = imm_binary[1:11]  # Bits 10 to 1
        imm_11 = imm_binary[11]  # Bit 11
        imm_19_12 = imm_binary[12:20]  # Bits 19 to 12

        rd_binary = getval(register_dict, l[1])  # Get the binary representation of rd

        opcode = type_dict["JAL"]  # Opcode for JAL

        # Combine the fields to form the instruction
        return imm_20 + imm_10_1 + imm_11 + imm_19_12 + rd_binary + opcode

    elif l[0] == "JALR":
        imm_binary = format(int(l[3]), '012b')  # Convert immediate to 12-bit binary

        rd_binary = getval(register_dict, l[1])  # Get the binary representation of rd
        rs1_binary = getval(register_dict, l[2])  # Get the binary representation of rs1

        opcode = type_dict["JALR"]  # Opcode for JALR
        funct3 = "000"  # Funct3 for JALR

        # Combine the fields to form the instruction
        return imm_binary + rs1_binary + funct3 + rd_binary + opcode

    elif l[0] == "BNE":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BNE"]  # Opcode for BNE
        funct3 = "001"  # Funct3 for BNE

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode
    elif l[0] == "BLT":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BLT"]  # Opcode for BLT
        funct3 = "100"  # Funct3 for BLT

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BGE":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BGE"]  # Opcode for BGE
        funct3 = "101"  # Funct3 for BGE

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BLTU":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BLTU"]  # Opcode for BLTU
        funct3 = "110"  # Funct3 for BLTU

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode

    elif l[0] == "BGEU":
        imm_binary = format(int(l[3]), '013b')  # Convert immediate to 13-bit binary

        imm_12 = imm_binary[0]  # Bit 12 (most significant bit)
        imm_10_5 = imm_binary[1:7]  # Bits 10 to 5
        imm_4_1_11 = imm_binary[7:]  # Bits 4 to 1 and 11

        rs2_binary = getval(register_dict, l[2])  # Get the binary representation of rs2
        rs1_binary = getval(register_dict, l[1])  # Get the binary representation of rs1

        opcode = type_dict["BGEU"]  # Opcode for BGEU
        funct3 = "111"  # Funct3 for BGEU

        # Combine the fields to form the instruction
        return imm_12 + imm_10_5 + rs2_binary + rs1_binary + funct3 + imm_4_1_11 + opcode































