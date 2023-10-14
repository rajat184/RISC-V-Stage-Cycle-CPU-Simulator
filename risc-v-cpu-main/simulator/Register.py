import Commons

SIZE = 32

class Register:

    def __init__(self) -> None:
        self.binary         = '0' * SIZE
        self.using          = list()
    
    @property
    def awaits_write(self):
        return len(self.using) != 0

    @property
    def value(self):
        return Commons.signExtend(self.binary)

    @value.setter
    def value(self, val: int) -> None:    
        self.binary         = Commons.twosComplement(val, SIZE)