import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url)
        print("🔎 API URL:", url)
        print("🌐 Status code:", response.status_code)

        if response.status_code != 200:
            print("❌ API Error!")
            return None

        data = response.json()
        print("📦 API response:", data)

        result = data['rates'].get(to_currency)
        if result:
            return round(result, 2)
        else:
            print("❌ Currency not found in response.")
            return None

    except Exception as e:
        print("🚨 Exception occurred:", e)
        return None


# Kullanıcıdan veri al
from_currency = input("From currency (e.g. USD): ").upper()
to_currency = input("To currency (e.g. TRY): ").upper()

try:
    amount = float(input("Amount: "))
except ValueError:
    print("❌ Please enter a valid number.")
    exit()

converted = convert_currency(from_currency, to_currency, amount)

if converted is not None:
    print(f"\n💱 {amount} {from_currency} = {converted} {to_currency}")
else:
    print("❌ Conversion failed.")
