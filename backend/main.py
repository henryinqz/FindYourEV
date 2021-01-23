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

database = open("ev_database.csv")

factors = database.readline().strip().split(",")

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
        "charging": info_list[CHARGING],
        "features": info_list[FEATURES]
    }
print(cars)