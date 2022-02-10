# ARM_Assembler
This script translates ARM assembly code to machine code.

The script can translate 3 types of ARM instructions 

1- Data processing instructions with the second source register is either a positive immediate decimal offset or a register:

Example 1: Add R0, R1, R2
Example 2: SUB R0, R0, #8
Example 3: ORRSEQ R2, R3, R4

notes: 
* The supported types of the data instructions functions are ('and', 'eor', 'sub', 'rsb', 'add', 'adc', 'sbc', 'rsc', 'tst', 'teq', 'cmp', 'cmn', 'orr', 'mov'])
* The supported conditions are ('eq', 'ne', 'cs', 'hs', 'cc', 'lo', 'ml', 'pl', 'vs', 'vc', 'hl', 'ls', 'ge', 'lt', 'le', 'al')
* If an 's' is added after the function this indicates that the CPSR register will save the condition flags.

2- Memory instructions in offset mode with postive immediate dcimal offset:

Example 1: STR R0, [R1, #10]
Example 2: LDR R2, [R3, #5]
Example 3: STRNE R0, [R1, #10]

notes: 
* The supported memory instructions are just Load (LDR) and Store (STR) instructions only wich stores ore loads a whole word.
* The first regester is the destination register when load and the source register when store.

3- Branch instructions (forward Branching only)

Example 1: B, #4
Example 2: BL, #6
Example 3: BLEQ, #8

notes:
* The immediate decimal value after the branch instruction represents the number of instructions needed to be skipped
* Both branch and branch link instructions are supported
