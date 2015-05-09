#  
#	A sample ASM file for CSP.
#	This executes a loop multiplication routine
#	ECE 190 MP1 translated from LC3 to CSP
# 

BEGIN 0

	# Clear all basic registers
	# R1 contains the multiplier
	# R2 contains the multiplicand
	# R3 contains the bitmask.
	# R4 contains the temporary multiplication result
	# R5 contains the final multiplication answer

	AND $R1 $R1 0
	AND $R2 $R2 0
	AND $R3 $R3 0
	AND $R4 $R4 0
	AND $R5 $R5 0

	LDI $R1 NUMTWO		# Loads value of multiplier
	LDI $R2 NUMONE		# Loads value of multiplicand
	ADD $R3 $R3 1		# Creates bitmask in R3 by adding 1 to empty R3.

OUTER:
	AND $R4 $R3 $R1		# Value of ANDed R3 and R1 stored in R4.
	BR z INNER			# Checks value of whether R4 is zero
	ADD $R5 $R5 $R2		# Offset value of R5 by digits via sum of R2

INNER:
	LSD	$R3 $R3 1		# Left shifts R3 over by 1 bit
	LSD $R2 $R2 1		# Left shifts R2 over by 1 bit
	BR np OUTER			# Checks value of whether R2 is positive/negative
	ST $R5 NUMTHREE		# Answer stored back into memory when finished

	HALT				# Halts program

NUMONE .DATA 6			# Holds the data for multiplicand
NUMTWO .DATA 4			# Holds the data for multiplier
NUMTHREE .DATA X		# Holds the result at this address
	
END
