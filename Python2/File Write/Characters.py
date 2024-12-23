import random
import string

def generate_syllable():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    return random.choice(consonants) + random.choice(vowels) + random.choice(consonants)

def generate_unique_character_names(count):
    names_set = set()

    while len(names_set) < count:
        name = "".join(generate_syllable() for _ in range(3))
        names_set.add(name.capitalize())

    return list(names_set)

def save_names_to_file(names, filename="File Write/character_names.txt"):
    with open(filename, "w") as file:
        for name in names:
            file.write(name + "\n")

def main():
    try:
        num_names = int(input("Enter the number of character names to generate: "))
        if num_names <= 0:
            raise ValueError("The number of names must be greater than zero.")

        character_names = generate_unique_character_names(num_names)
        save_names_to_file(character_names)
        print(f"{num_names} character names have been generated and saved to 'character_names.txt'.")

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
