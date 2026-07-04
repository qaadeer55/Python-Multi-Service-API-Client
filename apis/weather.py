import requests


def get_weather():

    url = "https://wttr.in/Karachi?format=j1"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        weather = {
            "city": "Karachi",
            "temperature_c": data["current_condition"][0]["temp_C"],
            "humidity": data["current_condition"][0]["humidity"],
            "weather": data["current_condition"][0]["weatherDesc"][0]["value"],
            "wind_speed_kmph": data["current_condition"][0]["windspeedKmph"]
        }

        return weather

    except requests.exceptions.Timeout:
        print("Weather API Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Weather API Error: Internet connection failed.")

    except requests.exceptions.HTTPError as error:
        print(f"Weather API HTTP Error: {error}")

    except KeyError as error:
        print(f"Weather API JSON Error: Missing field {error}")

    except ValueError:
        print("Weather API Error: Invalid JSON response.")

    return None