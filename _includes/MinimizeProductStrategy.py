# fivethirtyeight.com Riddler https://fivethirtyeight.com/features/can-you-outsmart-our-elementary-school-math-problems/

from random import randint

def RemainingAverage2(A,B):
	# The average of the remaining numbers now that A and B are gone
	return (45 - A - B)/8

def RemainingAverage3(A,B,C):
	# The average of the remaining numbers now that A, B, and C are gone
	return (45 - A - B - C)/7

HighHigh = [7,8,9]
LowHigh = [5,6]
HighLow = [3,4]
LowLow = [0,1,2]

def	process(A,B,C,D):
	global cases, accum
	cases += 1
	if A < 5:
		UpLeft = A
		if B < RemainingAverage2(A,B):
			# A and B both Low numbers
			DownLeft = B
			if C < RemainingAverage3(A,B,C):
				# Couple C with the lower of A and B
				if A < B:
					UpRight = C
					DownRight = D
				else:
					UpRight = D
					DownRight = C
			else:
				if A > B:
					UpRight = C
					DownRight = D
				else:
					UpRight = D
					DownRight = C
		elif (A in HighLow and B in HighHigh) \
			or (A in LowLow and B in LowHigh):
			# A and B "match" in being high or low in their range
			UpRight = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				DownRight = D
			else:
				DownLeft = D
				DownRight = C
		else:
			# A in HighLow and B in LowHigh or A in LowLow and B in HighHigh
			DownRight = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				UpRight = D
			else:
				DownLeft = D
				UpRight = C
	else:
		# A is a High number
		UpRight = A
		if B >= RemainingAverage2(A,B):
			DownRight = B
			if A > B:
				if C > RemainingAverage3(A,B,C):
					UpLeft = C
					DownLeft = D
				else:
					DownLeft = C
					UpLeft = D
			else:
				if C < RemainingAverage3(A,B,C): 
					UpLeft = C
					DownLeft = D
				else:
					DownLeft = C
					UpLeft = D
		elif (A in HighHigh and B in HighLow) \
			or (A in LowHigh and B in LowLow):
			UpLeft = B
			if C < RemainingAverage3(A,B,C):
				DownLeft = C
				DownRight = D
			else:
				DownLeft = D
				DownRight = C
		else:
			# A in HighHigh and B in LowLow or A in LowHigh and B in HighLow
			DownLeft = B
			if C < RemainingAverage3(A,B,C):
				UpLeft = C
				DownRight = D
			else:
				DownRight = C
				UpLeft = D
	accum += (10*UpLeft + UpRight)*(10*DownLeft + DownRight)

cases = 0
accum = 0
for A in range(10):
	for B in range(10):
		if B == A:
			continue
		for C in range(10):
			if C in [A,B]:
				continue
			for D in range(10):
				if D in [A,B,C]:
					continue
				process(A,B,C,D)
print(accum/cases)
