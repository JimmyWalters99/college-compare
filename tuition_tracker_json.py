import json
import requests

url = "https://www.tuitiontracker.org/school.html?unitid=164580"

api_endpoint = f"https://www.tuitiontracker.org/data/school-data-09042019/"
response = requests.get(f"{api_endpoint}{url.split('=')[-1]}.json").json()
tuition = response["yearly_data"][0]
lat = response["lat"]
lon = response["lon"]

print(
    round(tuition["price_instate_oncampus"], 2),
    round(tuition["avg_net_price_0_30000_titleiv_privateforprofit"], 2),
    lat, lon
)
