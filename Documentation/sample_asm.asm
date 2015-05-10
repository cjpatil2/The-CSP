#  
#	A sample ASM file for CSP.
#	This executes a loop multiplication routine
#	ECE 190 MP1 translated from LC3 to CSP
# 

BEGIN 0

	# Clear all basic registers
	# $1 contains the multiplier
	# $2 contains the multiplicand
	# $3 contains the bitmask.
	# $4 contains the temporary multiplication result
	# $5 contains the final multiplication answer

	AND $1 $1 0
	AND $2 $2 0
	AND $3 $3 0
	AND $4 $4 0
	AND $5 $5 0

	LDI $1 NUMTWO		# Loads value of multiplier
	LDI $2 NUMONE		# Loads value of multiplicand
	ADD $3 $3 1			# Creates bitmask in $3 by adding 1 to empty $3.

OUTER:
	AND $4 $3 $1		# Value of ANDed $3 and $1 stored in $4.
	BR z INNER			# Checks value of whether $4 is zero
	ADD $5 $5 $2		# Offset value of $5 by digits via sum of $2

INNER:
	LSD	$3 $3 1			# Left shifts $3 over by 1 bit
	LSD $2 $2 1			# Left shifts $2 over by 1 bit
	BR np OUTER			# Checks value of whether $2 is positive/negative
	ST $5 NUMTHREE		# Answer stored back into memory when finished

	HALT				# Halts program

NUMONE .DATA 6			# Holds the data for multiplicand
NUMTWO .DATA 4			# Holds the data for multiplier
NUMTHREE .DATA X		# Holds the result at this address
	
END
