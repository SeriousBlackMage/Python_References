

def main():
	x = 0

	while (x < 5):
		print (x)
		x = x + 1 

	for x in range(5,10):
		print(x)

	days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	for d in days: #For Loop wird über jeden Index iterieren
		print (d)

	for x in range(5,10):
		#if (x==7): break
		if (x % 2 == 0 ): continue #Continue skippt den Rest der Schleife und springt direkt an den Anfang zurück
		print(x)

	for i, d in enumerate(days): #i Wäre in diesem Fall der Index des Items.
		print(i, d)

if __name__ == "__main__":
	main()