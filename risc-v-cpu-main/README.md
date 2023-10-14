# Cycle accurate simulator for 5-stage pipelined RISC-V CPU

This project simulates a 5-stage pipelined CPU executing a binary encoded in the RV32I variant of the RISC-V ISA.

Instructions supported:

ISA instructions:

- ADD rd rs1 rs2
- SUB rd rs1 rs2
- AND rd rs1 rs2
- OR rd rs1 rs2
- SLL rd rs1 rs2
- SRA rd rs1 rs2
- LW rd rs1 off
- SW rs2 rs1 off
- BEQ rs2 rs1 off

Additional instructions:

- LOADNOC rs2 rs1 off
- STORENOC

Features:

1. Simulator is able to parse all instructions given as an input binary and simulate their pipelined execution
2. Pipeline with full bypassing
3. Delay cycles for memory accesses can be specified by the user and the pipeline stages will stall accordingly.
4. Logger generates a log file recording
   - per cycle state of the register file
   - instuctions in pipeline in each cycle
   - stalls per clock cycle
   - state of the data memory at the end of the simulation
5. Plotter generates plots for
   - instruction memory access pattern
   - data memory access pattern
   - stalls per cycle
   - number of memory/register instructions

<hr>

## Steps to run:

1. Clone the repository
2. cd into top level directory
3. run `python3 simulator/Main.py`

<hr>

## Please See: Assumptions

As stated in the specifications of the RISC-V ISA,

1. the endianness of memory systems can be either little or big endian - it depends on the execution environment. We assume our data and instruction memory store data in big endian format.

2. an exception must be raised if a branch instruction's target address will result in a misaligned instruction memory access. We assume that this exception simply skips over the instruction that generates it and the simulation continues.

3. it is up to the execution environment whether or not to allow misaligned data memory accesses by load and store operations. We assume that our data memory allows for misaligned memory access.

Further assumptions:

- In case both the writeback and the decode stage try to access the same register of the register file in the same cycle, the writeback stage will complete the write first and toggle the availability of the register it wrote to, making it available for access by the decode stage next in the same cycle.

- in case of BEQ, if the condition is true, the pipeline is ALWAYS flushed
