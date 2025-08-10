# stripe_project
# Реализация веб-приложения для работы со Stripe

## Возможности:
- http://127.0.0.1:8000/shop/item/ - просмотр всех доуступных товаров, в том числе их id для дальнейших запросов
- http://127.0.0.1:8000/shop/item/1/ - просмотр страницы товара с id=1, возможность перейти на страницу для оплаты от stripe
- http://127.0.0.1:8000/shop/order/1/ - просмотр страницы заказа с id=1, возможность перейти на страницу для оплаты от stripe
- http://127.0.0.1:8000/shop/buy/1/ - получение Stripe Session Id для оплаты выбранного товара
- http://127.0.0.1:8000/shop/buy_order/1/ - получение Stripe Session Id для оплаты выбранного заказа
- http://127.0.0.1:8000/admin/ - доступ к админке джанго(admin:admin)

## Приложение было опубликовано на pythonanywhere по ссылке - https://ekaterina2006.pythonanywhere.com/shop/item/
Так как на pythonanywhere БД PostgreSQL доступна только в платной подписке, я переделал версию на сайте на MySQL. 

### Технологии

- Python
- Django
- PostgreSQL(MySQL)

### Подготовка БД перед запуском

Создаём БД и пользователя для работы сервиса, выдаём новому пользователю права на БД:
```bash
psql postgres
```
```sql
CREATE DATABASE stripe;
CREATE USER stripe WITH PASSWORD 'stripe';
GRANT ALL PRIVILEGES ON DATABASE stripe to stripe;
\q
```

### Установка на MacOS/Linux

Открываем терминал, создаём папку, в которой будет располагаться проект и переходим в неё:
```bash
mkdir /ваш/путь
cd /ваш/путь
```
Клонируем репозотирий в эту папку:
```bash 
git clone https://github.com/DmitriyChubarov/stripe_project.git
```
После чего создаём новое виртуальное окружение. Запускаем и устанавливаем в него django, DRF и все необходимое:
```bash
pipenv shell
pip install django
pip install psycopg2-binary
pip install requests

```
Окончательно настраиваем проект:
```bash
cd stripe_project/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
  
### Контакты
- tg: @eeezz_z
- gh: https://github.com/DmitriyChubarov
