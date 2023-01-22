print("Welcome to the tip calculator.")
bill = float( input("What was the total bill?" + " $") )
percentage = float( input("What percentage tip would you like to pay? ") )
people = int( input("How many people are splitting the bill? ") )

bill = bill
total = ( (percentage / 100) + 1) * bill
# per_person = round( (total / people), 2 )
per_person = "{:.2f}".format( (total / people) )

print( "Each person should pay:" + " $" + str(per_person) )

"""
score = 0
height = 1.8
isWinning = True
#f-string
print(f"your score is {score}, your height is {height}, and your winning is {isWinning}")

age_years = int( input("What is your age? ") )
age_months = age_years*12
age_weeks = age_years*52
age_days = age_years*365

max_years = 90
max_months = max_years*12
max_weeks = max_years*52
max_days = max_years*365

years_left = max_years - age_years
months_left = max_months - age_months
weeks_left = max_weeks - age_weeks
days_left = max_days - age_days

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
"""