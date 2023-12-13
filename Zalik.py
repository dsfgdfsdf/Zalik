import requests
from datetime import datetime, timedelta

def get_alpha_vantage_data(api_key, symbol, date):
    # Формування URL для запиту до Alpha Vantage API
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    api_params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
    }

    response = requests.get(base_url, params=api_params)

    if response.status_code == 200:
        data = response.json()
        date_str = date.strftime("%Y-%m-%d")

        # Якщо дані за обрану дату є відсутніми, спробуємо отримати наступний день
        while date_str not in data["Time Series (Daily)"]:
            print(f"Дані за {date_str} відсутні. Спробуємо отримати наступний день.")
            date += timedelta(days=1)
            date_str = date.strftime("%Y-%m-%d")

        return data["Time Series (Daily)"][date_str]
    else:
        print(f"Помилка при отриманні даних: {response.status_code}")
        return None

def main():
    # Замініть 'YOUR_ALPHA_VANTAGE_API_KEY' на ваш ключ API Alpha Vantage
    api_key = 'GB6F4QK3WQ4458ML'
    symbol = "BOND"  # Приклад: символ для облігацій
    birth_date = datetime(2023, 5, 21)

    bond_data = get_alpha_vantage_data(api_key, symbol, birth_date)

    if bond_data:
        print(f"Історичні дані за {birth_date.strftime('%Y-%m-%d')}:\n{bond_data}")
    else:
        print(f"Дані не знайдені за {birth_date.strftime('%Y-%m-%d')}.")

if __name__ == "__main__":
    main()
