# garden_advice.py
# A program that provides gardening tips and advice based on the current month and season.


def get_season(month):
    """Determine the season based on the month number (1-12)."""
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


def get_advice(season):
    """Return gardening advice based on the current season."""
    if season == "Winter":
        return "Protect your plants from frost. Prune dormant trees and plan next year's garden."
    elif season == "Spring":
        return "Start sowing seeds indoors. Begin preparing your soil and watch for early pests."
    elif season == "Summer":
        return "Water regularly, especially in dry spells. Harvest vegetables often to encourage growth."
    else:
        return "Plant spring bulbs now. Clear fallen leaves and compost them for next season."


# Ask the user to enter the current month
month = int(input("Enter the current month (1-12): "))

# Get the season and advice using the functions above
season = get_season(month)
advice = get_advice(season)

# Display the results
print("Month:", month)
print("Season:", season)
print("Gardening Advice:", advice)