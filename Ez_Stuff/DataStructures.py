
def main():

    #Listen / Lists
    firstList = [1, "Hello", 7, 6.4, "World"]#Listen werden mit hilfe von [] init.. Sie können alle Values halten
    print("Thats the List:",firstList)
    print(firstList[0])#So können einzlne Inhalte abgefragt werden. Listen beginnen immer mit 0
    print(firstList[1],firstList[4])

    #Tuplets
    firstTuplet = 0, 1, 2
    print("\nThats the Tuplet:",firstTuplet)
    print(firstTuplet[2])
    #firstTuplet[1] = 2 Würde einen Fehler ausgeben ,da tuplets nicht editierbar sind

    #Dictionaries
    firstDict = {"Noah":"Cool", "An3": 3, "Mathis": 100}
    print("\nThats the Dictionary",firstDict)
    print("Noah ist",firstDict["Noah"])
    firstDict["Noah"] = "doch Blöd"
    print("Noah ist",firstDict["Noah"])


if __name__ == "__main__":
    main()
