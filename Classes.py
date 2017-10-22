
class myClass():

    def method1(self): #Self-Argument weist auf das Object an sich hin.
        print("myClass Method1")

    def method2(self, someString):
        print("myClass Method2 " + someString)

class anotherClass(myClass): #anotherClass wird inheritiert von myClass
    def method2(self): #Methoden werden Overrided
        print("anotherClass Method2")

    def method1(self):
        myClass.method1(self);
        print("anotherClass method1")

    #Test #Noch ein Test 

def main():

    c = myClass() #Klasse wird als Object instanziert
    c.method1() #Methode1 wird gecalled
    c.method2("This is a String") #Man muss kein Parameter für self übergeben. Das macht Python schon selber
    c2 = anotherClass()
    c2.method1()

if __name__ == "__main__":
    main()
