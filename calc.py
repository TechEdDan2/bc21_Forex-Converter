from forex_python.converter import CurrencyRates
c = CurrencyRates()

def convert_currency(amount, from_currency, to_currency):
    """ Convert amount from one currency to another """
    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        print(f"Error converting currency: {e}")
        return None 
