After cloning , project is located in the mentor_match_app folder.
Create a virtual environment: Ubuntu: Virtualenv myenv  
                              Windows: python -m venv myenv
Activate the environment: Ubuntu: source myenv/bin/activate
                          Windows:.\env\Scripts\activate 
Download Django using : pip install django
Download Crispy-forms : pip install django-crispy-forms
Download Crispy-bootstrap5 : pip install crispy-bootstrap5
Download matplotlib :  pip install matplotlib
Download seaborn  : pip install seanborn 
Change Directory: cd .\mentor_match_app\
Make migrations for admin_mentor_app:python manage.py makemigrations admin_mentor_app
                                     python manage.py migrate admin_mentor_app
                                     python manage.py makemigrations
                                     python manage.py migrate
Make migrations for mentees_app:     python manage.py makemigrations mentees_app
                                     python manage.py migrate mentees_app
                                     python manage.py makemigrations
                                     python manage.py migrate                                     
                                     
Run server: python3 manage.py runserver

 
