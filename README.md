# Система управления пользователями

## Описание
Это приложение предоставляет интерфейс для управления учетными записями пользователей в компании. Приложение позволяет администраторам добавлять, удалять пользователей, а также просматривать текущий список пользователей. Разработано с использованием Python и библиотеки Tkinter для создания графического интерфейса.

## Основной функционал
- **Добавление пользователя**: Администратор может добавить нового пользователя, указав уникальный идентификатор (ID), имя и уровень доступа (обычный пользователь или администратор).
- **Удаление пользователя**: Администратор может удалить пользователя из системы, указав его ID.
- **Просмотр списка пользователей**: Администратор может просмотреть текущий список всех пользователей системы.

## Установка
1. Убедитесь, что у вас установлен Python 3.6 или выше.
2. Клонируйте репозиторий проекта:
    ```sh
    git clone https://github.com/ваш-логин/User-Management.git
    ```
3. Перейдите в папку проекта:
    ```sh
    cd User-Management
    ```
4. Создайте и активируйте виртуальное окружение (опционально):
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Для Windows используйте `.venv\Scripts\activate`
    ```
5. Установите необходимые зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Использование
1. Запустите приложение:
    ```sh
    python main.py
    ```
2. **Добавление пользователя**:
    - Введите уникальный ID пользователя.
    - Введите имя пользователя.
    - Введите уровень доступа (по умолчанию "пользователь" или "админ").
    - Нажмите кнопку "Добавить пользователя".
3. **Удаление пользователя**:
    - Введите ID пользователя, которого нужно удалить.
    - Нажмите кнопку "Удалить пользователя".
4. **Просмотр списка пользователей**:
    - Нажмите кнопку "Показать пользователей", чтобы отобразить текущий список всех пользователей.

## Структура проекта
- `main.py`: Главный файл приложения, содержащий логику работы и графический интерфейс.
- `README.md`: Описание проекта и инструкции по установке и использованию.

## Требования
- Python 3.6 или выше
- Tkinter (обычно включен в стандартную библиотеку Python)

## Автор
Ваше имя

## Лицензия
Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.
