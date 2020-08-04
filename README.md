# EventManager
http://tywinevergreen-event-manager.xyz/#/

**Install python requirements**  

<!-- СДЕЛАТЬ, ЧТОБЫ README.md правильно генерировался на гитхабе.
после этого англофицировать весь сайт (что вряд-ли займёт много времени)
затем начинать деплоить проект на justhost.ru -->

``` bash
pip install -r requirements.txt
```

**Environment**

- Create an environment file named `event-manager.env`
- Possible keys:
    `SECRET_KEY`
    `EMAIL_HOST_USER`
    `EMAIL_HOST_PASSWORD`
    `EMAIL_PORT`
    `DB_NAME`
    `DB_USER`
    `DB_PASSWORD`
    `DB_HOST`
    `DB_PORT`
    `CELERY_BROKER_URL`

**VueJS**

``` bash
# go to the project directory vue
cd event_manager_vue

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run serve

# build for production with minification
npm run build
```

**Run in Docker container**

To run the Docker container you need to have a 'dist' directory in your project root
- First of all, in docker-compose.yml file set POSTGRES_DB, POSTGRS_USER, POSTGRES_PASSWORD variables on db container ('postgres' on each variable by default)

``` bash
# Build a Docker image
sudo docker-compose build

# Run Docker containers
sudo docker-compose up

# To stop all running containers
sudo docker-compose down
```

**Author's contacts**

- [VK Profile](https://vk.com/gsurkov99)
- e-mail: holydiver.gs@gmail.com
- telegram: @TywinEvergreen
