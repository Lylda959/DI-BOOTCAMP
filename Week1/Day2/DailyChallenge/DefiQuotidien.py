# ============================================================
# Daily Challenge 1: Letter Index Dictionary
# Instructions:
# Create a dictionary that stores the indices (position number)
# of each letter of a word provided by the user.
#
# Step 1 - User Input:
#   Ask the user to enter a word.
#   Store the entered word in a variable.
#
# Step 2 - Create the dictionary:
#   Loop through each character of the word.
#   Check if the character is already a key in the dictionary.
#     - If it is, append the current index to the list of that key.
#     - If it is not, create a new key-value pair in the dictionary.
#   Make sure characters (keys) are strings.
#   Make sure indices (values) are stored in lists.
#
# Step 3 - Expected output:
#   Input "dodo"   → {"d": [0, 2], "o": [1, 3]}
#   Input "froggy" → {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}
# ============================================================

# Ask the user to enter a word
mot = input("Entrez un mot : ")

# Create an empty dictionary to store letter indices
indice_lettres = {}

# Loop through each character and its index in the word
for index, caractere in enumerate(mot):
    # If the character is already a key, append the index to its list
    if caractere in indice_lettres:
        indice_lettres[caractere].append(index)
    # If not, create a new key with a list containing the current index
    else:
        indice_lettres[caractere] = [index]

print(indice_lettres)


# ============================================================
# Daily Challenge 2: Affordable Items
# Instructions:
# Create a program that prints a list of items that can be
# purchased with a given amount of money.
#
# Step 1 - Store the data:
#   You are given a dictionary (items_purchase) where keys are
#   item names and values are their prices as strings with "$".
#   Priority is defined by position in the dictionary (most to least).
#   You are also given a string (wallet) representing your budget.
#
# Step 2 - Clean the data:
#   Remove the dollar sign and commas using Python (not hardcoded).
#
# Step 3 - Determine affordable items:
#   Create a list called basket and add items you can afford.
#   Update your wallet after each purchase.
#   If basket is empty, return the string "Nothing".
#   Otherwise, print the basket list in alphabetical order.
#
# Examples:
#   items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
#   wallet = "$300"
#   Result → ["Bread", "Fertilizer", "Water"]
#
#   items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
#   wallet = "$1"
#   Result → "Nothing"
# ============================================================

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# Clean the wallet: remove "$" and "," then convert to int
budget = int(wallet.replace("$", "").replace(",", ""))

# Create an empty basket list
panier = []

# Loop through each item and its price
for article, prix in items_purchase.items():
    # Clean the price: remove "$" and "," then convert to int
    prix_nettoye = int(prix.replace("$", "").replace(",", ""))

    # If the item is affordable, add it to the basket and update the budget
    if prix_nettoye <= budget:
        panier.append(article)
        budget -= prix_nettoye

# If basket is empty, print "Nothing"
if not panier:
    print("Nothing")
# Otherwise, print the basket in alphabetical order
else:
    print(sorted(panier))