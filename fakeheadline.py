import random

# Lists of components
subjects = [
    "Aliens", "Elon Musk", "Politicians", "Scientists", "A Secret Society",
    "AI Robots", "Flat Earthers", "A Time Traveler", "The Government", "Lizard People"
]

verbs = [
    "discover", "ban", "invent", "destroy", "expose", "approve", "leak",
    "control", "predict", "sabotage"
]

objects = [
    "a mind-control chip", "immortality pill", "a parallel universe", "the moon landing hoax",
    "talking bananas", "teleportation device", "fake elections", "alien baby",
    "time travel machine", "Mars civilization"
]

places = [
    "in Area 51", "under the White House", "inside a volcano", "in the Bermuda Triangle",
    "on TikTok", "in North Korea", "in Antarctica", "on Mars", "inside Google HQ", "beneath the ocean"
]

# Function to generate a fake news headline
def generate_headline():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    place = random.choice(places)
    return f"{subject} {verb} {obj} {place}!"

# Main loop
while True:
    print("\n📰 FAKE NEWS HEADLINE:")
    print(generate_headline())

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        print("Goodbye! Stay skeptical 😄")
        break
