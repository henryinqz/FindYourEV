from typing import TextIO, List, Dict, Union

BRAND = 0
MODEL = 1
YEAR = 2
POWER = 3
DRIVETRAIN = 4
FORM_FACTOR = 5
PRICE = 6
EV_TYPE = 7
SAFETY_RATING = 8
RANGE = 9
CHARGING = 10
FEATURES = 11

def clean_data(input_file: TextIO) -> Dict:
    factors = input_file.readline().strip().split(",")

    cars = {}
    for info in database.readlines():
        info_list = info.split(",")
        for index in range(len(info_list)):
            info_list[index] = info_list[index].strip()

        cars[info_list[MODEL]] = {
            "brand": info_list[BRAND],
            "year": info_list[YEAR],
            "power": info_list[POWER],
            "drivetrain": info_list[DRIVETRAIN],
            "form_factor": info_list[FORM_FACTOR],
            "price": info_list[PRICE],
            "ev_type": info_list[EV_TYPE],
            "safety_rating": info_list[SAFETY_RATING],
            "range": info_list[RANGE],
            "charging": (info_list[CHARGING] == True),
            "features": info_list[FEATURES]
        }
    return cars

def search_data(car_data: Dict, search: List[List]) -> List[str]:
    # specification = [[price, {min, max}], [form_factor, {type, seats}]]
    # return list of model names that match search query
    searched_data = []
    for specification, query in search:
        if specification == BRAND:
            brands = get_models_from_brands(car_data, query)
            if brands not in searched_data:
                searched_data.append(brands)
        # elif specification == YEAR:

        # elif specification == POWER:

        # elif specification == DRIVETRAIN:

        # elif specification == FORM_FACTOR:

        # elif specification == PRICE:

        # elif specification == EV_TYPE:

        # elif specification == SAFETY_RATING:

        # elif specification == RANGE:

        # elif specification == CHARGING:

        # elif specification == FEATURES:

        
    return searched_data

def get_models_from_brands(car_data: Dict, brands: List[str]) -> List[str]:
    models_from_search_brands = []

    for model in car_data:
        model_data = car_data[model]
        if model_data["brand"] in brands:
                models_from_search_brands.append(model)
    
    return models_from_search_brands



database = open("ev_database.csv")
data = clean_data(database)
# print(data)
# print(get_models_from_brands(data, "Audi"))