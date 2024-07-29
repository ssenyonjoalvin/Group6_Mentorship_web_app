Mentor Match Application
Setup Instructions
1.	Clone the Project
       1. After cloning, the project will be located in the mentor_match_app folder.
2.	Create a Virtual Environment
       *       Ubuntu: virtualenv myenv
       *       Windows: python -m venv myenv
3.	Activate the Virtual Environment
       *       Ubuntu: source myenv/bin/activate
       *       Windows: .\myenv\Scripts\activate
4.	Install Required Packages
       *       Download Django: "pip install django"
       *       Download Crispy-forms: pip install django-crispy-forms
       *       Download Crispy-bootstrap5: pip install crispy-bootstrap5
       *       Download matplotlib: pip install matplotlib
       *       Download seaborn: pip install seaborn

5.	Change Directory
       *       Navigate to the project directory: cd .\mentor_match_app\
6.	Make Migrations
7.	For admin_mentor_app:
       *       python manage.py makemigrations admin_mentor_app
       *       python manage.py migrate admin_mentor_app

8.      For mentees_app:
   
       *	python manage.py makemigrations mentees_app
       *	python manage.py migrate mentees_app

    
	Note: You may also need to run general migrations:
        * 	python manage.py makemigrations
        *	python manage.py migrate

    
8.	Run the Server
        *        Start the Django development server:
  	*        python3 manage.py runserver


 

