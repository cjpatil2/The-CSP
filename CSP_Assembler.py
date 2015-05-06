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

# Universal "constants" related to the ISA and architecture
int word_size = 32
int addressability = 32	# MOST LIKELY WILL HAVE TO CHANGE
int register_bits = 4
int 
int 
