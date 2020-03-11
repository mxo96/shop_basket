
##Shop Basket Application

### Run Docker
docker build -t shop_basket .

docker run -d -p 5000:5000 shop_basket


### Run with Venv
create virtual env

install requirements.txt
EXPORT_FLASK=app.py

flask run