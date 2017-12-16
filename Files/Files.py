

def main():
    #Open() öffnet eine File oder erstellt sie falls sie noch nicht vorhanden ist
    f = open("textfile.txt","w+") #Das Erste Argument ist die zu behandelnde Datei und das zweite ist "was gemacht werden soll"

    for i in range(10):
        f.write("This is line %d \r \n" % (i+1))

    f.close()

    f = open("textfile.txt", "a+") #Modus "a" hängt etwas an das vorhandene File an
    f.write("Hello :D")
    f.close()

    f = open("textfile.txt", "r")  # Modus "r" liest die file
    if f.mode == 'r':
        #contents = f.read()
        #print(contents)

        fl = f.readlines() #readLines() liest die einzlnen Zeilen in eine Liste
        for x in fl:
            print(x)

if __name__=="__main__":
    main()
