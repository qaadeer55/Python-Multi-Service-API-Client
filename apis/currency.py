import requests


def get_currency_rates():

    url = "https://open.er-api.com/v6/latest/USD"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        currency = {
            "base_currency": data["base_code"],
            "PKR": data["rates"]["PKR"],
            "EUR": data["rates"]["EUR"],
            "GBP": data["rates"]["GBP"],
            "JPY": data["rates"]["JPY"]
        }

        return currency

    except requests.exceptions.Timeout:
        print("Currency API Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Currency API Error: Internet connection failed.")

    except requests.exceptions.HTTPError as error:
        print(f"Currency API HTTP Error: {error}")

    except KeyError as error:
        print(f"Currency API JSON Error: Missing field {error}")

    except ValueError:
        print("Currency API Error: Invalid JSON response.")

    return None