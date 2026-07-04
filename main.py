import json

from apis.weather import get_weather
from apis.currency import get_currency_rates
from apis.crypto import get_crypto_prices


weather = get_weather()
currency = get_currency_rates()
crypto = get_crypto_prices()


if weather:
    with open("output/weather.json", "w") as file:
        json.dump(weather, file, indent=4)
    print("Weather data saved successfully.")
else:
    print("Weather data was not saved.")


if currency:
    with open("output/currency.json", "w") as file:
        json.dump(currency, file, indent=4)
    print("Currency data saved successfully.")
else:
    print("Currency data was not saved.")


if crypto:
    with open("output/crypto.json", "w") as file:
        json.dump(crypto, file, indent=4)
    print("Crypto data saved successfully.")
else:
    print("Crypto data was not saved.")


print("\nProject execution completed.")
