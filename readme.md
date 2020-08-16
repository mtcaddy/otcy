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
