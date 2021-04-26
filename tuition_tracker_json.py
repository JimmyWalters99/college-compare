import json
import requests
import csv
import urllib.request
import difflib
from config import APIKEY


def get_college_info(collegename):
    """retrives and loads in data about a specific college"""
    idnumber = dict()
    with open("unitid.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            unitid = line[0]
            name = line[1]
            idnumber[name] = unitid

    api_endpoint = f"https://www.tuitiontracker.org/data/school-data-09042019/"
    response = requests.get(f"{api_endpoint}{idnumber[collegename]}.json").json()
    return response


def private_or_public(collegename):
    """takes a college name and returns what type of institution is it, public, private for profit, or private non-profit"""
    response = get_college_info(collegename)
    schooltype = response["control"]
    private_or_public = ""
    if schooltype == 1:
        private_or_public = "Public"
    if schooltype == 2:
        private_or_public = "Private, Non-Profit"
    else:
        private_or_public = "Private, For-Proft"
    return private_or_public


def get_location(collegename):
    """takes a college name and returns the city and state it is located in"""
    response = get_college_info(collegename)
    city = response["city"]
    state = response["state"]
    location = str(city + ", " + state)
    return location


def get_sticker_price(collegename):
    """takes a college name and returns the sticker price of that college, i.e cost of attendance without any financial aid"""
    response = get_college_info(collegename)
    tuition = response["yearly_data"][0]
    sticker_price = tuition["price_instate_oncampus"]
    return sticker_price


def get_lat(collegename):
    """takes a college name and returns a latitude coordinate"""
    response = get_college_info(collegename)
    lat = response["lat"]
    return lat


def get_lon(collegename):
    """takes a college name and returns a longitude coordinate"""
    response = get_college_info(collegename)
    lon = response["lon"]
    return lon


def get_acceptance_rate(collegename):
    """take a college name and returns the acceptance rate"""
    response = get_college_info(collegename)
    accept = response["enrollment"]["perc_admitted"]
    return accept


def get_grad_rate(collegename):
    """takes a college name and returns the graduation rate"""
    response = get_college_info(collegename)
    grad_rate = response["yearly_data"][3]["grad_rate_bachelors_6years_total"]
    return grad_rate


def get_weather_info(collegename):
    """loads in weather data based on a college name"""
    lat = get_lat(collegename)
    lon = get_lon(collegename)
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    return response_data


def get_current_temp(collegename):
    """takes a college name and returns the current temperature in farienheit"""
    response = get_weather_info(collegename)
    main_data = response["main"]
    current_temp = main_data["temp"] * 9 / 5 - 459.67
    return current_temp


def get_current_weather(collegename):
    """takes a college name and returns the current weather conditions"""
    response = get_weather_info(collegename)
    current_weather = response["weather"][0]["main"]
    return current_weather


def get_total_enroll(collegename):
    """takes a college name and returns the total number of undergraduate students"""
    response = get_college_info(collegename)
    total_enroll = response["enrollment"]["total_enrollment"]
    return total_enroll


def get_male_ratio(collegename):
    """takes a college name and returns the percentage of students who are male"""
    response = get_college_info(collegename)
    male_enroll = response["enrollment"]["total_men"]
    total_enroll = get_total_enroll(collegename)
    return male_enroll / total_enroll


def get_female_ratio(collegename):
    """takes a college name and returns the percentage of students who are female"""
    response = get_college_info(collegename)
    female_enroll = response["enrollment"]["total_women"]
    total_enroll = get_total_enroll(collegename)
    return female_enroll / total_enroll


def get_website(collegename):
    """take a college name and returns the url for their website"""
    response = get_college_info(collegename)
    website = response["website"]
    return website


def name_check(collegename):
    """Checks the name of the user inputted college and returns if it is a valid name in the list,
    and if not, returns up to 5 suggesttions of valid college names which the user may have meant"""
    valid = False
    with open("unitid.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        namelist = []
        for line in reader:
            name = line[1]
            namelist.append(name)
    for name in namelist:
        if name == collegename:
            valid = True
    if not valid:
        suggestions = difflib.get_close_matches(collegename, namelist, 5)
        if len(suggestions) > 0:
            return suggestions
        else:
            return valid
    else:
        return valid


def stat_list():
    res = [
        private_or_public(),
        get_location(),
        get_sticker_price(),
        get_acceptance_rate(),
        get_grad_rate(),
        get_current_weather(),
        get_total_enroll(),
        get_male_ratio(),
        get_female_ratio(),
        get_website(),
    ]
    return res


def main():
    collegename1 = "Babson College"
    collegename2 = "Pennsylvania State University-Main Campus"
    invalidname = ""
    # print(get_current_temp(collegename1))
    # print(get_sticker_price(collegename))
    # print(get_acceptance_rate(collegename), "%")
    # print(get_location(collegename1))
    # print(get_grad_rate(collegename1))
    # print(get_total_enroll(collegename1))

    print(get_location(collegename2))
    print(get_grad_rate(collegename2))
    print(get_total_enroll(collegename2))
    print(get_current_weather(collegename2))


if __name__ == "__main__":
    main()
