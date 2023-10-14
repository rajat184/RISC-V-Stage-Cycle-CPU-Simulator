

# def beq(i):
#     rs1=register_dict_rev[i[12:17]]
#     rs2=register_dict_rev[i[7:12]]
#     imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
#     imm=int(imm,2)
#     if reg_val[rs1]==reg_val[rs2]:
#         reg_val["R0"]=reg_val["R0"]+imm
#     print("BEQ")
#     print(reg_val)

# imm[12|10:5] rs2 rs1 000 imm[4:1|11] 1100011 BEQ rs1,rs2,imm

# def SB_type(i):
#     opcode = "1100011"
#     rs1 = register_dict[i[1]]
#     rs2 = register_dict[i[2]]
#     funct3 = funct3_dict[i[0]]
#     val=int(i[3])
#     imm = bin(val)[2:].zfill(12) 
#     if(val<0):
#         abs_value = abs(val)
#         imm = bin(abs_value)[2:].zfill(12)
#         inverted_binary = ''.join('1' if bit == '0' else '0' for bit in imm)
        
#         # Add 1 to the inverted binary to get the 2's complement representation.
#         carry = 1
#         result = []
#         for bit in reversed(inverted_binary):
#             if bit == '0':
#                 result.insert(0, str(carry))
#                 carry = 0
#             else:
#                 result.insert(0, '1' if carry == 0 else '0')
        
#         imm = ''.join(result)

#     imm=imm[::-1]
#     ans=imm[11]+ " " + imm[9:3:-1] +" "+rs2+" "+rs1+" "+funct3+" "+imm[3::-1]+" "+imm[10]+" "+opcode
#     return ans