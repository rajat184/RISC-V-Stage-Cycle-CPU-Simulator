def signExtend(binary: str, no_of_bits = 32) -> int:

    unsigned_ceil   = 2 ** no_of_bits
    signed_ceil     = 2 ** (no_of_bits - 1)
    
    unsigned_val    = int(binary, 2)

    if unsigned_val >= signed_ceil:
        signed_val  = unsigned_val - unsigned_ceil
    else:
        signed_val  = unsigned_val

    return signed_val


def twosComplement(signed_val: int, no_of_bits: int) -> str:
    unsigned_ceil   = 2 ** no_of_bits
    
    if signed_val < 0:
        signed_val  += unsigned_ceil
    
    bin_data = bin(signed_val)[2:]
    zero_bits = '0' * (32 - len(bin_data))
    data_str = zero_bits + bin_data
    
    return data_str