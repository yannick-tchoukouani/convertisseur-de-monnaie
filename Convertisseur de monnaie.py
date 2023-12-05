from forex_python.converter import CurrencyRates
import json
from datetime import datetime

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount, rate
    except:
        return None, None

def save_conversion_history(history):
    with open('conversion_history.json', 'w') as file:
        json.dump(history, file, indent=4)

def load_conversion_history():
    try:
        with open('conversion_history.json', 'r') as file:
            history = json.load(file)
        return history
    except FileNotFoundError:
        return []

def display_conversion_history(history):
    print("\nConversion History:")
    for entry in history:
        print(f"{entry['date']} - {entry['from_amount']} {entry['from_currency']} to {entry['to_amount']} {entry['to_currency']} (Rate: {entry['exchange_rate']})")

def main():
    amount = float(input("Entrez le montant à convertir : "))
    from_currency = input("Entrez la devise source (code ISO) : ").upper()
    to_currency = input("Entrez la devise cible (code ISO) : ").upper()

    converted_amount, exchange_rate = convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"\n{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency} (Taux de change : {exchange_rate})")

        # Enregistrement de l'historique
        history_entry = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'from_amount': amount,
            'from_currency': from_currency,
            'to_amount': converted_amount,
            'to_currency': to_currency,
            'exchange_rate': exchange_rate
        }

        history = load_conversion_history()
        history.append(history_entry)
        save_conversion_history(history)

        # Affichage de l'historique
        display_conversion_history(history)
    else:
        print(f"\nImpossible de convertir {amount} {from_currency} en {to_currency}. Vérifiez les codes de devise.")

if __name__ == "__main__":
    main()
