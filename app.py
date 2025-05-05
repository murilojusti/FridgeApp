from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

ingredients = [] 

def menu():
    while True:
        print("========== MENU ==========")
        print("1. Add Ingredients")
        print("2. Remove Ingredient")
        print("3. View Ingredients")
        print("4. Generate Recipe")
        print("5. End Application")
        print("=========================")
        op_menu = int(input("Insert an option: "))

        match op_menu:
            case 1:
                ingredients = add_ingredient()
            case 2:
                remove_ingredient(ingredients)
            case 3:
                view_ingredients(ingredients)
            case 4:
                generate_recipe(ingredients)
            case 5:
                break

def sanitize_input(ingredient_input):
    ingredient_input = ingredient_input.lower().strip()
    with open("FOOD.txt", "r", encoding="utf-8") as ingredients_list:
        for ingredient in ingredients_list:
            if ingredient_input == ingredient.strip():
                return True
        return 

def add_ingredient():  
    print("Press Enter to stop adding")
    while "" not in ingredients:
        ingredient_input = input("Insert an ingredient: ")
        if sanitize_input(ingredient_input) == True:
            ingredients.append(ingredient_input)
        else:
            print("Not an ingredient")
    ingredients.remove("")
    return ingredients

def remove_ingredient(ingredients):
    ingredient = input("Name the ingredient to be removed: ")
    if ingredient not in ingredients:
        print("Ingredient not found!")
    else:
        ingredients.remove(ingredient)
        print("Ingredient removed!")

def view_ingredients(ingredients):
    for i in ingredients:
        print(f"- {i}")

def generate_recipe(ingredients):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional chef and an expert in creating delicious recipes. "
                    "Your goal is to create REAL and tasty recipes using ONLY the ingredients provided by the user. "
                    "You MUST NOT add any extra ingredients that are not on the user's list. "
                    "If the ingredients are insufficient for a recipe, try suggesting a simple dish, "
                    "such as a salad, sandwich, or beverage. "
                    "If the ingredients are too limited or are not actual food items for a viable recipe, "
                    "simply inform the user with the following message: 'Invalid ingredients,' or 'Insufficient ingredients' and nothing else. "
                    "It is not necessary to use all the ingredients; you are a fridge system, so you dont need to 'force' "
                    "all the ingredients the user provides into the recipe."
                )
            },
            {
                "role": "user",
                "content": f"Ingredients: {ingredients}"
            }
        ]
    )
    answer = completion.choices[0].message.content
    print(answer)

menu()
