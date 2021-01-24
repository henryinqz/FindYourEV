import data_process as dp
from constants import *

if __name__ == "__main__":
    database = open("ev_database.csv", "r")
    data = dp.clean_data(database)
    # print(data)

    # Test calls
    temp_data = dp.search_data(data, [[BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]]])
    print(temp_data)
    print(dp.get_data_from_model(data, dp.get_random_cars_from_search_data(temp_data, 5)))

    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}]])
    #     )
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [POWER[CONSTANT], [HIGH_POWER]]])
    #     )

    # print(dp.get_data_from_model(data, dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}]])
    #     ))
    # print(dp.get_data_from_model(data, dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [POWER[CONSTANT], [HIGH_POWER]]])
    #     ))


    
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [EV_TYPE[CONSTANT], ["BEV", "HFCV"]]])
    #     )
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [DRIVETRAIN[CONSTANT], ["FWD"]]])
    #     )
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [DRIVETRAIN[CONSTANT], ["FWD"]],
    #     [FORM_FACTOR[CONSTANT], ["Compact", "Sedan", "Subcompact", "SUV"]]])
    #     )
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}],
    #     [RANGE_CAPACITY[CONSTANT], {MIN_RANGE: 300, MAX_RANGE: 400}]])
    #     )
    # print(dp.search_data(data, [
    #     [BRAND[CONSTANT], ["Audi", "Honda", "Toyota"]], 
    #     [YEAR[CONSTANT], {MIN_YR: 2020, MAX_YR: 2021}], 
    #     [SAFETY_RATING[CONSTANT], {MIN_RATING: 5, MAX_RATING: 5}]])
    #     )