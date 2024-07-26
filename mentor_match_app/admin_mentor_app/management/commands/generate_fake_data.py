from django.core.management.base import BaseCommand
from django.db import transaction, OperationalError, IntegrityError
from faker import Faker
from admin_mentor_app.models import (
    User,
    MentorshipMatch,
    Message,
    Notification,
    Schedule,
    Progress,
    Evaluation,
    Goals,
    MenteeChallenge,
)
import time

class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(0)

        def create_with_retry(model, retries=5, **kwargs):
            while retries > 0:
                try:
                    with transaction.atomic():
                        instance, created = model.objects.get_or_create(**kwargs)
                        if created:
                            return instance
                        else:
                            return None
                except (OperationalError, IntegrityError) as e:
                    retries -= 1
                    if retries == 0:
                        raise e
                    time.sleep(1)

        # Create unique emails
        used_emails = set()
        for _ in range(10):
            while True:
                email = fake.unique.email()
                if email not in used_emails:
                    used_emails.add(email)
                    break

            create_with_retry(
                User,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=email,  # Ensure unique email
                gender=fake.random_element(["Male", "Female"]),
                nationality=fake.country(),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=80),
                password=(fake.random_int(min=12344, max=43215)),  # Convert int to string and hash
                telephone=fake.phone_number(),
                role=fake.random_element(["1", "2", "3"]),
                profile_picture=None,  # No image
            )

        users = list(User.objects.all())
        mentors = list(User.objects.filter(role="2"))
        mentees = list(User.objects.filter(role="3"))

        # Create MentorshipMatches
        for _ in range(10):
            create_with_retry(
                MentorshipMatch,
                mentor=fake.random_element(mentors),
                mentee=fake.random_element(mentees),
                status=fake.random_element(["pending", "accepted", "rejected"]),
            )

        # Create Messages
        for _ in range(10):
            create_with_retry(
                Message,
                sender=fake.random_element(users),
                receiver=fake.random_element(users),
                content=fake.text(),
                file=None,
                sent_at=fake.date_time_this_year(),
            )

        # Create Notifications
        for _ in range(2):
            create_with_retry(
                Notification,
                sent_by=fake.random_element(users),
                received_by=fake.random_element(users),
                message=fake.text(),
                is_read=fake.boolean(),
                created_at=fake.date_time_this_year(),
            )

        # Create Schedules
        for _ in range(3):
            create_with_retry(
                Schedule,
                mentor=fake.random_element(mentors),
                mentee=fake.random_element(mentees),
                session_date=fake.date_time_this_year(),
                status=fake.random_element(
                    ["scheduled", "confirmed", "completed", "canceled"]
                ),
            )

        # Create Progress
        for _ in range(3):
            create_with_retry(
                Progress,
                mentor=fake.random_element(mentors),
                mentee=fake.random_element(mentees),
                progress_percentage=fake.random_element(
                    ["0%", "25%", "50%", "75%", "100%"]
                ),
            )

        progresses = list(Progress.objects.all())

        # Create Goals
        for _ in range(3):
            create_with_retry(
                Goals,
                goal_id=fake.random_element(progresses),
                goal=fake.sentence(),
                status=fake.random_element(["Not Started", "In Progress", "Completed"]),
            )

        # Create Evaluations
        matches = list(MentorshipMatch.objects.all())
        for _ in range(10):
            create_with_retry(
                Evaluation,
                mentorship_match=fake.random_element(matches),
                mentor=fake.random_element(mentors),
                mentee=fake.random_element(mentees),
                evaluation_date=fake.date_time_this_year(),
                technical_skills=fake.random_int(min=1, max=10),
                communication_skills=fake.random_int(min=1, max=10),
                problem_solving_skills=fake.random_int(min=1, max=10),
                time_management=fake.random_int(min=1, max=10),
                team_collaboration=fake.random_int(min=1, max=10),
                comments=fake.text() if fake.boolean() else None,
            )

        # Create MenteeChallenges
        for mentee in mentees:
            for _ in range(3):  # Create 3 challenges per mentee
                create_with_retry(
                    MenteeChallenge,
                    mentee=mentee,
                    mentor=fake.random_element(mentors),
                    challenge=fake.sentence(),
                    session_no=str(fake.random_int(min=1, max=10)),
                    details=fake.text(),
                    created_at=fake.date_time_this_year()
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated database with fake data")
        )
