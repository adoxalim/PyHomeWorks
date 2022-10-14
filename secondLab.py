def currentTime( ):
    currentYear=2022
    currentMonth=12
    currentDay=28
    return currentDay,currentMonth,currentYear
def totalDays(bornday,bornmonth,bornyear):
    fullBirthDay=currentTime()
    return ((fullBirthDay[0]-bornday)+(fullBirthDay[1]-bornmonth) * 30 + (fullBirthDay[2]-bornyear)*365)
def totalHours(bornday,bornmonth,bornyear):
    return totalDays(bornday,bornmonth,bornyear) * 24
bornYear=int(input("Which year you was born : "))
bornMonth=int(input("Which month you was born : "))
bornDay=int(input("Which day you was born : "))
totalDaysOfLife=totalDays(bornDay,bornMonth,bornYear)
print("The person has been living for ",totalDaysOfLife," days.")
totalHoursOfLife=totalHours(bornDay,bornMonth,bornYear)
print("The person has been living for ", totalHoursOfLife ," hours.")