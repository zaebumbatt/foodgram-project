# Foodgram. 
# Thesis project for Yandex Practicum.
http://142.93.108.170:8080/

# Run
1. [Install Docker](https://www.docker.com/products/docker-desktop) and [Docker Compose](https://docs.docker.com/compose/install/) (if you have Linux).
2. Clone repository https://github.com/zaebumbatt/foodgram-project.git
3. Rename ```.env-example``` to ```.env``` and fill with your secret data.
4. Open foodgram-project folder and run ```docker-compose up -d```
5. Go inside container ```docker exec -it foodgram-project_web_1 bash```
6. Run commands:
   
   ```python manage.py collectstatic```
   
   ```python manage.py migrate```
   
   ```python manage.py loadingredients```
   
   ```python manage.py createsuperuser``` - fill credential for new admin user.
   
   ```python manage.py runserver```
4. Go to http://localhost:8080/ or http://localhost:8080/admin/ for an admin panel.

# Functionality
* Full user authentication.
* Create/edit/delete new recipe.
* Filter by breakfast/lunch/dinner.  
* Choose from a bunch of ingredients.
* Add to favourites.
* Favourites page.
* Follow another authors.
* Add to shopping list.
* Download shopping list.

# What I used
* Python
* Django
* Django REST
* Docker


HTML/CSS/Javascript was made by web faculty (thank you).