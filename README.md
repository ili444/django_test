# Django application 

# Процесс запуска кода на локальной машине
  • Устанавливаем Python
  
  • Скачиванием репозиторий и распаковковываем в выбранную папку
  
  • Запускаем терминал(cmd, командная строка) и переходим в выбранную папку, где создаем виртуальное окружение: ```python -m venv myvenv ``` 
  
  • Активируем виртуальное окружение перейдя: ``` myvenv\Scripts\activate ```
  
  • Устанавливаем зависимости: ``` pip install -r requirements.txt ```
  
  • Создаем суперпользователя(admin) в терминале: ```python manage.py createsuperuser```
  
  • Производим миграции в терминале ```python manage.py migrate```
  
  • Запускаем сервер: ``` python manage.py runserver ```
  
  • Открываем в браузере: ``` localhost:8000 ```

