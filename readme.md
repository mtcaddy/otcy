# OTC Dashboard
Building OTC Desk infos by @bit2big

```bash
export PROJECT_NAME=otcy
python3 -m venv ~/.env/djenv  && source ~/.env/djenv/bin/activate
```
```bash
cd ~/dev && git@github.com:mtcaddy/otcy.git \
	&& poetry init -n  && poetry add Django \
	&& git commit -m "Add poetry"

```

```bash
poetry django-admin startproject $PROJECT_NAME
```
```bash
cd $PROJECT_NAME  && mv $PROJECT_NAME/ config
	&& find . -type f -name '*.py' -exec sed -i "s/$PROJECT_NAME/config/g" '{}' \;
```
```bash
python manage.py migrate
poetry run python manage.py runserver
```

```bash
poetry add -D pre-commit && poetry run pre-commit install
poetry run pre-commit sample-config > .pre-commit-config.yaml
cat >> .pre-commit-config.yaml << EOF
- repo: https://github.com/psf/black
  rev: stable
  hooks:
    - id: black
      language_version: python3.6
EOF
```

```bash
poetry run pre-commit run --all-files
```

```bash
Create admin user
python manage.py createsuperuser
```

python manage.py startapp blkeeping
	python manage.py sqlmigrate blkeeping 0001

python manage.py startapp blcontact
	Names
	Contacts (tel/whasapp)
	ID Info
	Profile Picture

 python manage.py startapp blpolls

 python manage.py startapp blog
 	python manage.py makemigrations blog
 	python manage.py sqlmigrate blog 0001
