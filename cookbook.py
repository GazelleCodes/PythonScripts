from recipes import recipes

def list_recipes():
    try:
        if not recipes:
            print("No recipes available.")
            return
        print("Available Recipes:")
        for recipe in recipes:
            print(recipe['name'])
    except Exception as e:
        print("An error occurred while listing recipes:", e)
  
def query_recipe():
    query_name = input("Enter the name of the recipe you want to search for: ")
    
    found_recipes = [recipe for recipe in recipes
            if query_name.lower() in recipe.get("name", "").lower()]
    
    if found_recipes:
        print(f"Found {len(found_recipes)} matching recipes:")
        for recipe in found_recipes:
            ingredients_list = [ingredient.get("name", "").lower()for ingredient in recipe.get("ingredients", [])]
            ingredients_str = ", ".join(ingredients_list)
            print(f"\nRecipe: {recipe.get('name', '')}\nIngredients: {ingredients_str}\nInstructions: {recipe.get('instructions', '')}\n")
    else:
        print("No matching recipes found.")
        
def find_recipes_by_ingredients(available_ingredients):
    matching_recipes = []
    for recipe in recipes:
        recipe_ingredients = [ingredient.get("name", "").lower()for ingredient in recipe.get("ingredients", [])]
        if all(ingredient.lower() in [ri.lower() for ri in recipe_ingredients] for ingredient in available_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes    
    
def main():
    print("Welcome to the Recipe Book CLI Application!")
    
    while True:
        print("\nChoose an option:")
        print("1. List recipes")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            list_recipes()
        elif choice == "2":
            query_recipe()
        elif choice == "3":
            available_ingredients = input("Enter the ingredients you have (comma-separated): ").split(',')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]
            
            matching_recipes = find_recipes_by_ingredients(available_ingredients)
            
            if matching_recipes:
                print("You can make the following recipes:")
                for recipe in matching_recipes:
                    print(recipe['name'])
            else:
                print("No recipes found with the given ingredients.")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
