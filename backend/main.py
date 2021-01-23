import data_process as data_process
from constants import *

if __name__ == "__main__":
    database = open("ev_database.csv", "r")
    data = data_process.clean_data(database)
    # print(data)

    # Test calls
    # temp_data = data_process.search_data(data, [[BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]]])
    # print(temp_data)
    # print(data_process.get_random_cars_from_search_data(temp_data, 3))

    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [POWER[CONSTANT], [HIGH_POWER]]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [EV_TYPE[CONSTANT], ["BEV", "HFCV"]]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [DRIVETRAIN[CONSTANT], ["FWD"]]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [DRIVETRAIN[CONSTANT], ["FWD"]],
    #     [FORM_FACTOR[CONSTANT], ["Compact", "Sedan", "Subcompact", "SUV"]]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [RANGE_CAPACITY[CONSTANT], {MIN_RANGE: 300, MAX_RANGE: 400}]])
    #     )
    # print(data_process.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}], 
    #     [SAFETY_RATING[CONSTANT], {MIN_RATING: 5, MAX_RATING: 5}]])
    #     )