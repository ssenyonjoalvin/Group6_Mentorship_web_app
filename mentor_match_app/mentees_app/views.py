from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from admin_mentor_app.models import User
from django.db.models import Q
from .forms import MenteeChallengeForm
from django.contrib import messages
from .models import MenteeChallenge, Evaluation
from admin_mentor_app.models import MentorshipMatch

def mentee_home(request):
    mentee_id = request.user.id

    # Fetch the specific mentor for the logged-in mentee
    mentor_ids = MentorshipMatch.objects.filter(mentee_id=mentee_id).values_list('mentor_id', flat=True)
    mentors = User.objects.filter(id__in=mentor_ids)

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
        'mentors': mentors,
        'available_mentors': available_mentors,
        'search_query': search_query,
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
    return render(request, 'mentees_app/profile/profile.html')

def mentee_programs(request):
    return render(request, 'mentees_app/programs/programs.html')

def mentee_resources(request):
    return render(request, 'mentees_app/resources/resources.html')

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

def fillEvaluationForm(request):
    return render(request, 'mentees_app/evaluation/evaluation_form_fill.html')

def evaluation_view(request):
    match_id = request.GET.get('match_id')
    mentorship_match = get_object_or_404(MentorshipMatch, pk=match_id)

    if request.method == 'POST':
        support = request.POST.get('support')
        communication = request.POST.get('communication')
        confidence = request.POST.get('confidence')
        career = request.POST.get('career')
        understanding = request.POST.get('understanding')
        comfort = request.POST.get('comfort')
        goals = request.POST.get('goals')
        recommend = request.POST.get('recommend')
        resources = request.POST.get('resources')
        additional_resources = request.POST.get('additional_resources')
        additional_comments = request.POST.get('additional_comments')

        evaluation = Evaluation.objects.create(
            mentorship_match=mentorship_match,
            mentor=request.user,
            mentee=mentorship_match.mentee,
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
            additional_comments=additional_comments,
        )

        messages.success(request, "Evaluation submitted successfully")
        return redirect('evaluation_success')

    else:
        evaluation_form = {
            'support': '',
            'communication': '',
            'confidence': '',
            'career': '',
            'understanding': '',
            'comfort': '',
            'goals': '',
            'recommend': '',
            'resources': '',
            'additional_resources': '',
            'additional_comments': '',
        }
        
        return render(request, 'mentees_app/evaluation/evaluation_form_fill.html', {'evaluation_form': evaluation_form, 'mentorship_match': mentorship_match})

def evaluation_success(request):
    return render(request, 'mentees_app/evaluation/evaluation_success.html')
