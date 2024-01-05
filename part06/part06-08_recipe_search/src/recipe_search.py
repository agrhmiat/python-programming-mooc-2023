# Write your solution here

def get_recipe_data(filename: str) -> list:
    recipe_data = []
    with open(filename) as recipe_file:
        for line in recipe_file:
            recipe_data.append(line.strip())
    recipe_data.insert(0, "")
    return recipe_data

def get_recipes(filename: str) -> list:
    recipes = []
    recipe_data = get_recipe_data(filename)
    for i in range(len(recipe_data)):
        recipe = {}
        if recipe_data[i] == "":
            recipe["name"] = recipe_data[i+1]
            recipe["cooking time"] = int(recipe_data[i+2])
            ingredients = []
            j = i + 3
            while recipe_data[j] != "":
                ingredients.append(recipe_data[j])
                if j == len(recipe_data)-1:
                    break
                j += 1
            recipe["ingredients"] = ingredients
            recipes.append(recipe)
    return recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = get_recipes(filename)
    recipe_details = []
    for recipe in recipes:
        for ingredient_name in recipe["ingredients"]:
            if ingredient in ingredient_name:
                recipe_name = recipe["name"]
                cooking_time = recipe["cooking time"]
                recipe_details.append(f"{recipe_name}, preparation time {cooking_time} min")
                break
    return recipe_details

def search_by_time(filename: str, prep_time: int) -> list:
    recipes = get_recipes(filename)
    recipe_details = []
    for recipe in recipes:
        if recipe["cooking time"] <= prep_time:
            recipe_name = recipe["name"]
            cooking_time = recipe["cooking time"]
            recipe_details.append(f"{recipe_name}, preparation time {cooking_time} min")
    return recipe_details

def search_by_name(filename: str, word: str) -> list:
    recipes = get_recipes(filename)
    recipe_names = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            recipe_names.append(recipe["name"])
    return recipe_names

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes2.txt", "fish")
    for recipe in found_recipes:
        print(recipe)
