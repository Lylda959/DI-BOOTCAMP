# ============================================================
# Exercise 1
# Instructions:
# You are given two lists.
# Convert them into a dictionary where the first list contains
# the keys and the second list contains the corresponding values.
# ============================================================

from ast import Call
from tokenize import String

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Convert the two lists into a dictionary
dictionnaire = dict(zip(keys, values))
print(dictionnaire)


# ============================================================
# Exercise 2
# Instructions:
# Write a program that calculates the total cost of movie tickets
# for a family based on their ages.
# Family members' ages are stored in a dictionary.
# Ticket pricing rules:
#   - Under 3 years old: Free
#   - 3 to 12 years old: $10
#   - Over 12 years old: $15
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
# ============================================================

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cout_total = 0

print("=== Prix des billets de cinéma ===\n")

for nom, age in family.items():
    if age < 3:
        cout = 0
        print(f"{nom.capitalize():<10} ({age} ans) → Gratuit")

    elif 3 <= age <= 12:
        cout = 10
        print(f"{nom.capitalize():<10} ({age} ans) → {cout}$")

    else:
        cout = 15
        print(f"{nom.capitalize():<10} ({age} ans) → {cout}$")

    cout_total += cout

print("-" * 40)
print(f"Coût total pour la famille : {cout_total}$")


# ============================================================
# Exercise 3
# Instructions:
# Create and manipulate a dictionary that contains information
# about the Zara brand.
# Brand Information:
#   name: Zara
#   creation_date: 1975
#   creator_name: Amancio Ortega Gaona
#   type_of_clothes: men, women, children, home
#   international_competitors: Gap, H&M, Benetton
#   number_stores: 7000
#   major_color: France: blue, Spain: red, US: pink, green
#
# Modify and access the dictionary as follows:
#   - Change the value of number_stores to 2
#   - Print a sentence describing Zara's clients using type_of_clothes
#   - Add a new key country_creation with the value Spain
#   - Check if international_competitors exists and add "Desigual"
#   - Delete the creation_date key
#   - Print the last item in international_competitors
#   - Print the major colors in the US
#   - Print the number of keys in the dictionary
#   - Print all keys of the dictionary
# Bonus: Create another dictionary and merge it with the original
# ============================================================

marque = {
    "nom": "Zara",
    "date_creation": 1975,
    "nom_createur": "Amancio Ortega Gaona",
    "type_vetements": ["hommes", "femmes", "enfants", "maison"],
    "concurrents_internationaux": ["Gap", "H&M", "Benetton"],
    "nombre_magasins": 7000,
    "couleur_principale": {
        "France": ["bleu"],
        "Espagne": ["rouge"],
        "US": ["rose", "vert"]
    }
}

# Change the value of number_stores to 2
marque["nombre_magasins"] = 2

# Print a sentence describing Zara's clients using type_of_clothes
print(f"Zara habille les : {', '.join(marque['type_vetements'])}")

# Add a new key country_creation with the value Spain
marque["pays_creation"] = "Espagne"

# Check if international_competitors exists and add "Desigual"
if "concurrents_internationaux" in marque:
    marque["concurrents_internationaux"].append("Desigual")

# Delete the creation_date key
del marque["date_creation"]

# Print the last item in international_competitors
print(f"Dernier concurrent : {marque['concurrents_internationaux'][-1]}")

# Print the major colors in the US
print(f"Couleurs principales aux US : {marque['couleur_principale']['US']}")

# Print the number of keys in the dictionary
print(f"Nombre de clés : {len(marque)}")

# Print all keys of the dictionary
print(f"Clés : {list(marque.keys())}")

# Bonus: Create another dictionary and merge it with the original
complement_zara = {"date_creation": 1975, "nombre_magasins": 7000}
marque.update(complement_zara)
print(f"\nDictionnaire fusionné : {marque}")


# ============================================================
# Exercise 4
# Instructions:
# Create a function that describes a city and its country.
# Key Python Topics: Functions with multiple parameters,
# default parameter values, string formatting.
#
# Step 1: Define a function named describe_city()
#         with two parameters: city and country.
#         Give the country parameter a default value of "Unknown".
# Step 2: Inside the function, display a sentence like
#         "<city> is in <country>."
# Step 3: Call describe_city() with different combinations.
#         Try with and without providing the country argument.
#         Example: describe_city("Reykjavik", "Iceland")
#                  describe_city("Paris")
# ============================================================

def decrire_ville(ville, pays="Inconnu"):
    # Print a sentence: "<city> is in <country>"
    print(f"{ville} est en {pays}.")

# Call the function with city and country
decrire_ville("Reykjavik", "Islande")
# Call the function without country to use default value
decrire_ville("Paris")
decrire_ville("Abidjan")


# ============================================================
# Exercise 5
# Instructions:
# Create a function that generates random numbers and compares them.
# Key Python Topics: random module, random.randint(), conditionals.
#
# Step 1: Import the random module.
# Step 2: Define a function that accepts a number between 1 and 100.
# Step 3: Inside the function, use random.randint(1, 100)
#         to generate a random integer.
# Step 4: If both numbers are the same, print a success message.
#         Otherwise, print a fail message and display both numbers.
# Step 5: Call the function with a number between 1 and 100.
# ============================================================

