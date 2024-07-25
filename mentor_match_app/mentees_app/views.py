
from django.shortcuts import render
from django.http import JsonResponse


# mentees home page
def mentee_home(request):
    # Dummy data for new message count
    new_message_count = 2  # Replace with actual count from the database
    context = {
        'new_message_count': new_message_count,
    }
    return render(request, 'mentees_app/home/mentee_home.html', context)



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

# mentees messages
def mentee_messages(request):
    # Dummy data for chat list
    chats = [
        {
            'id': 1,
            'mentor': {'name': 'Mentor 1', 'profile_pic': 'mentees_app/images/mentor_1.jpeg'},
            'last_message': 'Last message from Mentor 1',
            'last_message_time': '10:30 AM',
            'message_count': 5,
        },
        {
            'id': 2,
            'mentor': {'name': 'Mentor 2', 'profile_pic': 'mentees_app/images/mentor_2.jpeg'},
            'last_message': 'Last message from Mentor 2',
            'last_message_time': '11:00 AM',
            'message_count': 3,
        },
        {
            'id': 3,
            'mentor': {'name': 'Mentor 3', 'profile_pic': 'mentees_app/images/mentor_3.jpeg'},
            'last_message': 'Last message from Mentor 2',
            'last_message_time': '11:00 AM',
            'message_count': 1,
        },
        {
            'id': 4,
            'mentor': {'name': 'Mentor 4', 'profile_pic': 'mentees_app/images/mentor_4.jpeg'},
            'last_message': 'Last message from Mentor 2',
            'last_message_time': '11:00 AM',
            'message_count': '',
        },
    ]
     # Dummy data for new message count
    
    context = {
        'new_message_count': 0,
        'chats': chats,
    }
    return render(request, 'mentees_app/messages/messages.html', context)

# mentee chat details


# Mock API endpoint for chat details
def get_chat_details(request, chat_id):
    # Dummy data for chat details
    chat_data = {
        'mentor': {'name': 'Mentor 1'},
        'messages': [
            {'sender': 'mentor', 'text': 'Hello, how can I help you?', 'time': '10:30 AM'},
            {'sender': 'mentee', 'text': 'I have a question about...', 'time': '10:32 AM'},
        ],
    }
    return JsonResponse(chat_data)



# mentees profile
def mentee_profile(request):
    return render(request, 'mentees_app/profile/profile.html')

# mentees programs
def mentee_programs(request):
    return render(request, 'mentees_app/programs/programs.html')

# mentees resources
def mentee_resources(request):
    return render(request, 'mentees_app/resources/resources.html')