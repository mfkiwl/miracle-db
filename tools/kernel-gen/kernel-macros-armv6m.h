
#define LOAD_UBYTE_RI(RD,RB,IMM)  ldr  RD,RN,IMM 
#define LOAD_UHALF_RI(RD,RB,IMM)  ldrh RD,RN,IMM
#define LOAD_WORD_RI(RD,RB,IMM)   ldrb RD,RN,IMM
#define STORE_BYTE_RI(RS,RB,IMM)  str  RD,RN,IMM 
#define STORE_HALF_RI(RS,RB,IMM)  strh RD,RN,IMM
#define STORE_WORD_RI(RS,RB,IMM)  strb RD,RN,IMM
#define XOR_RR(RD,RA,RB)          eors RD,RD,RM 
#define XOR_RI(RD,RA,IMM)         .error "No xor reg imm on ARMv6M"
#define ADD_RR(RD,RA,IMM)         add  RD,RN,RM  
#define ADD_RI(RD,RA,IMM)         adds RD,RD,IM 
#define SHIFT_LEFT_RI(RD,RA,IMM)  lsls RD,RD,RS 
#define SHIFT_RIGHT_RI(RD,RA,IMM) lsrs RD,RD,RS 
#define ANOP                      nop
#define MNOP                      nop           
#define MULTIPLY_RR (RD,RA,RB)    muls RD,RM,RD 

#define FUNC_ENTER                push {r4, lr}
#define FUNC_RETURN               pop  {r4, pc}