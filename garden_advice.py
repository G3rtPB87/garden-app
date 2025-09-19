"""
Garden Advice App
This module provides a simple command-line application for giving gardening
advice based on user input for the current season and plant type.
Functions:
    get_user_input():
        Prompts the user to enter the current season and plant type.
        Returns:
            tuple: (season, plant_type) as lowercase strings.
    get_season_advice(season):
        Provides gardening advice specific to the given season.
        Args:
            season (str): The current season (e.g., 'summer', 'winter').
        Returns:
            str: Advice message for the season.
    get_plant_advice(plant_type):
        Provides gardening advice specific to the given plant type.
        Args:
            plant_type (str): The type of plant (e.g., 'flower', 'vegetable').
        Returns:
            str: Advice message for the plant type.
    main():
        Runs the gardening advice program by collecting user input,
        generating advice, and displaying it.
Usage:
    Run this module directly to start the interactive gardening advice app.
Future Improvements:
    - Store advice in a dictionary for multiple plants and seasons.
    - Recommend plants based on the entered season.
"""


def get_user_input():
    """Prompts the user for season and plant type and returns the values."""
    season = input("Enter the current season (e.g., summer, winter): ").lower()
    plant_type = input(
        "Enter your plant type (e.g., flower, vegetable): "
    ).lower()
    return season, plant_type


def get_season_advice(season):
    """Returns advice specific to the given season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Returns advice specific to the given plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Main function to run the gardening advice program."""
    # Get user input
    season, plant_type = get_user_input()

    # Get advice based on input
    advice = get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Print the generated advice
    print(advice)


# Run the program
if __name__ == "__main__":
    main()

# TODO: Future improvements:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
