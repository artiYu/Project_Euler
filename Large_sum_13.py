import os

def main():
	with open(os.getcwd() + "/Data/Large_sum_13.txt", "r") as infile:
		text = infile.readlines()

	sum_numbers = str(sum([int(i) for i in text]))[:10]
	print sum_numbers

if __name__ == '__main__':
	main()