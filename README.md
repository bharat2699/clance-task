## Backend python assessment

***Note from candidate:***

1. CURL command to test the signup api:

```
curl  -X POST \
  'http://127.0.0.1:8400/signup' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "userName": "Bharat",
  "userEmail": "bharat4official@gmail.com",
  "userPassword": "hello"
}'
```

2. CURL command to test the login api:

```
curl  -X POST \
  'http://127.0.0.1:8400/login' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "userEmail": "bharat4official@gmail.com",
  "userPassword": "hello"
}'
```

3. Celery Worker has been dockerized and is using mongodb as broker.

***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml`, `Dockerfile` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")

***Installation***

Running the scaffolding app is very easy. First [install](https://docs.docker.com/install/) docker for your operating system from the docs provided in the docker website. Also [install](https://docs.docker.com/compose/install/) docker-compose

Then run

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.

***Logs***

A `logs` folder is created in the root of the project i.e outside the `src` folder, which is mounted using the docker-compose volume mount. It will contain a file `flask-scaffolding.log` and will contain the project logs.

***Your Assignment***

You have to achieve two major tasks:

    Create a Login API (JSON) in flask in this structure.
    Setup celery in this project and write a task that stores last login information in another collection of mongo

Go through the structure of the project and figure out how you would proceed.

Make sure that all the api only logic should go in api layer (i.e. views.py) and all the business logic should go in the service layer (i.e. user_service.py).
Schema goes in the models/user.py file.

Refer docstrings in the above mentioned files.

***Submission***

For submitting your work, follow these steps:-

Push the codes in your personal Github Repo (Make sure it's public repository)

Put the screenshots of the running application inside the images folder

Share the link of your Github repo with Recruiter/HR Executive
