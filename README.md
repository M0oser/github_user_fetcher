# GitHub User Fetcher

GitHub User Fetcher — это Python-программа, которая получает публичные данные о пользователе GitHub, такие как имя, email (если доступно) и информацию о репозиториях. Данные сохраняются в текстовый файл.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/M0oser/github_user_fetcher.git
   cd github_user_fetcher
   ```

2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка

Для работы программы необходимо указать GitHub API токен.

1. Создайте файл `.env` в корневой директории проекта.
2. Добавьте в него ваш персональный токен GitHub:
   ```env
   GITHUB_TOKEN=ваш_персональный_токен
   ```
3. Получить токен можно в [настройках GitHub](https://github.com/settings/tokens) (Personal Access Token).
   - Дайте ему права на `read:user`.

## Запуск

1. Убедитесь, что виртуальное окружение активно (`source venv/bin/activate`).
2. Запустите программу:
   ```bash
   python main.py
   ```
3. После выполнения данные будут сохранены в файле `output.txt`.


