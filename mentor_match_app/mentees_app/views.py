from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from admin_mentor_app.models import Schedule, User
from django.db.models import Q
from .forms import MenteeChallengeForm,MenteeProfileUpdateForm 
from django.contrib import messages
from .models import MenteeChallenge
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db import transaction
from django.contrib.auth.decorators import login_required
from datetime import datetime
from admin_mentor_app.models import (
    User,
    MentorshipMatch,
    Message,
    Notification,
    Schedule,
    Progress,
    Goals,
    Evaluation,
    MenteeChallenge
)

# mentees home page
def mentee_home(request):
    mentee_id = request.user.id
    available_evaluations = []

    # Fetch evaluations with 100% progress for the logged-in mentee
    progressed_evaluations = Progress.objects.filter(
        mentee_id=mentee_id,
        progress_percentage=100,
    )
    print("Progress ev: ", progressed_evaluations)

    # Fetch the specific mentors for the logged-in mentee
    mentor_ids = MentorshipMatch.objects.filter(mentee_id=mentee_id).values_list('mentor_id', flat=True)
    mentors = User.objects.filter(id__in=mentor_ids)

    # Handle the search functionality for available mentors
    search_query = request.GET.get('search', '')

    if search_query:
        available_mentors = User.objects.filter(
            Q(role="2") & 
            Q(availability="1") & 
            (Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        )
    else:
        available_mentors = User.objects.filter(role="2", availability="1")
    print("Available ", available_mentors)

    context = {
        'mentors': mentors,
        'available_mentors': available_mentors,
        'search_query': search_query,
        'progressed_evaluations': progressed_evaluations,
    }
    return render(request, 'mentees_app/home/mentee_home.html', context)
def schedules(request):
    return render(request, 'mentees_app/schedules/schedules.html')

def send_request(request):
    if request.method == 'POST':
        mentor_id = request.POST.get('mentor_id')
        challenge_1 = request.POST.get('challenge_1')
        challenge_2 = request.POST.get('challenge_2')
        challenge_3 = request.POST.get('challenge_3')
        challenge_4 = request.POST.get('challenge_4')
        challenge_5 = request.POST.get('challenge_5')
        description = request.POST.get('description')

        mentee = get_object_or_404(User, id=request.user.id, role='3')
        mentor = get_object_or_404(User, id=mentor_id, role='2')

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

        messages.success(request, 'Your request has been successfully sent to the mentor.')
        return redirect('mentees_app:find_mentor')

    return redirect('mentees_app:find_mentor')

def mentee_messages(request):
    chats = [
        {
            'id': 1,
            'mentor': {'name': 'Mentor 1', 'profile_pic': 'mentees_app/images/mentor_1.jpeg'},
            'last_message': 'Last message from Mentor 1',
            'last_message_time': '10:30 AM',
            'message_count': 5,
        },
        # other chats...
    ]

    context = {
        'new_message_count': 0,
        'chats': chats,
    }
    return render(request, 'mentees_app/messages/messages.html', context)

def get_chat_details(request, chat_id):
    chat_data = {
        'mentor': {'name': 'Mentor 1'},
        'messages': [
            {'sender': 'mentor', 'text': 'Hello, how can I help you?', 'time': '10:30 AM'},
            {'sender': 'mentee', 'text': 'I have a question about...', 'time': '10:32 AM'},
        ],
    }
    return JsonResponse(chat_data)

def mentee_profile(request):

    user = request.user  # Get the currently logged-in user
    if request.method == "POST":
        form = MenteeProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("mentees_app:profile")
    else:
        form = MenteeProfileUpdateForm(instance=user)
    return render(request, "mentees_app/profile/profile.html", {"form": form})

def mentee_programs(request):
    return render(request, 'mentees_app/programs/programs.html')

def mentee_resources(request):
  
    if request.method == 'GET':
        # Handle GET request: render the schedule page with the list of schedules for the logged-in mentee
        loggedin_mentee_id = request.user.id  # Assuming the logged-in user's ID represents the mentee ID

        # Fetch all schedules for the logged-in mentee
        schedules = Schedule.objects.filter(mentee_id=loggedin_mentee_id).select_related('mentor')
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

@login_required
@transaction.atomic
def previewMentor(request, mentor_id):
    logged_in_user = request.user.id
    mentee = get_object_or_404(User, id=mentor_id)    
    messages = Message.objects.filter(
        (Q(sender_id=logged_in_user) & Q(receiver_id=mentor_id)) |
        (Q(sender_id=mentor_id) & Q(receiver_id=logged_in_user))
    ).order_by('sent_at')  # Order messages by sent time
    
    menteechallenges = MenteeChallenge.objects.filter(
        mentee_id=logged_in_user,
        mentor_id=mentor_id
    )

    mentor_mentee_match_status = MentorshipMatch.objects.filter(
            mentee_id=logged_in_user,
            mentor_id=mentor_id,
            status="accepted"
        )

    
    mentor_progress_groups = Progress.objects.filter(
        mentee_id=logged_in_user,
        mentor_id=mentor_id
    )
    
    progresses = []
    for mentor_progress in mentor_progress_groups:
        goals = Goals.objects.filter(
            goal_id=mentor_progress
        )
        progresses.append({
            'session_number': mentor_progress.session_number,
            'progress_percentage': mentor_progress.progress_percentage,
            'goals': goals,
            # 'status': goals.status
        })
    print("BAN: ",mentor_mentee_match_status)
    return render(request, 'mentees_app/mentor/mentor_preview.html',  {
        'mentee': mentee,
        'messages': messages,
        'menteechallenges': menteechallenges,
        'progresses': progresses
        ,'mentor_mentee_match_status':mentor_mentee_match_status
    })

def mentor(request):
    mentee_id = request.user.id
    
    try:
        mentorship_match = MentorshipMatch.objects.get(mentee_id=mentee_id)
        mentor = User.objects.get(id=mentorship_match.mentor_id)
    except (MentorshipMatch.DoesNotExist, User.DoesNotExist):
        mentor = None

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

def evaluation_form(request):
    return render(request, 'mentees_app/evaluation/evaluation_form.html')

def fillEvaluationForm(request,mentor_id):
    return render(request, 'mentees_app/evaluation/evaluation_form_fill.html',{"mentor_id":mentor_id})

def submitEvaluationForm(request, mentor_id):
    if request.method == "POST":
        mentee = request.user
        mentor = get_object_or_404(User, id=mentor_id)
        mentorship_match = get_object_or_404(MentorshipMatch, mentor=mentor, mentee=mentee)
        
        # Extract form data from POST request
        support = request.POST.get("support")
        communication = request.POST.get("communication")
        confidence = request.POST.get("confidence")
        career = request.POST.get("career")
        understanding = request.POST.get("understanding")
        comfort = request.POST.get("comfort")
        goals = request.POST.get("goals")
        recommend = request.POST.get("recommend")
        resources = request.POST.get("resources")
        additional_resources = request.POST.get("additional_resources", "")
        additional_comments = request.POST.get("additional_comments", "")
        
       
        # Create and save the evaluation
        evaluation = Evaluation.objects.create(
            mentorship_match=mentorship_match,
            mentor=mentor,
            mentee=mentee,
            support=support,
            communication=communication,
            confidence=confidence,
            career=career,
            understanding=understanding,
            comfort=comfort,
            goals=goals,
            recommend=recommend,
            resources=resources,
            additional_resources=additional_resources,
            additional_comments=additional_comments
        )
        
        # Redirect to mentee home after successful form submission
        return redirect('mentees_app:mentee_home')
    
    # If GET request, redirect to mentee home (or show an error page)
    return redirect('mentees_app:mentee_home')
def evaluation_view(request):
    # match_id = request.GET.get('match_id')
    # mentorship_match = get_object_or_404(MentorshipMatch, pk=match_id)

    print(request)
        
    return render(request, 'mentees_app/evaluation/evaluation_form_fill.html')

def evaluation_success(request):
    return render(request, 'mentees_app/evaluation/evaluation_success.html')

@login_required
def sendRequestToMentor(request, mentor_id):
    mentee = request.user
    mentor = get_object_or_404(User, id=mentor_id)

    # Create a new mentorship match with 'pending' status
    MentorshipMatch.objects.create(
        mentee=mentee,
        mentor=mentor,
        status='pending',
        match_date=datetime.now()
    )

    # Redirect to the mentee home page
    return redirect('mentees_app:mentee_home')
    