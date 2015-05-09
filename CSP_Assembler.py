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

	# Check first word. Several possibilities can occur
	# 3. Opcode (treat as normal instruction)
	# 4. Something else...label, data

	# If a line is just a comment, ignore, string basically doesn't change
	if parsed_spaces[0] == "#"
		output_values = output_values + ""

	# If the first word is BEGIN, signify a program beginning
	if parsed_spaces[0] == "BEGIN"
		base_address = int(parsed_spaces[1])

	# Call the opcode translation function

# Functions for various opcode types
# 1. Arithmetic/Floating-point/Shift
# 2. Control instructions
# 3. Mem-type
# 4. Special opcodes


def opcode_translate(curr_line):

	if(curr_line[0] == "ADD")
		temp_string = temp_string + "000000"
	else if (curr_line[0] == "SUB")
		temp_string = temp_string + "000001"
	else if (curr_line[0] == "MULT")
		temp_string = temp_string + "000010"
	else if (curr_line[0] == "DIV")
		temp_string = temp_string + "000011"

	else if (curr_line[0] == "AND")
		temp_string = temp_string + "000100"
	else if (curr_line[0] == "OR")
		temp_string = temp_string + "000101"
	else if (curr_line[0] == "NOT")
		temp_string = temp_string + "000110"
	else if (curr_line[0] == "XOR")
		temp_string = temp_string + "000111"

	else if (curr_line[0] == "LSA")
		temp_string = temp_string + "001000"
	else if (curr_line[0] == "LSD")
		temp_string = temp_string + "001000"
	else if (curr_line[0] == "RSA")
		temp_string = temp_string + "001001"
	else if (curr_line[0] == "RSD")
		temp_string = temp_string + "001001"
	


SUB
MULT
DIV
AND
OR
NOT
XOR





	return temp_string

def hex-convert(d):
	hex_value = hex(d).split('x')[1]

	return hex_value








