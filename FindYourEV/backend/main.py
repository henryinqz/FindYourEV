from typing import TextIO, List, Dict, Union

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
RANGE_CAPACITY = ["range", 9]
FEATURES = ["features", 10]

MIN_YR = "min_year"
MAX_YR = "max_year"

HIGH_POWER = 300
NORMAL_POWER = 150
LOW_POWER = 0

MIN_PRICE = "min_price"
MAX_PRICE = "max_price"

MIN_RATING = "min_rating"
MAX_RATING = "max_rating"

MIN_RANGE = "min_range"
MAX_RANGE = "max_range"

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
            POWER[CONSTANT]: int(info_list[POWER[INDEX]]),
            DRIVETRAIN[CONSTANT]: info_list[DRIVETRAIN[INDEX]],
            FORM_FACTOR[CONSTANT]: info_list[FORM_FACTOR[INDEX]],
            PRICE[CONSTANT]: int(info_list[PRICE[INDEX]]),
            EV_TYPE[CONSTANT]: info_list[EV_TYPE[INDEX]],
            SAFETY_RATING[CONSTANT]: float(info_list[SAFETY_RATING[INDEX]]),
            RANGE_CAPACITY[CONSTANT]: int(info_list[RANGE_CAPACITY[INDEX]]),
            FEATURES[CONSTANT]: info_list[FEATURES[INDEX]]
        }
    return cars

def search_data(car_data: Dict, search: List[List]) -> List[str]:
    '''
    Return a list of car models  that match search query.

    search = [
        [brand, ["Audi", "Honda"]],
        [year, {MIN_YEAR, MAX_YEAR}],
        [price, {MIN_YR, MAX_YR}],
        [power, [HIGH_POWER, NORMAL_POWER, LOW_POWER]],
        [drivetrain, ["AWD", "FWD", "RWD"]],
        [form_factors, ["SUV", "Sedan"]],
        [years, {MIN_PRICE, MAX_PRICE}],
        [ev_type, ["PHEV", "BEV", "HFCV"]],
        [safety_rating, {MIN_RATING, MAX_RATING}],
        [range_capacity, {MIN_RANGE, MAX_RANGE}]
        ]
    ''' 
    car_models = list(car_data.keys())

    for specification, query in search:
        if specification == BRAND[CONSTANT]:
            car_models = update_car_models(get_models_from_brands(car_data, query), car_models)
        elif specification == YEAR[CONSTANT]:
            car_models = update_car_models(get_models_from_years(car_data, query), car_models)     
        #elif specification == POWER[CONSTANT]:

        # elif specification == DRIVETRAIN[CONSTANT]:

        # elif specification == FORM_FACTOR[CONSTANT]:

        # elif specification == PRICE[CONSTANT]:

        # elif specification == EV_TYPE[CONSTANT]:

        elif specification == SAFETY_RATING[CONSTANT]:
            car_models = update_car_models(get_models_from_safety_rating(car_data, query), car_models)

        elif specification == RANGE_CAPACITY[CONSTANT]:
            car_models = update_car_models(get_models_from_range(car_data, query), car_models)
    return car_models

def update_car_models(cars_with_search_query: List[str], car_models: List[str]) -> List[str]:
    searched_models = car_models.copy()

    for car in car_models:
        if car not in cars_with_search_query:
            searched_models.remove(car)

    return searched_models # Change to searched_models.copy() if there are any bugs!

def get_models_from_brands(car_data: Dict, brands: List[str]) -> List[str]:
    '''
    brands = ["Audi", "Honda"]
    '''
    models_from_search_brands = []

    for model in car_data:
        model_data = car_data[model]
        if model_data["brand"] in brands:
                models_from_search_brands.append(model)
    
    return models_from_search_brands

def get_models_from_years(car_data: Dict, years: Dict[str, int]) -> List[str]:
    '''
    years = {MIN_YEAR, MAX_YEAR}
    '''
    models_from_search_years = []

    for model in car_data:
        model_data = car_data[model]
        if years[MIN_YR] <= model_data[YEAR[CONSTANT]] <= years[MAX_YR]:
                models_from_search_years.append(model)
    
    return models_from_search_years

def get_models_from_power(car_data: Dict, power: int) -> List[str]:
    '''
    power = HIGH_POWER/NORMAL_POWER/LOW_POWER
    '''
    pass

def get_models_from_drivetrain(car_data: Dict, drivetrain: List[str]) -> List[str]:
    '''
    drivetrain = ["AWD", "FWD", "RWD"]
    '''
    pass

def get_models_from_form_factor(car_data: Dict, form_factors: List[str]) -> List[str]:
    '''
    form_factors = ["SUV", "Sedan"]
    '''
    pass

def get_models_from_price(car_data: Dict, price: Dict[str, int]) -> List[str]:
    '''
    years = {MIN_PRICE, MAX_PRICE}
    '''
    pass

def get_models_from_ev_type(car_data: Dict, ev_type: List[str]) -> List[str]:
    '''
    ev_type = ["PHEV", "BEV", "HFCV"]
    '''
    pass

def get_models_from_safety_rating(car_data: Dict, safety_rating: Dict[str, int]) -> List[str]:
    '''
    safety_rating = {MIN_RATING, MAX_RATING}
    '''
    models_from_search_safety = []
    
    for model in car_data:
        model_data = car_data[model]
        if safety_rating[MIN_RATING] <= model_data[SAFETY_RATING[CONSTANT]] <= safety_rating[MAX_RATING]:
            models_from_search_safety.append(model)
    
    return models_from_search_safety

def get_models_from_range(car_data: Dict, range_capacity: Dict[str, int]) -> List[str]:
    '''
    range_capacity = {MIN_RANGE, MAX_RANGE}
    '''
    models_from_search_range = []

    for model in car_data:
        model_data = car_data[model]
        if range_capacity[MIN_RANGE] <= model_data[RANGE_CAPACITY[CONSTANT]] <= range_capacity[MAX_RANGE]:
            models_from_search_range.append(model)
    
    return models_from_search_range

def get_models_from_features(car_data: Dict, years: Dict[str, int]) -> List[str]:
    '''
    
    '''
    pass


database = open("FindYourEV\ev_database.csv")
data = clean_data(database)
# print(data)
# print(get_models_from_brands(data, ["Audi", "Honda"]))
# print(get_models_from_years(data, {MIN_YR: 2020, MAX_YR: 2020}))
print(search_data(data, [
    [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]]])
    )
print(search_data(data, [
    [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}]])
    )
print(search_data(data, [
    [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    [RANGE_CAPACITY[CONSTANT], {MIN_RANGE: 300, MAX_RANGE: 400}]])
    )
print(search_data(data, [
    [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}], 
    [SAFETY_RATING[CONSTANT], {MIN_RATING: 5, MAX_RATING: 5}]])
    )