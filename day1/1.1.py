import math

def main():
	answer = 0
	#For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
	with open('input.txt') as f:
		for cnt, line in enumerate(f):
			c = math.floor((int(line)/3)) - 2
			answer = answer + c

	print(answer)
if __name__ == '__main__':
	main()