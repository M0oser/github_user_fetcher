import requests
import json

def load_config():
    """Загружает конфигурацию из файла config.json."""
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_github_user_data(username, token):
    """Получает данные пользователя GitHub."""
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def save_data_to_file(user_data):
    """Сохраняет данные в файл."""
    with open("user_data.txt", "w", encoding="utf-8") as file:
        file.write(f"Имя: {user_data.get('name', 'Не указано')}\n")
        file.write(f"Email: {user_data.get('email', 'Не указан')}\n")
        file.write(f"Публичные репозитории: {user_data.get('public_repos', 0)}\n")

def get_achievements(username, token):
    """Получает информацию о достижениях пользователя (подписчики, звезды, форки)."""
    headers = {"Authorization": f"token {token}"}
    
    # Количество подписчиков
    followers_url = f"https://api.github.com/users/{username}"
    response = requests.get(followers_url, headers=headers)
    followers = response.json().get("followers", 0)

    # Количество звезд и форков во всех репозиториях
    repos_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repos_url, headers=headers)
    repos = response.json()

    stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    forks = sum(repo.get("forks_count", 0) for repo in repos)

    return {
        "followers": followers,
        "stars": stars,
        "forks": forks
    }
def main():
    config = load_config()
    user_data = get_github_user_data(config["username"], config["token"])
    if user_data:
        save_data_to_file(user_data)
        print("Данные сохранены в user_data.txt")
    else:
        print("Ошибка при получении данных.")

if __name__ == "__main__":
    main()