
from datetime import date
from datetime import time
from datetime import datetime

def main():

    today = date.today() #Übergibt der Variable today das heutige Datum

    print("Today date is: ",today)
    print("Date Components: ", today.day, today.month, today.year)
    print("Today's Weekday Number: ", today.weekday())

    today = datetime.now()
    print("the current date and time is:", today)

    t = datetime.time(datetime.now()) #Übergibt t nur die zurzeitige Zeit
    print("The current time is:", t)

    wd = date.weekday(today)
    #Days start at 0 for Monday
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number: ", wd)
    print("Which is a", days[wd])


if __name__ == "__main__":
    main()
