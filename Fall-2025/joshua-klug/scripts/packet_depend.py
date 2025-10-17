from itertools import combinations
from collections import Counter

# Packet size
PACKET_SIZE = 4

# Output file name
OUTPUT_FILE = "valid_vliw_packets.txt"

INSTRUCTION_FU = {
    #Scalar
    "add.s": "SCALAR",
    "sub.s": "SCALAR",
    "mul.s": "SCALAR",
    "div.s": "SCALAR",
    "mod.s": "SCALAR",
    "or.s": "SCALAR",
    "xor.s": "SCALAR",
    "sll.s": "SCALAR",
    "srl.s": "SCALAR",
    "sra.s": "SCALAR",
    "slt.s": "SCALAR",
    "sltu.s": "SCALAR",
    "addi.s": "SCALAR",
    "subi.s": "SCALAR",
    "muli.s": "SCALAR",
    "divi.s": "SCALAR",
    "modi.s": "SCALAR",
    "ori.s": "SCALAR",
    "andi.s": "SCALAR",
    "xori.s": "SCALAR",
    "slli.s": "SCALAR",
    "srli.s": "SCALAR",
    "srai.s": "SCALAR",
    "slti.s": "SCALAR",
    "sltui.s": "SCALAR",
    "li.s": "SCALAR", #not sure abt this one
    #Branch/Jump
    "beq.s": "BR/J",
    "bne.s": "BR/J",
    "blt.s": "BR/J",
    "bge.s": "BR/J",
    "bgt.s": "BR/J",
    "ble.s": "BR/J",
    "jal": "BR/J",
    "jalr": "BR/J",
    #Load Scalar
    "lw.s": "LOAD.S", #seems like it may cause issues with these being seperate due to L/S advancment
    #Store Scalar
    "sw.s": "STORE.S",
    #Vector
    "add.vv": "VECTOR",
    "sub.vv": "VECTOR",
    "mul.vv": "VECTOR",
    "div.vv": "VECTOR",
    "and.vv": "VECTOR",
    "or.vv": "VECTOR",
    "xor.vv": "VECTOR",
    "addi.vi": "VECTOR",
    "subi.vi": "VECTOR",
    "muli.vi": "VECTOR",
    "divi.vi": "VECTOR",
    "expi.vi": "VECTOR",
    "sqrti.vi": "VECTOR",
    "not.vi": "VECTOR",
    "shift.vi": "VECTOR",
    "shift.vs": "VECTOR", #this may be a pain in the ass
    #Vector Load
    "vreg.ld": "LOAD.V", #seems like it may cause issues with these being seperate due to L/S advancment
    #Vector Store
    "vreg.st": "STORE.V",
    #GEMM
    "gemm.vv": "GEMM",
    "lw.vi": "GEMM", #not sure abt this one
    #SCPAD Load
    "scpad.ld": "LOAD.SCPAD", #might cause problems being seperate but not sure, need to consult scpad team
    #SCPAD Store
    "scpad.st": "STORE.SCPAD",

    #these things
    "nop.s": "NOP",
    #"halt.s": "HALT",
    #"fence.s": "FENCE",

}


FU_LIMITS = {
    "SCALAR": 1,
    "VECTOR": 1,
    "LOAD.S": 1,
    "STORE.S": 1,
    "BR/J": 1,
    "LOAD.V": 1,
    "STORE.V": 1,
    "GEMM": 1,
    "LOAD.SCPAD": 1,
    "STORE.SCPAD": 1,
    "NOP": PACKET_SIZE  # NOPs can go anywhere
}


