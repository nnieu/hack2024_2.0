# services/scenario_service.py
import random

date_ideas = [
    "Enjoy a day outdoors",
    "Explore a local attraction",
    "Attend a live performance",
    "Go for a nature walk",
    "Visit a cultural site",
    "Take a class together",
    "Experience a food event",
    "Have a cozy night in",
    "Engage in a fun competition",
    "Visit an entertainment venue",
    "Spend a day at a fair or festival",
    "Watch a sports event",
    "Catch a film together",
    "Learn a new dance style",
    "Discover historical landmarks",
    "Take a scenic drive",
    "Enjoy a tasting experience",
    "Get creative with a craft activity",
    "Relax at a café",
    "Go on a leisurely bike ride",
    "Host a game night at home",
    "Shop at a local market",
    "Stargaze under the night sky",
    "Try a unique experience together",
    "Enjoy seasonal activities",
    "Attend a community gathering",
    "Visit a creative space",
    "Take on a fun challenge",
    "Spend a day in nature",
    "Explore new food options",
    "Participate in a local event",
    "Create art together",
    "Visit a specialty shop",
    "Enjoy a relaxing day at home",
    "Spend time at a scenic location",
    "Try a new recreational activity",
    "Attend a social gathering",
    "Explore a nearby city",
    "Spend a day at the beach",
    "Enjoy a themed dinner night",
    "Try a new hobby together",
    "Take a scenic boat ride",
    "Attend a workshop or seminar",
    "Discover local history",
    "Engage in a fun physical activity",
    "Attend a storytelling event",
    "Try out an adventurous activity",
    "Explore a community garden",
    "Visit a farm or orchard",
    "Take part in a food tour",
    "Enjoy a wellness day",
    "Share a meal at a new restaurant",
    "Participate in a local class",
    "Explore a local market",
    "Spend a day exploring nature trails",
    "Try an indoor activity together",
    "Participate in an arts and crafts fair",
    "Attend a themed event or festival",
    "Visit a historic town or village",
    "Try an escape room experience",
    "Spend time in a cozy bookstore",
    "Take a leisurely scenic hike",
    "Enjoy a culinary experience",
    "Attend a lecture or talk",
    "Try a new dessert place",
    "Participate in a local charity event",
    "Spend time at an amusement park",
    "Go to a unique venue",
    "Participate in a local sports event",
    "Try a new adventure sport",
    "Attend a community art show",
    "Visit an interactive exhibit",
    "Try out new board games",
    "Spend a day volunteering together",
    "Visit a local winery or brewery",
    "Go to a trivia night",
    "Engage in a cooking or baking session",
    "Explore a nature reserve",
    "Try out an outdoor activity",
    "Visit a petting zoo or animal sanctuary",
    "Spend time at a local festival or fair",
    "Attend a cultural or music festival",
    "Visit a new coffee shop",
    "Participate in a themed scavenger hunt",
    "Enjoy a cozy movie marathon",
    "Visit a unique outdoor market",
    "Take part in a wellness workshop",
    "Try out a new fitness class together",
    "Explore local street art",
    "Attend a public lecture or discussion",
    "Go strawberry picking together",
    "Relax at a cat cafe",
]


scenarios = {
    "easy": {
        "description": "an easy-going conversation where the we are actively engaged with the user and their interests. Make the conversation flow easily.",
        "prompt": "Start a friendly and casual conversation with the user."
    },
    "medium": {
        "description": "a more in-depth conversation about personal opinions. Introduce some differences in the user and our opinions.",
        "prompt": "Engage the user in a meaningful conversation while being friendly."
    },
    "hard": {
        "description": "an uncomfortable and awkward situation.",
        "prompt": "Respond to the user in a way that creates an awkward and tense conversation."
    }
}

def get_scenario(scenario_type):
    return scenarios.get(scenario_type, scenarios["easy"])  # Default to "easy" if not found

def get_random_date_idea():
    """Return a random date idea from the date_ideas list."""
    return random.choice(date_ideas)