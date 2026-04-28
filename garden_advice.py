# garden_advice.py
# A program that provides gardening tips and advice based on the current month and season.

# TODO: Replace hardcoded month number with user input using the input() function
# TODO: Add a function called get_season() to determine the season from the month
# TODO: Add a function called get_advice() to return gardening advice based on the season
# TODO: Add comments/docstrings to document what each section of the code does

month = 4

if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"

if season == "Winter":
    advice = "Protect your plants from frost. Prune dormant trees and plan next year's garden."
elif season == "Spring":
    advice = "Start sowing seeds indoors. Begin preparing your soil and watch for early pests."
elif season == "Summer":
    advice = "Water regularly, especially in dry spells. Harvest vegetables often to encourage growth."
else:
    advice = "Plant spring bulbs now. Clear fallen leaves and compost them for next season."

print("Month:", month)
print("Season:", season)
print("Gardening Advice:", advice)
