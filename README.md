# Kick Starter

This loads kickstarter data from 2018 and puts it on a site where you can view details

## Authors

[Hannah Sindorf](https://github.com/hsindorf) [Matthew Brown](https://github.com/mthwbrwn)

## Instructions (local)

1. Clone the repo
1. Start a pipenv shell
1. Install dependencies
1. run 'docker-compose up --build'
1. enter 'docker exec -it container_name_web_1 bash' in another terminal tab to shell into container
1. enter 'python3 load_db.py' to load the database
1. visit localhost

## Technology used

- Python
- Django
- numpy, pandas (to load csv data)
- Sass/SCSS

## Updates

- 1-14-19: initial django setup, basic routes, load db with csv data, sass
