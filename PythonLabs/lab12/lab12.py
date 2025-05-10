import requests

# Функция, выполняющая запрос и подробный вывод
def make_request(method, url, data=None):
    print(f"\n{'='*10} Метод {method} {'='*10}")

    try:
        if method == 'OPTIONS':
            response = requests.options(url)
        elif method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, data=data)
        else:
            print('Не поддерживаемый метод.')
            return

        # Выводим детали запроса (для GET и POST)
        if method in ['GET', 'POST']:
            print(f"Запрос ({method}):")
            print(f"URL: {response.request.url}")
            print(f"Заголовки запроса:\n{response.request.headers}")
            if data:
                print(f"Тело запроса:\n{response.request.body}")

        # Подробный вывод ответа сервера
        print(f"\nОтвет сервера ({response.status_code}):")
        print(f"Код ответа: {response.status_code}")
        print("Заголовки ответа:")
        for k, v in response.headers.items():
            print(f"{k}: {v}")

        # Тело ответа
        print("\nТело ответа:")
        print(response.text)

    except Exception as e:
        print("Ошибка при выполнении запроса:", e)

if __name__ == "__main__":
    url = 'https://httpbin.org'

    # Тестирование метода OPTIONS
    make_request('OPTIONS', url)

    # Тестирование метода GET
    make_request('GET', url + '/get?param=value')

    # Тестирование метода POST с отправкой данных
    data = {'username': 'oleg', 'password': '12345'}
    make_request('POST', url + '/post', data=data)