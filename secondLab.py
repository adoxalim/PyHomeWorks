'''
#IN THIS ASSIGNMENT YOU WILL WRITE A SIMPLE PROGRAM TO COMPUTE SOMEONE'S AGE IN TERMS OF DAYS AND HOURS. 
STEP-BY-STEP INSTRUCTIONS ARE PROVIDED BELOW.
MAKE SURE THAT THE VARIABLES ARE NAMED PROPERLY.
'''

#STEP 1) Define a function that returns the current year, month, and day.
#This function should include the following:
#2.1 A variable that holds the current year (i.e., 2022)
#2.2 A variable that holds the current month (i.e., 10)
#2.3 A variable that holds the current day (i.e., 17)

def currentTime( ):
   currentYear=2022
   currentMonth=12
   currentDay=28
   return currentDay,currentMonth,currentYear

#For this assignment, we assume that current month is greater than the month the user was born, and that current day is greater than the day the user was born.
#STEP 2) Define a function (with a proper name) that computes and returns the total number of days that the user has been alive (in other words, the age in terms of days). The parameters should include year, month, and day. This function should call the function created in STEP #1 to get the current year, month, and day info, which are necessary for the computation.

def totalDays(bornday,bornmonth,bornyear):
    fullBirthDay=currentTime()
    return ((fullBirthDay[0]-bornday)+(fullBirthDay[1]-bornmonth) * 30 + (fullBirthDay[2]-bornyear)*365)
#STEP 3) Define a function (with a proper name) that computes and returns the total number of hours that the user has been alive (in other words, the age in terms of hours). This function should make a call to the function defined in Step #1 to compute the hours.
def totalHours(bornday,bornmonth,bornyear):
    return totalDays(bornday,bornmonth,bornyear) * 24
#STEP 4) Write the necessary code to ask the user the following info (separately):
#--The year s/he was born (e.g., 2001)
#--The month s/he was born (e.g., 9)
#--The day you s/he born (e.g., 15)
bornYear=int(input("Which year you was born : "))
bornMonth=int(input("Which month you was born : "))
bornDay=int(input("Which day you was born : "))
#STEP 5 Make a proper call to the function defined in Step #2 to compute the user age in terms of days. Assign the computation result into a new variable.
totalDaysOfLife=totalDays(bornDay,bornMonth,bornYear)
#STEP 6 Print the total number of days as shown in the example below.
#The person has been living for 13684 days.
print("The person has been living for ",totalDaysOfLife," days.")
#STEP 7 Make a proper call to the function defined in Step #3 to compute the user age in terms of hours. Assign the computation result into a new variable.
totalHoursOfLife=totalHours(bornDay,bornMonth,bornYear)
#STEP 8 Print the total number of hours as shown in the example below.
#The person has been living for 326496 hours.
print("The person has been living for ", totalHoursOfLife ," hours.")