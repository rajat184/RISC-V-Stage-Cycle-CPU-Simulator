from assembler_final import Assembler
from simulator import Simulator

class CPU:
    def __init__(self):
        self.assembler = Assembler()
        self.simulator = Simulator()

    def read_file(self, filename):
        with open(filename, 'r') as f:
            instructions = f.readlines()
        return instructions

    def encode(self, instructions):
        encoded_instructions = []
        for instruction in instructions:
            encoded_instruction = self.assembler.encode_instruction(instruction)
            print(instruction + ' -> ' + encoded_instruction)
            encoded_instructions.append(encoded_instruction)
        return encoded_instructions

    def execute(self, encoded_instructions):
        for encoded_instruction in encoded_instructions:
            self.simulator.execute(encoded_instruction)

if __name__ == '__main__':
    cpu = CPU()
    instructions = cpu.read_file('ca-final/test_file.txt')
    encoded_instructions = cpu.encode(instructions)
    print(encoded_instructions)
    cpu.execute(encoded_instructions)
