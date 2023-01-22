"""
## Grading program
##
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
score = 0
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

## travel log
##
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
"""
## blind auction
##

top_bidder = ""
top_bid = 0
all_bids = {}

more_bidders = True
while more_bidders:
    name = input("What is your name?")
    price = float(input("What is your bid?"))
    all_bids[name] = price
    another_bidder = input("Is there another bidder? Y or N")
    if another_bidder == "N":
        more_bidders = False

for bidder in all_bids:
    if all_bids[bidder] > top_bid:
        top_bidder = bidder
        top_bid = all_bids[bidder]

print(f"The winning bid was {top_bid} from {top_bidder}")