from typing import TextIO, List, Dict, Union

MIN_YR = "min_year"
MAX_YR = "max_year"

CONSTANT = 0
INDEX = 1
BRAND = ["brand", 0]
MODEL = ["model", 1]
YEAR = ["year", 2]
POWER = ["power", 3]
DRIVETRAIN = ["drivetrain", 4]
FORM_FACTOR = ["form_factor", 5]
PRICE = ["price", 6]
EV_TYPE = ["ev_type", 7]
SAFETY_RATING = ["safety_rating", 8]
RANGE = ["range", 9]
CHARGING = ["charging", 10]
FEATURES = ["features", 11]

def clean_data(input_file: TextIO) -> Dict:
    input_file.readline().strip().split(",") # First row

    cars = {}
    for info in database.readlines():
        info_list = info.split(",")
        for index in range(len(info_list)):
            info_list[index] = info_list[index].strip()

        cars[info_list[MODEL[INDEX]]] = {
            BRAND[CONSTANT]: info_list[BRAND[INDEX]],
            YEAR[CONSTANT]: int(info_list[YEAR[INDEX]]),
            POWER[CONSTANT]: info_list[POWER[INDEX]],
            DRIVETRAIN[CONSTANT]: info_list[DRIVETRAIN[INDEX]],
            FORM_FACTOR[CONSTANT]: info_list[FORM_FACTOR[INDEX]],
            PRICE[CONSTANT]: info_list[PRICE[INDEX]],
            EV_TYPE[CONSTANT]: info_list[EV_TYPE[INDEX]],
            SAFETY_RATING[CONSTANT]: info_list[SAFETY_RATING[INDEX]],
            RANGE[CONSTANT]: info_list[RANGE[INDEX]],
            CHARGING[CONSTANT]: (info_list[CHARGING[INDEX]] == True),
            FEATURES[CONSTANT]: info_list[FEATURES[INDEX]]
        }
    return cars

def search_data(car_data: Dict, search: List[List]) -> List[str]:
    # specification = [
    #     [price, {min, max}],
    #     [form_factor, {type, seats}]
    #     ]
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

def get_models_from_years(car_data: Dict, years: Dict[str, int]) -> List[str]:
    # years = {MIN_YEAR, MAX_YEAR}
    models_from_search_years = []

    for model in car_data:
        model_data = car_data[model]
        if years[MIN_YR] <= model_data[YEAR[CONSTANT]] <= years[MAX_YR]:
                models_from_search_years.append(model)
    
    return models_from_search_years



database = open("ev_database.csv")
data = clean_data(database)
# print(data)
# print(get_models_from_brands(data, "Audi"))
# print(get_models_from_years(data, {MIN_YR: 2020, MAX_YR: 2020}))