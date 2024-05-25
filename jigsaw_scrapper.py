import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.jigsawstack.com/v1/ai/scrape"


headers = {
    "x-api-key": os.getenv("JS_API_KEY"),
    "Content-Type": "application/json",
}
data = {
    "url": "https://www.dbs.com.sg/personal/insurance/endowment-with-protection/retirement-plans/retiresavvy",
    "element_prompts": ["flpweb-legacy"],
}


def get_data():
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        json_response = response.json()
        print(json_response)
        return json_response
    else:
        print(f"Request failed with status code {response.status_code}")


scraped_data = get_data()

# Extract the "text" field
texts = [result["text"] for result in scraped_data["data"][0]["results"]]

# Write the "text" fields into a new text file
with open("output.txt", "w") as txt_file:
    for text in texts:
        txt_file.write(text + "\n")
