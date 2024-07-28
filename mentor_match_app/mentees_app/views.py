
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from admin_mentor_app.models import User
from django.db.models import Q
from .forms import MenteeChallengeForm
from django.contrib import messages
from .models import MenteeChallenge
from admin_mentor_app.models import MentorshipMatch



# mentees home page
def mentee_home(request):

    mentee_id = request.user.id
    mentor = None

    # Fetch the specific mentor for the logged-in mentee
    try:
        mymentor = MentorshipMatch.objects.get(mentee_id=mentee_id)
        mentor_id = mymentor.mentor_id
        mentor = User.objects.get(id=mentor_id)
        print(mentor)
    except MentorshipMatch.DoesNotExist:
        mentor = None
    except User.DoesNotExist:
        mentor = None

    # Handle the search functionality for available mentors
    search_query = request.GET.get('search', '')

    if search_query:
        available_mentors = User.objects.filter(
            Q(role=3) & 
            (Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        )
    else:
        available_mentors = User.objects.filter(role=3)

    context = {
        'mentor': mentor,
        'available_mentors': available_mentors,
        
    }
    return render(request, 'mentees_app/home/mentee_home.html', context,)

def schedules(request):
    
    return render(request, 'mentees_app/schedules/schedules.html')

#save data from mentees_challenge form
def send_request(request):
    if request.method == 'POST':
        mentor_id = request.POST.get('mentor_id')
        challenge_1 = request.POST.get('challenge_1')
        challenge_2 = request.POST.get('challenge_2')
        challenge_3 = request.POST.get('challenge_3')
        challenge_4 = request.POST.get('challenge_4')
        challenge_5 = request.POST.get('challenge_5')
        description = request.POST.get('description')

        # Ensure the user is a mentee
        mentee = get_object_or_404(User, id=request.user.id, role='3')
        mentor = get_object_or_404(User, id=mentor_id, role='2')

        # Save the request data to the database
        MenteeChallenge.objects.create(
            mentee=mentee,
            mentor=mentor,
            challenge_1=challenge_1,
            challenge_2=challenge_2,
            challenge_3=challenge_3,
            challenge_4=challenge_4,
            challenge_5=challenge_5,
            description=description
        )
        # Add a success message
        # Redirect to the find_mentor page with a success message
        messages.success(request, 'Your request has been successfully sent to the mentor.')
        return redirect('mentees_app:find_mentor')
    #Redirect to the find_mentor page if the request method is not POST
    return redirect('mentees_app:find_mentor')

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
def mentor(request):
    mentee_id = request.user.id
    mentor = None

    # Fetch the specific mentor for the logged-in mentee
    try:
        mymentor = MentorshipMatch.objects.get(mentee_id=mentee_id)
        mentor_id = mymentor.mentor_id
        mentors = User.objects.get(id=mentor_id)
        print(mentors)
    except MentorshipMatch.DoesNotExist:
        mentor = None
    except User.DoesNotExist:
        mentor = None

    # Handle the search functionality for available mentors
    search_query = request.GET.get('search', '')

    if search_query:
        available_mentors = User.objects.filter(
            Q(role=3) & 
            (Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        )
    else:
        available_mentors = User.objects.filter(role=3)

    context = {
        'mentor': mentor,
        'available_mentors': available_mentors,
    }
    return render(request, 'mentees_app/mentor/mentor.html', context)


#EvaluationForm
def evaluation_form(request):
    return render(request, 'mentees_app/evaluation/evaluation_form.html')
   

      