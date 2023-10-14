

# def beq(i):
#     rs1=register_dict_rev[i[12:17]]
#     rs2=register_dict_rev[i[7:12]]
#     imm=i[0]+i[24]+i[1:7]+i[20:24]+"0"
#     imm=int(imm,2)
#     if reg_val[rs1]==reg_val[rs2]:
#         reg_val["R0"]=reg_val["R0"]+imm
#     print("BEQ")
#     print(reg_val)