import json
import requests
import csv
import urllib.request


def get_college_info(collegename):

    idnumber = dict()
    with open("unitid.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for line in reader:
            unitid = line[0]
            name = line[1]
            idnumber[name] = unitid

    url = "https://www.tuitiontracker.org/school.html?unitid=164580"
    api_endpoint = f"https://www.tuitiontracker.org/data/school-data-09042019/"
    response = requests.get(f"{api_endpoint}{idnumber[collegename]}.json").json()
    return response

def get_location(collegename):
    response = get_college_info(collegename)
    city = response['city']
    state = response['state']
    location = str(city + ", " + state)
    return location

def get_sticker_price(collegename):
    response = get_college_info(collegename)
    tuition = response["yearly_data"][0]
    sticker_price = tuition["price_instate_oncampus"]
    return sticker_price


def get_lat(collegename):
    response = get_college_info(collegename)
    lat = response["lat"]
    return lat


def get_lon(collegename):
    response = get_college_info(collegename)
    lon = response["lon"]
    return lon


def get_acceptance_rate(collegename):
    response = get_college_info(collegename)
    accept = response["enrollment"]["perc_admitted"]
    return accept

def get_grad_rate(collegename):
    response = get_college_info(collegename)
    grad_rate = response['yearly_data'][3]['grad_rate_bachelors_6years_total']
    return grad_rate

def get_current_temp(collegename):
    lat = get_lat(collegename)
    lon = get_lon(collegename)
    APIKEY = "2dc51f29cd9c9ea11bce898ebee754a9"
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)

    main_data = response_data["main"]
    current_temp = main_data["temp"] * 9 / 5 - 459.67
    return current_temp

def get_total_enroll(collegename):
    response = get_college_info(collegename)
    total_enroll = response['enrollment']['total_enrollment']
    return total_enroll

def main():
    collegename1 = 'Babson College'
    collegename2 = "Pennsylvania State University-Main Campus"
    # print(get_current_temp(collegename))
    # print(get_sticker_price(collegename))
    # print(get_acceptance_rate(collegename), "%")
    print(get_location(collegename1))
    print(get_grad_rate(collegename1))
    print(get_total_enroll(collegename1))

    print(get_location(collegename2))
    print(get_grad_rate(collegename2))
    print(get_total_enroll(collegename2))

if __name__ == "__main__":
    main()
