class Simulator:
    def __init__(self):
        self.reg_val = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0,
            "R4": 0,
            "R5": 0,
            "R6": 0,
            "R7": 0,
            "R8": 0,
            "R9": 0,
            "R10": 0,
            "R11": 0,
            "R12": 0,
            "R13": 0,
            "R14": 0,
            "R15": 0,
            "R16": 0,
            "R17": 0,
            "R18": 0,
            "R19": 0,
            "R20": 0,
            "R21": 0,
            "R22": 0,
            "R23": 0,
            "R24": 0,
            "R25": 0,
            "R26": 0,
            "R27": 0,
            "R28": 0,
            "R29": 0,
            "R30": 0,
            "R31": 0,
        }
        self.register_dict = {
            "00000": "R0",
            "00001": "R1",
            "00010": "R2",
            "00011": "R3",
            "00100": "R4",
            "00101": "R5",
            "00110": "R6",
            "00111": "R7",
            "01000": "R8",
            "01001": "R9",
            "01010": "R10",
            "01011": "R11",
            "01100": "R12",
            "01101": "R13",
            "01110": "R14",
            "01111": "R15",
            "10000": "R16",
            "10001": "R17",
            "10010": "R18",
            "10011": "R19",
            "10100": "R20",
            "10101": "R21",
            "10110": "R22",
            "10111": "R23",
            "11000": "R24",
            "11001": "R25",
            "11010": "R26",
            "11011": "R27",
            "11100": "R28",
            "11101": "R29",
            "11110": "R30",
            "11111": "R31",
        }

    def print_reg_val(self):
        # print register values in a table
        print("Register Values:")
        for i in range(0, 32, 4):
            print(
                f"{self.register_dict[str(bin(i))[2:].zfill(5)]}: {self.reg_val[self.register_dict[str(bin(i))[2:].zfill(5)]]}\t\t\t{self.register_dict[str(bin(i + 1))[2:].zfill(5)]}: {self.reg_val[self.register_dict[str(bin(i + 1))[2:].zfill(5)]]}\t\t\t{self.register_dict[str(bin(i + 2))[2:].zfill(5)]}: {self.reg_val[self.register_dict[str(bin(i + 2))[2:].zfill(5)]]}\t\t\t{self.register_dict[str(bin(i + 3))[2:].zfill(5)]}: {self.reg_val[self.register_dict[str(bin(i + 3))[2:].zfill(5)]]}"
            )

    def execute(self, instruction):
        instruction = instruction.replace(" ", "")
        opcode = instruction[25:32]
        if opcode == "0110011":
            # R type: add, sub, sll, slt, sltu, xor, srl, sra, or, and
            return self.r_type(instruction)
        elif opcode == "0010011":
            # I type: addi, slti, sltiu, xori, ori, andi, slli, srli, srai
            return self.i_type(instruction)
        elif opcode == "0100011":
            # S type: sb, sh, sw, sd
            return self.s_type(instruction)
        elif opcode == "1100011":
            # SB type: beq, bne, blt, bge, bltu, bgeu
            return self.sb_type(instruction)
        elif opcode == "0110111" or opcode == "0010111":
            # U type: lui, auipc
            return self.u_type(instruction)
        elif opcode == "1101111":
            # UJ type: jal
            return self.uj_type(instruction)
        else:
            print("Invalid instruction")

    def r_type(self, instruction):
        funct7 = instruction[0:7]
        rs2 = self.register_dict[instruction[7:12]]
        rs1 = self.register_dict[instruction[12:17]]
        funct3 = instruction[17:20]
        rd = self.register_dict[instruction[20:25]]
        instr_name = ""

        if funct7 == "0000000":
            if funct3 == "000":
                # add
                instr_name = "add"
                self.reg_val[rd] = self.reg_val[rs1] + self.reg_val[rs2]
            elif funct3 == "001":
                # sll
                instr_name = "sll"
                self.reg_val[rd] = self.reg_val[rs1] << self.reg_val[rs2]
            elif funct3 == "010":
                # slt
                instr_name = "slt"
                self.reg_val[rd] = 1 if self.reg_val[rs1] < self.reg_val[rs2] else 0
            elif funct3 == "011":
                # sltu
                instr_name = "sltu"
                self.reg_val[rd] = 1 if self.reg_val[rs1] < self.reg_val[rs2] else 0
            elif funct3 == "100":
                # xor
                instr_name = "xor"
                self.reg_val[rd] = self.reg_val[rs1] ^ self.reg_val[rs2]
            elif funct3 == "101":
                # srl
                instr_name = "srl"
                self.reg_val[rd] = self.reg_val[rs1] >> self.reg_val[rs2]
            elif funct3 == "110":
                # or
                instr_name = "or"
                self.reg_val[rd] = self.reg_val[rs1] | self.reg_val[rs2]
            elif funct3 == "111":
                # and
                instr_name = "and"
                self.reg_val[rd] = self.reg_val[rs1] & self.reg_val[rs2]
        elif funct7 == "0100000":
            if funct3 == "000":
                # sub
                instr_name = "sub"
                self.reg_val[rd] = self.reg_val[rs1] - self.reg_val[rs2]
            elif funct3 == "101":
                # sra
                instr_name = "sra"
                self.reg_val[rd] = self.reg_val[rs1] >> self.reg_val[rs2]

        print(f"{instr_name} {rd}, {rs1}, {rs2}")
        self.print_reg_val()

    def i_type(self, instruction):
        opcode = instruction[25:32]
        rs1 = self.register_dict[instruction[12:17]]
        rd = self.register_dict[instruction[20:25]]
        funct3 = instruction[17:20]
        imm = int(instruction[0:12], 2)
        instr_name = ""

        if opcode == "0010011":
            if funct3 == "000":
                # addi
                instr_name = "addi"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            # elif funct3 == "001":
            #     # slli
            #     instr_name = "slli"
            #     self.reg_val[rd] = self.reg_val[rs1] << imm
            elif funct3 == "010":
                # slti
                instr_name = "slti"
                self.reg_val[rd] = 1 if self.reg_val[rs1] < imm else 0
            elif funct3 == "011":
                # sltiu
                instr_name = "sltiu"
                self.reg_val[rd] = 1 if self.reg_val[rs1] < imm else 0
            elif funct3 == "100":
                # xori
                instr_name = "xori"
                self.reg_val[rd] = self.reg_val[rs1] ^ imm
            # elif funct3 == "101":
            #     # srli
            #     instr_name = "srli"
            #     self.reg_val[rd] = self.reg_val[rs1] >> imm
            elif funct3 == "110":
                # ori
                instr_name = "ori"
                self.reg_val[rd] = self.reg_val[rs1] | imm
            elif funct3 == "111":
                # andi
                instr_name = "andi"
                self.reg_val[rd] = self.reg_val[rs1] & imm
        elif opcode == "0000011":
            if funct3 == "000":
                # lb
                instr_name = "lb"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            elif funct3 == "001":
                # lh
                instr_name = "lh"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            elif funct3 == "010":
                # lw
                instr_name = "lw"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            # elif funct3 == "011":
            #     # ld
            #     instr_name = "ld"
            #     self.reg_val[rd] = self.reg_val[rs1] + imm
            elif funct3 == "100":
                # lbu
                instr_name = "lbu"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            elif funct3 == "101":
                # lhu
                instr_name = "lhu"
                self.reg_val[rd] = self.reg_val[rs1] + imm
            # elif funct3 == "110":
            #     # lwu
            #     instr_name = "lwu"
            #     self.reg_val[rd] = self.reg_val[rs1] + imm
        elif opcode == "1100111":
            # jalr
            instr_name = "jalr"
            self.reg_val[rd] = self.reg_val[rs1] + imm
        elif opcode == "1110011":
            # scall, sbreak
            if funct3 == "000":
                if imm == 0:
                    # scall
                    instr_name = "scall"
                elif imm == 1:
                    # sbreak
                    instr_name = "sbreak"

        print(f"{instr_name} {rd}, {rs1}, {imm}")
        self.print_reg_val()

    def s_type(self, instruction):
        opcode = instruction[25:32]
        rs1 = self.register_dict[instruction[12:17]]
        rs2 = self.register_dict[instruction[7:12]]
        funct3 = instruction[17:20]
        imm = int(instruction[0:7] + instruction[20:25], 2)
        instr_name = ""

        if opcode == "0100011":
            if funct3 == "000":
                # sb
                instr_name = "sb"
                self.reg_val[rs1] = imm + self.reg_val[rs2]
            elif funct3 == "001":
                # sh
                instr_name = "sh"
                self.reg_val[rs1] = imm + self.reg_val[rs2]
            elif funct3 == "010":
                # sw
                instr_name = "sw"
                self.reg_val[rs1] = imm + self.reg_val[rs2]
            # elif funct3 == "011":
            #     # sd
            #     instr_name = "sd"
            #     self.reg_val[rs1] = imm + self.reg_val[rs2]

        print(f"{instr_name} {rs1}, {imm}({rs2})")
        self.print_reg_val()

    def sb_type(self, instruction):
        opcode = instruction[25:32]
        rs1 = self.register_dict[instruction[12:17]]
        rs2 = self.register_dict[instruction[7:12]]
        funct3 = instruction[17:20]
        imm = int(instruction[0] + instruction[24] +
                  instruction[1:7] + instruction[20:24] + "0", 2)
        instr_name = ""

        if opcode == "1100011":
            if funct3 == "000":
                # beq
                instr_name = "beq"
                if self.reg_val[rs1] == self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm
            elif funct3 == "001":
                # bne
                instr_name = "bne"
                if self.reg_val[rs1] != self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm
            elif funct3 == "100":
                # blt
                instr_name = "blt"
                if self.reg_val[rs1] < self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm
            elif funct3 == "101":
                # bge
                instr_name = "bge"
                if self.reg_val[rs1] >= self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm
            elif funct3 == "110":
                # bltu
                instr_name = "bltu"
                if self.reg_val[rs1] < self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm
            elif funct3 == "111":
                # bgeu
                instr_name = "bgeu"
                if self.reg_val[rs1] >= self.reg_val[rs2]:
                    self.reg_val["R0"] = self.reg_val["R0"] + imm

        print(f"{instr_name} {rs1}, {rs2}, {imm}")
        self.print_reg_val()

    def u_type(self, instruction):
        opcode = instruction[25:32]
        rd = self.register_dict[instruction[20:25]]
        imm = int(instruction[0:20] + "000000000000", 2)
        instr_name = ""

        if opcode == "0110111":
            # lui
            instr_name = "lui"
            self.reg_val[rd] = imm
        elif opcode == "0010111":
            # auipc
            instr_name = "auipc"
            self.reg_val[rd] = imm

        print(f"{instr_name} {rd}, {imm}")
        self.print_reg_val()

    def uj_type(self, instruction):
        opcode = instruction[25:32]
        rd = self.register_dict[instruction[20:25]]
        imm = int(instruction[0] + instruction[12:20] +
                  instruction[11] + instruction[1:11] + "0", 2)
        instr_name = ""

        if opcode == "1101111":
            # jal
            instr_name = "jal"
            self.reg_val[rd] = imm

        print(f"{instr_name} {rd}, {imm}")
        self.print_reg_val()


# sim = Simulator()
# # execute a r type instruction
# sim.execute("0000000 00010 00011 000 00001 0110011")

# # execute a i type instruction - addi
# sim.execute("000000000000 00001 00010 000 0010011")
# # sim.execute("000000000000 00001 00010 000 00001 0010011")

# # execute a s type instruction
# sim.execute("0000000 00010 00001 000 00000 0100011")

# # execute a sb type instruction
# sim.execute("0000000 00001 00010 000 00000 1100011")

# # execute a u type instruction
# sim.execute("00000000000000000000 00001 0110111")

# # execute a uj type instruction
# sim.execute("00000000000000000000 00001 1101111")
