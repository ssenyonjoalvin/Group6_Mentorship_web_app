from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
from admin_mentor_app.models import User, MentorshipMatch, Message, Notification, Schedule, Progress, Evaluation

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(0)

        # Create Users
        for _ in range(60):
            user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                gender=fake.random_element(['Male', 'Female']),
                nationality=fake.country(),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=80),
                password=make_password('defaultpassword'),  # Replace with a default password
                telephone=fake.phone_number(),
                role=fake.random_element(['1', '2', '3']),
                profile_picture=None  # No image
            )
            user.save()

        users = list(User.objects.all())

        # Create MentorshipMatches
        for _ in range(60):
            MentorshipMatch.objects.create(
                mentor=fake.random_element(users),
                mentee=fake.random_element(users),
                status=fake.random_element(['pending', 'accepted', 'rejected'])
            )

        # Create Messages
        for _ in range(60):
            Message.objects.create(
                sender=fake.random_element(users),
                receiver=fake.random_element(users),
                content=fake.text(),
                file=None,
                sent_at=fake.date_time_this_year()
            )

        # Create Notifications
        for _ in range(60):
            Notification.objects.create(
                user=fake.random_element(users),
                message=fake.text(),
                is_read=fake.boolean(),
                created_at=fake.date_time_this_year()
            )

        # Create Schedules
        for _ in range(60):
            Schedule.objects.create(
                mentor=fake.random_element(users),
                mentee=fake.random_element(users),
                session_date=fake.date_time_this_year(),
                status=fake.random_element(['scheduled', 'confirmed', 'completed', 'canceled'])
            )

        # Create Progress
        schedules = list(Schedule.objects.all())
        for _ in range(60):
            Progress.objects.create(
                schedule=fake.random_element(schedules),
                goal=fake.sentence(),
                milestone=fake.sentence() if fake.boolean() else None,
                feedback=fake.text(),
                progress_date=fake.date_time_this_year()
            )

        # Create Evaluations
        matches = list(MentorshipMatch.objects.all())
        for _ in range(60):
            Evaluation.objects.create(
                mentorship_match=fake.random_element(matches),
                mentor=fake.random_element(users),
                mentee=fake.random_element(users),
                evaluation_date=fake.date_time_this_year(),
                technical_skills=fake.random_int(min=1, max=10),
                communication_skills=fake.random_int(min=1, max=10),
                problem_solving_skills=fake.random_int(min=1, max=10),
                time_management=fake.random_int(min=1, max=10),
                team_collaboration=fake.random_int(min=1, max=10),
                comments=fake.text() if fake.boolean() else None
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database with fake data'))
