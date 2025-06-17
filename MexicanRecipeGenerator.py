import random  # Import the random module to enable random selection from lists

# ----------------------------
# Dictionary of recipes
# ----------------------------
# This dictionary stores Mexican recipes by meat type.
# Each key is a meat type ("chicken", "pork") mapped to a list of recipes.
# Each recipe is a dictionary containing:
# - 'name': the name of the recipe
# - 'ingredients': list of ingredients needed
# - 'instructions': step by step cooking directions
recipes = {
    "chicken": [
        {
            "name": "Chicken Tinga",
            "ingredients": [
                "2 cups shredded chicken",
                "1 onion, sliced",
                "2 cloves garlic",
                "3 tomatoes",
                "2 chipotle peppers in adobo",
                "1 tbsp olive oil",
                "Salt and pepper to taste"
            ],
            "instructions": "Blend tomatoes, chipotle, and garlic. Saute onion in oil, add chicken and sauce. Simmer for 15 minutes. Serve on tostadas."
        },
        {
            "name": "Pollo Asado",
            "ingredients": [
                "2 chicken thighs",
                "1/4 cup orange juice",
                "1/4 cup lime juice",
                "2 cloves garlic, minced",
                "1 tsp cumin",
                "1 tsp paprika",
                "Salt and pepper"
            ],
            "instructions": "Marinate chicken for 2+ hours. Grill until cooked through. Serve with rice and salsa."
        },
        {
            "name": "Chicken Enchiladas Verde",
            "ingredients": [
                "2 cups cooked, shredded chicken",
                "8 corn tortillas",
                "1 cup green enchilada sauce",
                "1/2 cup shredded cheese",
                "1/4 cup sour cream"
            ],
            "instructions": "Fill tortillas with chicken, roll up, place in baking dish, pour sauce, top with cheese. Bake at 375°F for 20 min."
        },
        {
            "name": "Chicken Mole",
            "ingredients": [
                "2 cups shredded chicken",
                "1/2 cup mole sauce",
                "1 tbsp sesame seeds",
                "1 tbsp oil",
                "Corn tortillas"
            ],
            "instructions": "Heat mole sauce with oil, stir in chicken. Simmer for 10 minutes. Serve with tortillas and sesame seeds."
        }
    ],

    "pork": [
        {
            "name": "Carnitas",
            "ingredients": [
                "2 lbs pork shoulder",
                "1/2 cup orange juice",
                "1/4 cup lime juice",
                "1 onion, chopped",
                "2 cloves garlic",
                "1 tsp oregano"
            ],
            "instructions": "Slow cook all ingredients for 4 hours. Shred pork and crisp in a hot pan. Serve in tacos."
        },
        {
            "name": "Al Pastor",
            "ingredients": [
                "2 lbs pork shoulder, thinly sliced",
                "3 guajillo chilies",
                "1/2 cup pineapple juice",
                "1/4 cup vinegar",
                "2 garlic cloves",
                "1 tsp cumin"
            ],
            "instructions": "Blend marinade, coat pork, marinate overnight. Grill or roast, serve with pineapple and cilantro."
        },
        {
            "name": "Chilorio",
            "ingredients": [
                "1 lb pork",
                "3 ancho chiles",
                "2 cloves garlic",
                "1/2 tsp cumin",
                "1/4 cup vinegar"
            ],
            "instructions": "Boil pork until tender. Blend chilies, garlic, cumin, vinegar. Saute pork in sauce. Serve with tortillas."
        },
        {
            "name": "Puerco en Salsa Verde",
            "ingredients": [
                "1 lb pork chunks",
                "6 tomatillos",
                "2 jalapenos",
                "1/2 onion",
                "1 clove garlic"
            ],
            "instructions": "Boil tomatillos, jalapenos, onion, garlic. Blend into sauce. Brown pork, simmer in sauce for 30 mins. Serve with rice."
        }
    ],

    "beef": [
        {
            "name": "Carne Asada",
            "ingredients": [
                "1 lb flank steak",
                "1/4 cup lime juice",
                "2 cloves garlic",
                "1 tsp cumin",
                "1/2 tsp chili powder"
            ],
            "instructions": "Marinate steak for 2 hours. Grill to desired tenderness. Slice thin and serve in tacos."
        },
        {
            "name": "Barbacoa",
            "ingredients": [
                "2 lbs beef chuck roast",
                "3 chipotle peppers",
                "1/2 cup beef broth",
                "2 tbsp apple cider vinegar",
                "2 cloves garlic"
            ],
            "instructions": "Slow cook all ingredients for about 6-8 hours. Shred beef and serve in tacos or burritos."
        },
        {
            "name": "Picadillo",
            "ingredients": [
                "1 lb ground beef",
                "1 potato, diced",
                "1/2 onion, chopped",
                "2 cloves garlic",
                "1/2 cup tomato sauce",
                "1/4 cup peas"
            ],
            "instructions": "Cook beef and onion. Add potato, garlic, sauce, peas. Simmer until potatoes are soft. Serve with rice."
        },
        {
            "name": "Beef Empanadas",
            "ingredients": [
                "1 lb ground beef",
                "1/2 onion, chopped",
                "1/2 cup tomato sauce",
                "Empanada dough",
                "1 egg (for brushing)"
            ],
            "instructions": "Cook beef and onion, add sauce. Fill dough, fold and seal. Brush with egg. Bake at 375°F for 20 min."
        }
    ],

    "fish": [
        {
            "name": "Fish Tacos",
            "ingredients": [
                "1 lb white fish (tilapia/cod)",
                "1/4 cup lime juice",
                "1 tsp cumin",
                "1/2 tsp chili powder",
                "Corn tortillas",
                "Cabbage slaw"
            ],
            "instructions": "Marinate fish, grill or pan-fry. Serve in tortillas with slaw and crema."
        },
        {
            "name": "Pescado a la Veracruzana",
            "ingredients": [
                "1 lb white fish fillets",
                "1 tomato, chopped",
                "1/2 onion",
                "1/4 cup olives",
                "1 tbsp capers",
                "2 cloves garlic"
            ],
            "instructions": "Saute onion, garlic, tomato. Add olives and capers. Simmer fish in sauce until cooked through."
        },
        {
            "name": "Ceviche",
            "ingredients": [
                "1 lb white fish, diced",
                "1/2 cup lime juice",
                "1/4 cup diced onion",
                "1/4 cup diced tomato",
                "1 tbsp chopped cilantro"
            ],
            "instructions": "Soak fish in lime juice 1 hr. Add other ingredients. Chill before serving with tostadas or chips."
        },
        {
            "name": "Fish Enchiladas",
            "ingredients": [
                "1 lb cooked white fish",
                "8 corn tortillas",
                "1 cup enchilada sauce",
                "1/2 cup shredded cheese",
                "1/4 cup chopped green onion"
            ],
            "instructions": "Fill tortillas with fish, roll up. Place in dish, pour sauce, top with cheese and onions. Bake at 375°F for 20 min."
        }
    ]
}

