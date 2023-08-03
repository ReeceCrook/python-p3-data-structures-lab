spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    i = 0
    spicy_foods_names = []
    while i < len(spicy_foods):
        spicy_foods_names.append(spicy_foods[i]["name"])
        i += 1
    return spicy_foods_names

def get_spiciest_foods(spicy_foods):
    i = 0
    hottest_spicy_foods = []
    while i < len(spicy_foods):
        if spicy_foods[i]["heat_level"] > 5:
            hottest_spicy_foods.append(spicy_foods[i])
            i+=1
        else:
            i+=1
    return hottest_spicy_foods

def print_spicy_foods(spicy_foods):
    i = 0
    while i < len(spicy_foods):
        print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}")
        i+=1

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    i = 0
    while i < len(spicy_foods):
        if spicy_foods[i]["cuisine"] == cuisine:
            return spicy_foods[i]
        else:
            i+=1
        

def print_spiciest_foods(spicy_foods):
    i = 0
    while i < len(spicy_foods):
        if spicy_foods[i]["heat_level"] > 5:
            print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}")
            i+=1
        else:
            i+=1

def get_average_heat_level(spicy_foods):
    i = 0
    heat_levels = []
    while i < len(spicy_foods):
        heat_levels.append(spicy_foods[i]["heat_level"])
        i+=1
    average_heat = sum(heat_levels) / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
