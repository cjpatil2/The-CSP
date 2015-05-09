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
		full_instruction = arithmetic_op(line_in_file)

	if (line_in_file[0] == "FADD" or 
		line_in_file[0] == "FSUB" or 
		line_in_file[0] == "FMULT" or
		line_in_file[0] == "FDIV" or 
		line_in_file[0] == "ITOF" or
		line_in_file[0] == "FTOI"):
		full_instruction = floating_op(line_in_file)

	if (line_in_file[0] == "BR" or 
		line_in_file[0] == "BRC" or 
		line_in_file[0] == "BREQ" or
		line_in_file[0] == "BRNEQ" or 
		line_in_file[0] == "JMP" or
		line_in_file[0] == "RET" or 
		line_in_file[0] == "PCR" or
		line_in_file[0] == "PCS"):
		full_instruction = branch_op(line_in_file)

	if (line_in_file[0] == "LD" or 
		line_in_file[0] == "LDR" or 
		line_in_file[0] == "LDW" or
		line_in_file[0] == "LDB" or 
		line_in_file[0] == "LSP" or
		line_in_file[0] == "POP" or 
		line_in_file[0] == "SDEC"):
		full_instruction = load_op(line_in_file)

	if (line_in_file[0] == "ST" or 
		line_in_file[0] == "STR" or 
		line_in_file[0] == "STW" or
		line_in_file[0] == "STB" or 
		line_in_file[0] == "STP" or
		line_in_file[0] == "PUSH" or 
		line_in_file[0] == "SINC"):
		full_instruction = load_op(line_in_file)

	if (line_in_file[0] == "WVAL" or 
		line_in_file[0] == "HALT" or 
		line_in_file[0] == "NOP"):
		full_instruction = special_op(line_in_file)

	else
		full_instruction = ""

	return full_instruction


def arithmetic_op(instruction_line):


	return 

def floating_op(instruction_line):


	return 

def branch_op(instruction_line):


	return 

def load_op(instruction_line):


	return 

def store_op(instruction_line):


	return 

def special_op(instruction_line):


	return 



# The largest look-up table function ever. Just assigns a boolean value for
# every opcode in the system. Wondering if I can clean this up.
def opcode_translate(curr_word):

	if(curr_word == "NOP")
		opcode_out = "111111"

	else if(curr_word == "ADD")
		opcode_out = "000000"
	else if curr_word == "SUB":
		opcode_out = "000001"
	else if curr_word == "MULT":
		opcode_out = "000010"
	else if curr_word == "DIV":
		opcode_out = "000011"

	else if curr_word == "AND":
		opcode_out = "000100"
	else if curr_word == "OR":
		opcode_out = "000101"
	else if curr_word == "NOT":
		opcode_out = "000110"
	else if curr_word == "XOR":
		opcode_out = "000111"

	else if curr_word == "LSA":
		opcode_out = "001000"
	else if curr_word == "LSD":
		opcode_out = "001000"
	else if curr_word == "RSA":
		opcode_out = "001001"
	else if curr_word == "RSD":
		opcode_out = "001001"

	else if curr_word == "FADD":
		opcode_out = "001010"
	else if curr_word == "FSUB":
		opcode_out = "001011"
	else if curr_word == "FMULT":
		opcode_out = "001100"
	else if curr_word == "FDIV":
		opcode_out = "001101"
	else if curr_word == "ITOF":
		opcode_out = "001110"
	else if curr_word == "FTOI":
		opcode_out = "001111"

	else if curr_word == "BR":
		opcode_out = "010000"
	else if curr_word == "BRC":
		opcode_out = "010001"
	else if curr_word == "BREQ":
		opcode_out = "010010"
	else if curr_word == "BRNEQ":
		opcode_out = "010011"

	else if curr_word == "JMP":
		opcode_out = "010 100"
	else if curr_word == "RET":
		opcode_out = "010 101"
	else if curr_word == "PCR":
		opcode_out = "010 110"
	else if curr_word == "PCS":
		opcode_out = "010 111"

	else if curr_word == "LD":
		opcode_out = "011 000"
	else if curr_word == "LDR":
		opcode_out = "011 001"
	else if curr_word == "LDW":
		opcode_out = "011 010"
	else if curr_word == "LDB":
		opcode_out = "011 011"
	else if curr_word == "LSP":
		opcode_out = "011 100"
	else if curr_word == "POP":
		opcode_out = "011 101"
	else if curr_word == "SDEC":
		opcode_out = "011 110"



	return opcode_out


def calc_offset(curr_line):


	return


# Binary to hex converter (without the 1x in front)
def hex-convert(bin_value):

	hex_value = hex(int(bin_value,2)).split('x')[1]

	return hex_value
	