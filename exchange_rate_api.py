import requests

def get_exchange_rate(base="EUR", target="GBP"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # DEBUG - Uncomment next line to see full API response
        # print("DEBUG - API response:", data)

        rates = data.get("rates")
        if rates and target in rates:
            return rates[target]
        else:
            print(f"Target currency '{target}' not found in rates.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def main():
    print("Welcome to the Euro to Pound Transfer Fee Converter ⚽")
    rate = get_exchange_rate()
    if rate is None:
        print("Could not retrieve exchange rate. Please try again later.")
        return

    try:
        euros = float(input("Enter the amount in Euros: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    pounds = euros * rate
    print(f"{euros:.2f} EUR is approximately {pounds:.2f} GBP 💷")

if __name__ == "__main__":
    main()




