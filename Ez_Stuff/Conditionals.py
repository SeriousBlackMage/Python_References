


def main():
	x, y = 100, 1000

	if y < x :
		st = "x is larger than y"

	elif y == x:
		st = "x is equal to y"

	else:
		st = "x is smaller than y"

	print (st)

	st = "x is larger than y" if x > y else "x is smaller or equal to y" 
	print (st)
if __name__ == "__main__":
	main()


