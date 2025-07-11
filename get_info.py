import requests
from typing import Dict, Optional, Any
import json

PYRUS_URL = 'https://accounts.pyrus.com/api/v4'
TASKS_URL = 'https://api.pyrus.com/v4/tasks'
BOT_LOGIN = input('Введите Login: ').strip()
BOT_KEY = input('Введите API Pyrus: ').strip()

def get_token(login: str, apikey: str, url: str) -> Dict[str, str]:
    print("Запрос токена...")
    auth_headers = {'Content-Type': 'application/json'}
    auth_data = {'login': login, 'security_key': apikey}

    try:
        response = requests.post(url, headers=auth_headers, json=auth_data)
        response.raise_for_status()
        print(f"Авторизация успешна! Код ответа: {response.status_code}.")
        
    except requests.RequestException as error_type:
        print(f"Ошибка авторизации: {error_type}")
        raise
    
    print("_________________________________________________")
    access_token = response.json().get("access_token")
    
    if not access_token:
        print("Токен отсутствует!")
        raise ValueError("Токен отсутствует!")

    return {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
def authenticate(): #-> Optional[Dict[str, str]]:
    """Функция авторизации и получения токена"""
    try:
        url = f"{PYRUS_URL}/auth"
        auth_headers = get_token(BOT_LOGIN, BOT_KEY, url)
        print("Шаг 1: Данные авторизации получены")
        return auth_headers
    
    except Exception as error_type:
        print(f"Ошибка авторизации: {error_type}")
        return None

def get_task(task_id: int, headers: Dict[str, str]) -> Optional[Dict[str, Any]]:
    """Получение задачи по номеру в Pyrus"""
    try:
        print(f"Запрос задачи №{task_id}...")
        response = requests.get(f"{TASKS_URL}/{task_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error_type:
        print(f"Ошибка при получении задачи: {error_type}")
        return None

def main() -> None:
    """Основная логика программы"""
    auth_headers = authenticate()
    if not auth_headers:
        return
    
    while True:
        print("\nВведите номер задачи (или 'quit' для выхода):")
        user_input = input().strip()
        
        if user_input.lower() == 'quit':
            print("Выход из программы.")
            break
            
        if not user_input.isdigit():
            print("Ошибка: введите числовой номер задачи!")
            continue
            
        task_id = int(user_input)
        task_data = get_task(task_id, auth_headers)
        
        if task_data:
            print(json.dumps(task_data, indent=2, ensure_ascii=False))
        else:
            print("Не удалось получить данные задачи.")

if __name__ == "__main__": # Прост вызов
    main()
=======
import requests
from typing import Dict, Optional, Any
import json

PYRUS_URL = 'https://accounts.pyrus.com/api/v4'
TASKS_URL = 'https://api.pyrus.com/v4/tasks'
BOT_LOGIN = input('Введите Login: ').strip()
BOT_KEY = input('Введите API Pyrus: ').strip()

def get_token(login: str, apikey: str, url: str) -> Dict[str, str]:
    print("Запрос токена...")
    auth_headers = {'Content-Type': 'application/json'}
    auth_data = {'login': login, 'security_key': apikey}

    try:
        response = requests.post(url, headers=auth_headers, json=auth_data)
        response.raise_for_status()
        print(f"Авторизация успешна! Код ответа: {response.status_code}.")
        
    except requests.RequestException as error_type:
        print(f"Ошибка авторизации: {error_type}")
        raise
    
    print("_________________________________________________")
    access_token = response.json().get("access_token")
    
    if not access_token:
        print("Токен отсутствует!")
        raise ValueError("Токен отсутствует!")

    return {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
def authenticate(): #-> Optional[Dict[str, str]]:
    """Функция авторизации и получения токена"""
    try:
        url = f"{PYRUS_URL}/auth"
        auth_headers = get_token(BOT_LOGIN, BOT_KEY, url)
        print("Шаг 1: Данные авторизации получены")
        return auth_headers
    
    except Exception as error_type:
        print(f"Ошибка авторизации: {error_type}")
        return None

def get_task(task_id: int, headers: Dict[str, str]) -> Optional[Dict[str, Any]]:
    """Получение задачи по номеру в Pyrus"""
    try:
        print(f"Запрос задачи №{task_id}...")
        response = requests.get(f"{TASKS_URL}/{task_id}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error_type:
        print(f"Ошибка при получении задачи: {error_type}")
        return None

def main() -> None:
    """Основная логика программы"""
    auth_headers = authenticate()
    if not auth_headers:
        return
    
    while True:
        print("\nВведите номер задачи (или 'quit' для выхода):")
        user_input = input().strip()
        
        if user_input.lower() == 'quit':
            print("Выход из программы.")
            break
            
        if not user_input.isdigit():
            print("Ошибка: введите числовой номер задачи!")
            continue
            
        task_id = int(user_input)
        task_data = get_task(task_id, auth_headers)
        
        if task_data:
            print(json.dumps(task_data, indent=2, ensure_ascii=False))
        else:
            print("Не удалось получить данные задачи.")

if __name__ == "__main__": # Прост вызов
    main()
>>>>>>> 78000c59b119d36200a26b1a99be802f9e7185bb
