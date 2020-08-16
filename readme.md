python3 -m venv ~/.env/djenv  && source ~/.env/djenv/bin/activate

cd ~/dev && git@github.com:mtcaddy/otcy.git \
	&& poetry init -n  && poetry add Django \
	&& git commit -m "Add poetry"
 
 && mkdir app && cd app 


export PROJECT_NAME=otcy
poetry django-admin startproject $PROJECT_NAME

cd $PROJECT_NAME /
	&& mv $PROJECT_NAME/ config /
	&& find . -type f -name '*.py' -exec sed -i "s/$PROJECT_NAME/config/g" '{}' \;




django-admin.py startproject dashcount . \
		&& python manage.py migrate \
		&& python manage.py runserver

