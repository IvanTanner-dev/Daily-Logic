def get_allergen_friendly_meals(meals, allergens):
    # convert to a set for faster lookup
    avoid_set = set(allergens)

    return [name for name, allergens in meals if avoid_set.isdisjoint(allergens)]