# ----------------------------
# Function: get_random_recipe
# ----------------------------
# Purpose: Return a randomly selected recipe dictionary for the meat type.
# Input: meat_type (string) - user input representing a category of meat (like "chicken")
# Output: a single recipe dictionary or None if meat type is invalid
def get_random_recipe(meat_type):
    meat_type = meat_type.lower()  # Convert input to lowercase to handle case differences
    if meat_type in recipes:
        return random.choice(recipes[meat_type])  # Randomly pick one recipe from the list
    else:
        return None  # Return None if meat type is not in dictionary

# ----------------------------
# Function: display_recipe
# ----------------------------
# Purpose: Print out the recipe name, ingredients, and instructions in a user friendly format.
# Input: recipe (dictionary) containing keys 'name', 'ingredients', 'instructions'
# Output: None (prints directly to the console)
def display_recipe(recipe):
    print(f"\n🍽️  {recipe['name']}\n")  # Print recipe title with an emoji for fun
    print("Ingredients:")
    for item in recipe['ingredients']:
        print(f" - {item}")  # Print each ingredient on a new line with a dash
    print("\nInstructions:")
    print(recipe['instructions'])  # Print the step-by-step instructions
    print("\nEnjoy your meal! 🇲🇽")  # Friendly closing message with flag emoji

# ----------------------------
# Main program entry point
# ----------------------------
# Purpose: Run the recipe generator program. Interact with the user,
# ask for a meat type, fetch a random recipe, and display it.
def main():
    print("Welcome to the Mexican Recipe Generator! 🇲🇽🌮")
    print("Available meat types: Chicken, Pork, Beef, Fish")

    while True:  # Loop to allow repeated attempts if user input is invalid
        meat_type = input("Please enter a meat type (or type 'exit' to quit): ").strip().lower()

        if meat_type == 'exit':
            print("Thanks for using the Recipe Generator! Goodbye!")
            break  # Exit the loop and end program

        recipe = get_random_recipe(meat_type)

        if recipe:
            display_recipe(recipe)
            break  # Exit after showing the recipe
        else:
            print("Sorry, we don't have recipes for that meat type. Please try again with Chicken, Pork, Beef, or Fish.")

# Call main to start the program when the file is run
if __name__ == "__main__":
    main()
