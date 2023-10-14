from Memory import Memory

BITS_PER_ADDRESS = 8
MEM_SIZE = 1024          # in bytes

class InstructionMemory(Memory):

    def __init__(self, binary: str, delay: int, size: int = MEM_SIZE) -> None:
        super().__init__(size, delay)
        
        byte_address = 0
        for i in range(0, len(binary), BITS_PER_ADDRESS):
            self.data[byte_address] = binary[i:i + BITS_PER_ADDRESS]
            byte_address += 1
        
        print("- instructions loaded in instruction memory")