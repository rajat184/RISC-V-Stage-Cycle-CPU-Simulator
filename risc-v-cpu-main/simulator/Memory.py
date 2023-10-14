class Memory:

    def __init__(self, size: int, delay: int) -> None:
        '''
        Initializes the memory to be of a fixed size (in bytes)
        '''
        self.data       = ["00000000",] * size
        self.delay      = delay
        self.res_time   = -1

    def readData(self, address: int) -> str:
        '''
        Function to return the data present at the (address)th index of the memory
        '''
        if (self.res_time == -1):
            self.res_time = self.delay

        if (self.res_time == 0):
            instruction = "".join(self.data[address : address + 4])
            return instruction
        
        return None

    def decrementResTime(self):
        if (self.res_time >= 0):
            self.res_time -= 1