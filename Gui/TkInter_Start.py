from tkinter import * #Der Stern bewirkt, dass alles innerhalb von tkinter importiert wird
from tkinter import ttk

def main():

    root = Tk() #TK Klassen Instanzierung

    button = ttk.Button(root, text = 'Click Me') #Root wird als Parent gesetzt
    button.pack()

    #Buttons enthalten ein Dictionary in welchem alle Eigenschaften drinnen stehen
    button['text'] = 'Press Me'
    button.config(text = "Push me")

    ttk.Label(root, text = "Hello").pack() #Da keine Reference zu dem Object gespeichert wurde, kann man es später auch nicht weiter bearbeiten

    root.mainloop()

if __name__ == "__main__":
    main()
