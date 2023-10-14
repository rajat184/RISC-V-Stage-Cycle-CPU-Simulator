class Buffer:
    def __init__(self):
        self.empty          = True
        self.instruction_no = None
        self.pc             = None
    
    def clear(self):
        self.empty          = True

class FD_Buffer(Buffer):
    def __init__(self):
        super().__init__()
        self.instruction    = str()

class DX_Buffer(Buffer):
    def __init__(self):
        super().__init__()
        self.opcode         = str()
        self.rs1_val        = None
        self.rs2_val        = None
        self.funct7         = str()
        self.funct3         = str()
        self.rd             = str()
        self.immediate      = int()
        self.store_offset   = int()
        self.beq_offset     = int()

class XM_Buffer(Buffer):
    def __init__(self):
        super().__init__()
        self.opcode         = None
        self.prev_output    = None
        self.rd             = None
        self.rs2_val        = None
        self.forwarding_reg  = None
        self.forwarding_data = None

class MW_Buffer(XM_Buffer):
    def __init__(self):
        super().__init__()
