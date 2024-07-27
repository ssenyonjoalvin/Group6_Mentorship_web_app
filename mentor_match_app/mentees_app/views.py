
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from admin_mentor_app.models import User
from django.db.models import Q
from .forms import MenteeChallengeForm,MenteeProfileUpdateForm 
from django.contrib import messages
from .models import MenteeChallenge


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

def find_mentor(request):
    query = request.GET.get('search', '')
    role_mentor = '2'
    filtered_mentors = []
    if query:
        filtered_mentors = User.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query), 
            # Q(interests__icontains=query) | 
            # Q(expertise__icontains=query),
            role=role_mentor
        )
        
    else:
        filtered_mentors = User.objects.filter(role=role_mentor)
    all_mentors = User.objects.filter(role=role_mentor)  # Get all mentors

    # mentee challenge form
    if request.method == 'POST':
        form = MenteeChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.mentee = request.user  # Assuming the user is logged in
            challenge.mentor = User.objects.get(id=request.POST.get('mentor_id'))
            challenge.save()
            messages.success(request, 'A request has been successfully sent to the mentor.')
            return redirect('mentees_app:find_mentor')

    else:
        form = MenteeChallengeForm()


    return render(request, 'mentees_app/find_a_mentor/find_mentor.html', {'mentors': filtered_mentors, 'all_mentors': all_mentors, 'form': form, 'query': query})

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


#mentee profile 
# @login_required        
def mentee_profile(request):

    user = request.user  # Get the currently logged-in user
    if request.method == "POST":
        form = MenteeProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("mentees_app:profile")
    else:
        form = MenteeProfileUpdateForm(instance=user)
        print(form.fields)

    return render(request, "mentees_app/profile/profile.html", {"form": form})

# @login_required
# @transaction.atomic
# def get_mentees(request):
#     try:
#         mentor_id = request.user.id
#         # Fetch all MentorshipMatch records for the given mentor
#         mentorship_matches = MentorshipMatch.objects.filter(mentor_id=mentor_id).select_related('mentee')

#         # Extract mentee objects and mentorship match records
#         mentees_with_matches = []
#         for match in mentorship_matches:
#             mentees_with_matches.append({
#                 'mentee': match.mentee,
#                 'match': match
#             })

#         return render(request, "admin_mentor_app/mentee/get_mentees.html", {'mentees_with_matches': mentees_with_matches})
#     finally:
#         connection.close()
# @login_required
# @transaction.atomic
# def accept_mentee(request, match_id):
#     mentorship_match = get_object_or_404(MentorshipMatch, id=match_id)
#     mentorship_match.status = 'accepted'
#     mentorship_match.save()
#     return redirect('mentees')

# @login_required
# @transaction.atomic
# def reject_mentee(request, match_id):
#     mentorship_match = get_object_or_404(MentorshipMatch, id=match_id)
#     mentorship_match.status = 'rejected'
#     mentorship_match.save()
#     return redirect('mentees')
    
             
# @login_required
# @transaction.atomic
# def preview_mentee(request, mentee_id):
#     logged_in_user = request.user.id
#     mentee = get_object_or_404(User, id=mentee_id)
    
#     messages = Message.objects.filter(
#         (Q(sender_id=logged_in_user) & Q(receiver_id=mentee_id)) |
#         (Q(sender_id=mentee_id) & Q(receiver_id=logged_in_user))
#     ).order_by('sent_at')  # Order messages by sent time
    
#     menteechallenges = MenteeChallenge.objects.filter(
#         mentee_id=mentee_id,
#         mentor_id=logged_in_user
#     )

#     mentor_progress_groups = Progress.objects.filter(
#         mentee_id=mentee_id,
#         mentor_id=logged_in_user
#     )
    
#     progresses = []
#     for mentor_progress in mentor_progress_groups:
#         goals = Goals.objects.filter(
#             goal_id=mentor_progress
#         )
#         progresses.append({
#             'session_number': mentor_progress.session_number,
#             'progress_percentage': mentor_progress.progress_percentage,
#             'goals': goals,
#             # 'status': goals.status
#         })

#     return render(request, 'admin_mentor_app/mentee/preview_mentee.html', {
#         'mentee': mentee,
#         'messages': messages,
#         'menteechallenges': menteechallenges,
#         'progresses': progresses
#     })

# @csrf_exempt
# @require_POST
# def add_goal(request):
#     goal_text = request.POST.get('newGoal')
#     progress_id = request.POST.get('progress_id')
    
#     try:
#         progress = Progress.objects.get(session_number=progress_id)
#         new_goal = Goals.objects.create(
#             goal_id=progress,
#             goal=goal_text,
#             status='Pending'
#         )
#         new_goal.save()

#         # Calculate the progress percentage
#         total_goals = progress.session_goals.count()
#         completed_goals = progress.session_goals.filter(status='Completed').count()
        
#         if total_goals == 0:
#             progress_percentage = 0
#         else:
#             progress_percentage = (completed_goals / total_goals) * 100
        
#         progress.progress_percentage = str(math.floor(progress_percentage))
#         progress.save()

#         return JsonResponse({'success': True, 'goal': {
#             'id': new_goal.id,
#             'goal': new_goal.goal,
#             'status': new_goal.status
#         }})
#     except Progress.DoesNotExist:
#         return JsonResponse({'success': False, 'error': 'Progress not found'})@method_decorator(csrf_exempt, name='dispatch')
# def send_message(request):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         file = request.FILES.get('file') if 'file' in request.FILES else None
#         receiver_id = request.POST.get('receiver_id')
#         sender_id = request.user.id
        
#         print(content)
#         receiver = User.objects.get(id=receiver_id)
#         sent_at = datetime.datetime.now()
        
#         message = Message(
#             receiver_id=receiver_id,
#             sender_id=sender_id,
#             content=content,
#             file=file,
#             sent_at=sent_at
#         )
#         if message.save():      
#             print("Saved")
        
#         return JsonResponse({'status': 'success', 'message': 'Message sent successfully.'})
#     return JsonResponse({'status': 'failure', 'message': 'Invalid request.'})

# @require_POST
# def update_goal_status(request):
#     goal_id = request.POST.get('goal_id')
#     status = request.POST.get('status')
    
#     try:
#         goal = Goals.objects.get(id=goal_id)
#         goal.status = status
#         goal.save()

#         # Calculate the progress percentage
#         progress = goal.goal_id
#         total_goals = progress.session_goals.count()
#         completed_goals = progress.session_goals.filter(status='Completed').count()
        
#         if total_goals == 0:
#             progress_percentage = 0
#         else:
#             progress_percentage = (completed_goals / total_goals) * 100
        
#         progress.progress_percentage = str(math.floor(progress_percentage))
#         progress.save()

#         return JsonResponse({'success': True})
#     except Goals.DoesNotExist:
#         return JsonResponse({'success': False, 'error': 'Goal not found'})
# @require_POST
# def delete_goal(request):
#     goal_id = request.POST.get('goal_id')
    
#     try:
#         goal = Goals.objects.get(id=goal_id)
#         goal.delete()
#         return JsonResponse({'success': True})
#     except Goals.DoesNotExist:
#         return JsonResponse({'success': False, 'error': 'Goal not found'})
