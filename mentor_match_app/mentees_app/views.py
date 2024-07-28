
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from admin_mentor_app.models import Schedule, User
from django.db.models import Q
from .forms import MenteeChallengeForm
from django.contrib import messages
from .models import MenteeChallenge
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# mentees home page
def mentee_home(request):
    # Dummy data for new message count
    new_message_count = 2  # Replace with actual count from the database

    # Fetch all mentors
    role_mentor = '2'  # Assuming '2' represents the mentor role
    all_mentors = User.objects.filter(role=role_mentor)
    context = {
        'new_message_count': new_message_count,
        'mentors': all_mentors,
    }
    return render(request, 'mentees_app/home/mentee_home.html', context)

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
  
    if request.method == 'GET':
        # Handle GET request: render the schedule page with the list of schedules for the logged-in mentee
        loggedin_mentee_id = request.user.id  # Assuming the logged-in user's ID represents the mentee ID

        # Fetch all schedules for the logged-in mentee
        schedules = Schedule.objects.filter(mentee_id=loggedin_mentee_id).select_related('mentor')
        print(schedules)
        # Create a list of dictionaries with mentor details and corresponding schedule
        schedule_list = [
            {
                'mentor': schedule.mentor,
                'schedule': schedule
            }
            for schedule in schedules
        ]

        return render(request, "mentees_app/resources/resources.html", {'schedule_list': schedule_list})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@require_POST
def confirm_appointment(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if schedule.status == 'scheduled':
        schedule.status = 'confirmed'
        schedule.save()
    return redirect('mentees_app:resources') 

@csrf_exempt
@login_required
def cancel_appointment(request, schedule_id):
    try:
        schedule = get_object_or_404(Schedule, id=schedule_id)
        
        # Check if the current user is authorized to cancel this schedule
        if request.user.id != schedule.mentee_id:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to cancel this appointment.'})

        schedule.status = 'canceled'
        schedule.save()
        
        return redirect('mentees_app:resources')  # Redirect to the schedule page

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    

@require_POST
def confirm_appointment(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if schedule.status == 'scheduled':
        schedule.status = 'confirmed'
        schedule.save()
    return redirect('mentees_app:resources') 