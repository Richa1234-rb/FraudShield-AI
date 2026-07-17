from datetime import datetime


MERCHANTS = {
    "amazon": 1,
    "flipkart": 2,
    "apple": 3,
    "google": 4,
    "paypal": 5,
    "crypto": 6
}


LOCATIONS = {
    "bhubaneswar": 1,
    "delhi": 2,
    "mumbai": 3,
    "bangalore": 4,
    "kolkata": 5,
    "russia": 6,
    "usa": 7
}


def encode_merchant(name: str):

    return MERCHANTS.get(
        name.lower(),
        0
    )


def encode_location(location: str):

    return LOCATIONS.get(
        location.lower(),
        0
    )


def current_hour():

    return datetime.now().hour