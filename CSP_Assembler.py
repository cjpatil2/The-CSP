#=================================================================
#	
#	Chirag's Superscalar Processor: The Assembler
#				   -Chirag Patil
#	
#	This Python script acts as an assembler for running files on
#	the CSP Verilog processor. It follows the syntax and ISA as
#	defined in the software programmer guide (found in CSP/docs)
#	
#	The assembler first reads in an assembly file and line-by-line 
#	converts it into a hexadecimal string that the main processor 
#	memory can read (binary is ideal, but it's messy and hex is 
#	much neater to read and debug). The string is then into the
#	format of the ideal SystemVerilog memory file by addressability
#	of the RAM memory and then dumped into a memory.sv file.
#
#	Version 1.0 (May 2015): just a no-frills assembler. Only reads
#		pure instructions.

#	Later features include an optimization engine to reduce data
#	dependencies and memory access stalls during execution.
#
#=================================================================

from sys import argv

# Open the assembly file passed as a command-line argument
filename = sys.argv[1]
asm_file = open(filename)

# Create the memory file in the Quartus directory
memory_name = sys.argv[2]
memory_file = open(memory_name, 'w')

# This is the starting program address variable. Gets updated when the
# program's BEGIN statement is read. All offsets are derived by line
# offsets from this and previous held data variables.
base_address = NONE

# The final string output of hex values
string output_values = ""


for line in asm_file

	# Remove whitespace from beginning and split into list by spaces
	parsed_spaces = line.strip().split()

	# If a line is just a comment, ignore, string basically doesn't change
	if parsed_spaces[0] == "#"
		output_values = output_values + ""

	# If the first word is BEGIN, signify a program beginning
	if parsed_spaces[0] == "BEGIN"
		base_address = int(parsed_spaces[1])

	# Decode each line
	converted_line = decoded_line(parsed_spaces)

	# Write into file
	memory_file.write(converted_line)
	


def decoded_line(line_in_file):

	if (line_in_file[0] == "ADD" or 
		line_in_file[0] == "SUB" or 
		line_in_file[0] == "MULT" or
		line_in_file[0] == "DIV" or 
		line_in_file[0] == "AND" or
		line_in_file[0] == "OR" or 
		line_in_file[0] == "NOT" or
		line_in_file[0] == "XOR" or 
		line_in_file[0] == "LSA" or
		line_in_file[0] == "LSD" or 
		line_in_file[0] == "RSA" or
		line_in_file[0] == "RSD"):
		full_instruction = arithmetic_operation(line_in_file)

	if (line_in_file[0] == "FADD" or 
		line_in_file[0] == "FSUB" or 
		line_in_file[0] == "FMULT" or
		line_in_file[0] == "FDIV" or 
		line_in_file[0] == "ITOF" or
		line_in_file[0] == "FTOI"):
		full_instruction = floating_operation(line_in_file)

	if (line_in_file[0] == "BR" or 
		line_in_file[0] == "BRC" or 
		line_in_file[0] == "BREQ" or
		line_in_file[0] == "BRNEQ" or 
		line_in_file[0] == "JMP" or
		line_in_file[0] == "RET" or 
		line_in_file[0] == "PCR" or
		line_in_file[0] == "PCS"):
		full_instruction = branch_operation(line_in_file)

	if (line_in_file[0] == "LD" or 
		line_in_file[0] == "LDR" or 
		line_in_file[0] == "LDW" or
		line_in_file[0] == "LDB" or 
		line_in_file[0] == "LSP" or
		line_in_file[0] == "POP" or 
		line_in_file[0] == "SDEC"):
		full_instruction = load_operation(line_in_file)

	if (line_in_file[0] == "ST" or 
		line_in_file[0] == "STR" or 
		line_in_file[0] == "STW" or
		line_in_file[0] == "STB" or 
		line_in_file[0] == "STP" or
		line_in_file[0] == "PUSH" or 
		line_in_file[0] == "SINC"):
		full_instruction = store_operation(line_in_file)

	if (line_in_file[0] == "WVAL" or 
		line_in_file[0] == "HALT" or 
		line_in_file[0] == "NOP"):
		full_instruction = special_operation(line_in_file)

	else
		full_instruction = ""

	return full_instruction

# Decodes the full artihmetic instruction into a binary string
def arithmetic_operation(line_in_file):

	opcode = arith_opcode_decode(line_in_file[0])
	dr_set = register_convert(line_in_file[1])
	sr1_set = register_convert(line_in_file[2])

	# Depending on the last number, the instruction is I- or R-type
	# In the case of NOT, we just ignore and set all remaining bits 0

	if line_in_file[0] == "NOT"
		sr2_set = "00000000000000000"

	else if line_in_file[0] == "LSD" or line_in_file[0] == "RSD"
		sr2_set = imm_convert(line_in_file[3], '017b') + "0"

	else if '$' in line_in_file[3]
		sr2_set = register_convert(line_in_file[3]) + "00000000000000"

	else if '$' not in line_in_file[3]
		sr2_set = imm_convert(line_in_file[3], '017b') + "1"

	final_instruction = opcode + dr_set + sr1_set + sr2_set
	hex_decoded_instr = hex_convert(final_instruction)

	return hex_decoded_instr

# Opcode decode function for arithmetic instructions
def arith_opcode_decode(line_in_file):

	if(line_in_file[0] == "ADD")
		op_out = "000000"
	else if line_in_file[0] == "SUB":
		op_out = "000001"
	else if line_in_file[0] == "MULT":
		op_out = "000010"
	else if line_in_file[0] == "DIV":
		op_out = "000011"

	else if line_in_file[0] == "AND":
		op_out = "000100"
	else if line_in_file[0] == "OR":
		op_out = "000101"
	else if line_in_file[0] == "NOT":
		op_out = "000110"
	else if line_in_file[0] == "XOR":
		op_out = "000111"

	else if line_in_file[0] == "LSA":
		op_out = "001000"
	else if line_in_file[0] == "LSD":
		op_out = "001000"
	else if line_in_file[0] == "RSA":
		op_out = "001001"
	else if line_in_file[0] == "RSD":
		op_out = "001001"

	return op_out


# Register number to binary converter. Takes in a segment of an instruction
# word like $0 and converts the number into a 4-digit binary value.
def register_convert(instruction_term):

	no_dollar = instruction_term.split("$",1)[1]
	converted_value = format(int(no_dollar), '004b')

	return converted_value

# Generalized decimal to binary converter, usually used for immediates.
def imm_convert(instruction_term, string_formatter):

	converted_value = format(int(instruction_term), string_formatter)	# '004b' example

	return converted_value

# Binary string to hex converter (without the 1x in front)
def hex_convert(bin_value):

	hex_value = hex(int(bin_value,2)).split('x')[1]

	return hex_value
	