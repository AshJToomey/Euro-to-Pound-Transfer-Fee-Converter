from exchange_rate_api import get_exchange_rate

def convert_eur_to_gbp(euros, rate):
    """
    Converts Euros to British Pounds using a provided exchange rate.
    """
    if euros < 0:
        raise ValueError("Amount in euros cannot be negative.")
    return round(euros * rate, 2)

def main():
    print("Welcome to the Euro to Pound Transfer Fee Converter ⚽")
    
    rate = get_exchange_rate()
    if rate is None:
        print("Unable to retrieve exchange rate. Try again later.")
        return  # Exit early if no rate
    
    try:
        euros = float(input("Enter the amount in Euros: "))
        gbp = convert_eur_to_gbp(euros, rate)  # Pass rate here!
        print(f"€{euros} is approximately £{gbp} at a rate of {rate:.4f}.")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
