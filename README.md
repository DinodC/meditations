# Meditations by Marcus Aurelius
The web application provides an ancient drop of knowledge from the
philosopher-king Marcus Aurelius.
http://meditations-marcus-aurelius.info

## Getting Started
To get started, clone the repository https://github.com/DinodC/meditations

### Prerequisites
You will need to install: Python3, Flask, gunicorn and nose.

### Installing
Install virtual environment
```
$ cd meditations
$ virtualenv -p python3 .env
```
Activate the virtual environment
```
$ source .env/bin/activate
```
Install Flask, Gunicorn, and nose
```
(.env) $ pip install -r requirements.txt
```

## Running the tests
Run tests
```
(.env) nosetests -v
```

## Deployment
Serve using Flask, and then with Gunicorn

### Serving with Flask
Serve with Flask
```
(.env) $ python app
```
Check on http://127.0.0.1:5000/

### Serving with Gunicorn
Serve with Gunicorn
```
(.env) $ gunicorn -b 127.0.0.1:5000 -w 2 app:app
```
Check on http://127.0.0.1:5000/


## Built With
* [Flask](http://flask.pocoo.org) - web framework used
* [Gunicorn](https://gunicorn.org) - application server used
* [Nginx](https://www.nginx.com) - front end reverse proxy used

## Versioning
For the versions available see the [tags on this repository](https://github.com/DinodC/meditations)

## Author
* **Dino de Castro** - *Initial work* - [DinodC] (https://github.com/DinodC)

## License
This project is licensed under the author.

## Acknowledgments
A big thank you to the fam - dad, mom, Bok, Anton, Brye and Livia
