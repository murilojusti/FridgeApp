from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)


def menu():
    while True:
        print("========== MENU ==========")
        print("1. Add Ingredients")
        print("2. Generate Recipe")
        print("3. End Application")
        print("=========================")
        op_menu = int(input("Insert an option: "))

        match op_menu:
            case 1:
                ingredients = add_ingredient()
            case 2:
                generate_recipe(ingredients)
            case 3:
                break


def add_ingredient():
    ingredients = []
    print("Type '.' to stop adding ingredients")
    while "." not in ingredients:
        ingredients.append(input("Insert an ingredient: "))
    ingredients.remove(".")
    return ingredients


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
                    "simply inform the user with the following message: 'Invalid ingredients,' and nothing else. "
                    "It is not necessary to use all the ingredients; you are a fridge system, so you don’t need to 'force' "
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