import random

def comparer_nombre(nombre_utilisateur):
    # Generate a random integer between 1 and 100
    nombre_aleatoire = random.randint(1, 100)
    # Compare the two numbers
    if nombre_utilisateur == nombre_aleatoire:
        print("Succès !")
    else:
        print(f"Échec ! Votre nombre : {nombre_utilisateur}, Nombre aléatoire : {nombre_aleatoire}")

# Call the function with a number between 1 and 100
comparer_nombre(50)


# ============================================================
# Exercise 6
# Instructions:
# Create a function to describe a shirt's size and message,
# with default values.
# Key Python Topics: Functions with parameters and default values,
# keyword arguments.
#
# Step 1: Define a function called make_shirt() with two
#         parameters: size and text.
# Step 2: Display a sentence summarizing the shirt's size and message.
# Step 3: Call the function.
# Step 4: Modify the function so that size defaults to "large"
#         and text defaults to "I love Python".
# Step 5: Call make_shirt() with default values, with medium size,
#         and with a custom message.
# Step 6 (Bonus): Call make_shirt() using keyword arguments.
# ============================================================

def creer_tshirt(taille="large", texte="I love Python"):
    # Print a summary of the shirt's size and message
    print(f"La taille du t-shirt est {taille} et le texte est : {texte}.")

# Call with default values (large shirt, default message)
creer_tshirt()
# Call with medium size and default message
creer_tshirt("medium")
# Call with custom size and custom message
creer_tshirt("small", "Vive la Côte d'Ivoire !")
# Bonus: Call using keyword arguments
creer_tshirt(taille="XL", texte="Hello Abidjan!")


# ============================================================
# Exercise 7
# Instructions:
# Generate a random temperature and provide advice based on the range.
# Key Python Topics: Functions, conditionals, random numbers,
# floating-point numbers (Bonus), handling seasons (Bonus).
#
# Step 1: Create get_random_temp() that returns a random integer
#         between -10 and 40 degrees Celsius.
# Step 2: Create main(). Inside it, call get_random_temp(),
#         store the result and print a friendly message.
# Step 3: Provide advice based on the temperature:
#         Below 0°C       → "Brrr, that's freezing!"
#         0°C to 16°C     → "Quite chilly!"
#         16°C to 23°C    → "Nice weather."
#         24°C to 32°C    → "A bit warm, stay hydrated."
#         32°C to 40°C    → "It's really hot!"
# Step 4 (Bonus): Use random.uniform() for floating-point temps.
# Step 5 (Bonus): Ask the user for a month (1-12), determine the
#                 season, and return season-specific temperatures.
# ============================================================

import random

def obtenir_temperature_aleatoire():
    # Bonus: return a random floating-point number between -10 and 40
    return random.uniform(-10, 40)

def principale():
    # Call get_random_temp() and store the temperature
    temperature = obtenir_temperature_aleatoire()
    print(f"La température en ce moment est de {temperature:.1f} degrés Celsius.")

    # Provide advice based on the temperature range
    if temperature < 0:
        # Below 0°C
        print("Brrr, il gèle ! Couvrez-vous bien.")
    elif temperature < 16:
        # Between 0°C and 16°C
        print("Il fait frais ! N'oubliez pas votre veste.")
    elif temperature < 24:
        # Between 16°C and 23°C
        print("Temps agréable.")
    elif temperature < 32:
        # Between 24°C and 32°C
        print("Un peu chaud, pensez à vous hydrater.")
    else:
        # Between 32°C and 40°C
        print("Il fait très chaud ! Restez au frais.")

# Call the main function
principale()


# ============================================================
# Exercise 8
# Instructions:
# Key Python Topics: Loops, lists, string formatting.
#
# - Write a loop that asks the user to enter pizza toppings one by one.
# - Stop the loop when the user types 'quit'.
# - For each topping entered, print "Adding [topping] to your pizza."
# - After exiting the loop, print all toppings and the total cost.
# - Base price is $10, and each topping adds $2.50.
# ============================================================

# Base price of the pizza
PRIX_DE_BASE = 10
# Price added per topping
PRIX_PAR_GARNITURE = 2.5

garnitures = []

# Loop to collect toppings one by one
while True:
    garniture = input("Ajoutez une garniture (ou 'quitter' pour terminer) : ")
    # Stop the loop when the user types 'quitter'
    if garniture.lower() == 'quitter':
        break
    # Store the topping and print a confirmation message
    garnitures.append(garniture)
    print(f"Ajout de {garniture} à votre pizza.")

# Print all toppings and the total price
print(f"\nVos garnitures : {', '.join(garnitures)}")
prix_total = PRIX_DE_BASE + len(garnitures) * PRIX_PAR_GARNITURE
print(f"Prix total : {prix_total}$")