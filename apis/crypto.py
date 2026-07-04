import requests


def get_crypto_prices():

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        crypto = {
            "Bitcoin_USD": data["bitcoin"]["usd"],
            "Ethereum_USD": data["ethereum"]["usd"],
            "Solana_USD": data["solana"]["usd"]
        }

        return crypto

    except requests.exceptions.Timeout:
        print("Crypto API Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Crypto API Error: Internet connection failed.")

    except requests.exceptions.HTTPError as error:
        print(f"Crypto API HTTP Error: {error}")

    except KeyError as error:
        print(f"Crypto API JSON Error: Missing field {error}")

    except ValueError:
        print("Crypto API Error: Invalid JSON response.")

    return None