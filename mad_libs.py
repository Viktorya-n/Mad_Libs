import random

def get_input(prompt, validation_type="word"):
    while True:
        try:
            val = input(prompt).strip()

            if not val:
                print("Input can't be blank, try again.")
                continue

            vtype = validation_type.lower()

            if vtype == "number":
                if val.isdigit():
                    return val
                print("Error: Please enter a numeric value (digits only).")

            elif vtype == "ing":
                if val.lower().endswith("ing") and val.replace(" ", "").isalpha():
                    return val
                print("Error: word must end in and contain letters only 'ing'.")

            elif vtype == "ly":
                if val.lower().endswith("ly") and val.replace(" ", "").isalpha():
                    return val
                print("Error: word must end in 'ly'.")

            elif vtype == "word":
                if val.replace(" ", "").isalpha():
                    return val
                print("Error: please use letters only.")

            elif vtype == "measure of time":
                valid_times = [
                    "second", "seconds", "minute", "minutes",
                    "hour", "hours", "day", "days",
                    "week", "weeks", "month", "months",
                    "year", "years"
                ]
                if val.lower() in valid_times:
                    return val
                print("Error: Please enter a valid measure of time (minute, day, year).")

            else:
                return val

        except (KeyboardInterrupt, EOFError):
            raise ExitGame


class ExitGame(Exception):
    pass


def play_mad_libs():
    print("\n___Mad Libs Station___\n")

    try:
        user_choice = input("Pick a template (1, 2, or 3): ").strip()

        if user_choice not in ["1", "2", "3"]:
            print("Hmm, that's not 1, 2, or 3...")
            choice = random.randint(1, 3)
            print(f"Randomly picked Template {choice} for you!\n")
        else:
            choice = int(user_choice)

        print(f"\nTemplate {choice} it is! Fill in the blanks:\n")

        if choice == 1:
            number1 = get_input("Number: ", "number")
            time1 = get_input("Measure of time: ", "measure of time")
            transport = get_input("Mode of Transportation: ")
            adj1 = get_input("Adjective: ")
            adj2 = get_input("Adjective: ")
            noun1 = get_input("Noun: ")
            color1 = get_input("Color: ")
            body1 = get_input("Part of the Body: ")
            verb1 = get_input("Verb: ")
            number2 = get_input("Number: ", "number")
            noun2 = get_input("Noun: ")
            noun3 = get_input("Noun: ")
            body2 = get_input("Part of the Body: ")
            verb2 = get_input("Verb: ")
            noun4 = get_input("Noun: ")
            adj3 = get_input("Adjective: ")
            silly1 = get_input("Silly Word: ", "any")
            noun5 = get_input("Noun: ")

            story = f"""
It was about {number1} {time1} ago when I arrived at the hospital in a {transport}.
The hospital is a/an {adj1} place, there are a lot of {adj2} {noun1} here.
There are nurses here who have {color1} {body1}. If someone wants to come into my room
I told them that they have to {verb1} first. I've decorated my room with {number2} {noun2}.
Today I talked to a doctor and they were wearing a {noun3} on their {body2}.
I heard that all doctors {verb2} {noun4} every day for breakfast.
The most {adj3} thing about being in the hospital is the {silly1} {noun5}!"""

        elif choice == 2:
            name1 = get_input("Person's Name: ")
            noun1 = get_input("Noun: ")
            feeling1 = get_input("Feeling: ")
            verb1 = get_input("Verb: ")
            feeling2 = get_input("Feeling: ")
            animal1 = get_input("Animal: ")
            verb2 = get_input("Verb: ")
            color1 = get_input("Color: ")
            verb3 = get_input("Verb (ending in ing): ", "ing")
            adverb1 = get_input("Adverb (ending in ly): ", "ly")
            number1 = get_input("Number: ", "number")
            time1 = get_input("Measure of time: ", "measure of time")
            color2 = get_input("Color: ")
            animal2 = get_input("Animal: ")
            number2 = get_input("Number: ", "number")
            silly1 = get_input("Silly Word: ", "any")
            noun2 = get_input("Noun: ")

            story = f"""
This weekend I am going camping with {name1}. I packed my lantern, sleeping bag, and {noun1}.
I am so {feeling1} to {verb1} in a tent. I am {feeling2} we might see a(n) {animal1},
I hear they're kind of dangerous. While we're camping, we are going to hike, fish, and {verb2}.
I have heard that the {color1} lake is great for {verb3}. Then we will {adverb1} hike
through the forest for {number1} {time1}. If I see a {color2} {animal2} while hiking,
I am going to bring it home as a pet! At night we will tell {number2} {silly1} stories
and roast {noun2} around the campfire!"""

        elif choice == 3:
            name1 = get_input("Person's Name: ")
            adj1 = get_input("Adjective: ")
            color1 = get_input("Color: ")
            animal1 = get_input("Animal: ")
            place1 = get_input("Place: ", "any")
            adj2 = get_input("Adjective: ")
            creature1 = get_input("Plural Magical Creature: ")
            adj3 = get_input("Adjective: ")
            creature2 = get_input("Plural Magical Creature: ")
            room1 = get_input("Room in a House: ")
            noun1 = get_input("Noun: ")
            noun2 = get_input("Noun: ")
            noun3 = get_input("Plural Noun: ")
            adj4 = get_input("Adjective: ")
            noun4 = get_input("Plural Noun: ")
            number1 = get_input("Number: ", "number")
            time1 = get_input("Measure of time: ", "measure of time")
            verb1 = get_input("Verb (ending in ing): ", "ing")
            adj5 = get_input("Adjective: ")
            noun5 = get_input("Noun: ")

            story = f"""
Dear {name1}, I am writing to you from a {adj1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color1} {animal1} in {place1}.
There are {adj2} {creature1} and {adj3} {creature2} here!
In the {room1} there is a pool full of {noun1}. I fall asleep each night on a {noun2}
of {noun3} and dream of {adj4} {noun4}. It feels as though I have lived here
for {number1} {time1}. I hope one day you can visit, although the only way to get here
now is {verb1} on a {adj5} {noun5}!!"""

        print("\n___YOUR STORY___")
        print(story)

    except ExitGame:
        print("\n bye!!")


if __name__ == "__main__":
    play_mad_libs()