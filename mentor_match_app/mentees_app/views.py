
from django.shortcuts import render

# mentees home page
def mentee_home(request):
    return render(request, 'mentees_app/home/mentee_home.html')



# Dummy data for mentors
mentors = [
    {'name': 'John Doe', 'interests': 'Data Science', 'expertise': 'Machine Learning', 'availability': 'Weekends'},
    {'name': 'Jane Smith', 'interests': 'Web Development', 'expertise': 'Django', 'availability': 'Weekdays'},
    {'name': 'Alice Johnson', 'interests': 'Data Science', 'expertise': 'Deep Learning', 'availability': 'Weekends'},
    {'name': 'Bob Brown', 'interests': 'Web Development', 'expertise': 'React', 'availability': 'Weekdays'},
]

def find_mentor(request):
    query = request.GET.get('search', '')
    filtered_mentors = []
    if query:
        filtered_mentors = [mentor for mentor in mentors if query.lower() in mentor['name'].lower() or query.lower() in mentor['interests'].lower() or query.lower() in mentor['expertise'].lower()]
        
    else:
        filtered_mentors = mentors

    return render(request, 'mentees_app/find_a_mentor/find_mentor.html', {'mentors': filtered_mentors, 'query': query})