INCOMPATIBLE = {
    #Scalar
    "add.s": {},
    "sub.s": {},
    "mul.s": {},
    "div.s": {},
    "mod.s": {},
    "or.s": {},
    "xor.s": {},
    "sll.s": {},
    "srl.s": {},
    "sra.s": {},
    "slt.s": {},
    "sltu.s": {},
    "addi.s": {},
    "subi.s": {},
    "muli.s": {},
    "divi.s": {},
    "modi.s": {},
    "ori.s": {},
    "andi.s": {},
    "xori.s": {},
    "slli.s": {},
    "srli.s": {},
    "srai.s": {},
    "slti.s": {},
    "sltui.s": {},
    "li.s": {}, #not sure abt this one
    #Branch/Jump
    "beq.s": {},
    "bne.s": {},
    "blt.s": {},
    "bge.s": {},
    "bgt.s": {},
    "ble.s": {},
    "jal": {},
    "jalr": {},
    #Load Scalar
    "lw.s": {"sw.s"}, #seems like it may cause issues with these being seperate due to L/S advancment
    #Store Scalar
    "sw.s": {"lw.s"},
    #Vector
    "add.vv": {},
    "sub.vv": {},
    "mul.vv": {},
    "div.vv": {},
    "and.vv": {},
    "or.vv": {},
    "xor.vv": {},
    "addi.vi": {},
    "subi.vi": {},
    "muli.vi": {},
    "divi.vi": {},
    "expi.vi": {},
    "sqrti.vi": {},
    "not.vi": {},
    "shift.vi": {},
    "shift.vs": {}, #this may be a pain in the ass
    #Vector Load
    "vreg.ld": {"vreg.st"}, #seems like it may cause issues with these being seperate due to L/S advancment
    #Vector Store
    "vreg.st": {"vreg.ld"},
    #GEMM
    "gemm.vv": {},
    "lw.vi": {}, #not sure abt this one
    #SCPAD Load
    "scpad.ld": {"scpad.st"}, #might cause problems being seperate but not sure, need to consult scpad team
    #SCPAD Store
    "scpad.st": {"scpad.ld"},

    #these things
    "nop.s": {}
    #"halt.s": "HALT",
    #"fence.s": "FENCE",
}



def violates_fu_limits(packet, inst_fu_map, fu_limits):
    """Return True if packet exceeds any FU issue limit."""
    fu_counts = Counter(inst_fu_map[inst] for inst in packet)
    for fu, count in fu_counts.items():
        if count > fu_limits.get(fu, 0):
            return True
    return False


def is_valid_packet(packet, inst_fu_map, fu_limits, incompat_map):
    """Check if packet respects FU limits and explicit incompatibilities."""
    # Check FU group limits
    if violates_fu_limits(packet, inst_fu_map, fu_limits):
        return False

    # Check explicit instruction incompatibilities
    for i, inst1 in enumerate(packet):
        for inst2 in packet[i + 1:]:
            if (inst2 in incompat_map.get(inst1, set())) or (inst1 in incompat_map.get(inst2, set())):
                return False
    return True


def generate_valid_packets(instructions, inst_fu_map, fu_limits, incompat_map, size):
    """Generate all valid instruction packets."""
    valid_packets = []
    for combo in combinations(instructions, size):
        if is_valid_packet(combo, inst_fu_map, fu_limits, incompat_map):
            valid_packets.append(combo)
    return valid_packets


#main

if __name__ == "__main__":
    instructions = list(INSTRUCTION_FU.keys())
    packets = generate_valid_packets(instructions, INSTRUCTION_FU, FU_LIMITS, INCOMPATIBLE, PACKET_SIZE)
    total_packets = len(packets)

    # Write output to file
    with open(OUTPUT_FILE, "w") as f:
        f.write("VLIW Valid Instruction Packets\n")
        f.write("---------------------------------\n\n")
        for idx, packet in enumerate(packets, start=1):
            f.write(f"{idx:04d}: {packet}\n")
        f.write("\n---------------------------------\n")
        f.write(f"Total valid packets: {total_packets}\n")

    print(f"Generated {total_packets} valid instruction packets.")
    print(f"Results saved to: {OUTPUT_FILE}")