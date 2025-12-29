from django.core.management.base import BaseCommand
from django.db import connections
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Xóa dữ liệu cũ
        db['users'].delete_many({})
        db['teams'].delete_many({})
        db['activities'].delete_many({})
        db['leaderboard'].delete_many({})
        db['workouts'].delete_many({})

        # Tạo dữ liệu mẫu
        marvel_team = {'name': 'Marvel', 'members': ['ironman@octofit.com', 'spiderman@octofit.com']}
        dc_team = {'name': 'DC', 'members': ['batman@octofit.com', 'wonderwoman@octofit.com']}
        db['teams'].insert_many([marvel_team, dc_team])

        users = [
            {'name': 'Iron Man', 'email': 'ironman@octofit.com', 'team': 'Marvel'},
            {'name': 'Spider-Man', 'email': 'spiderman@octofit.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@octofit.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@octofit.com', 'team': 'DC'},
        ]
        db['users'].insert_many(users)

        activities = [
            {'user': 'ironman@octofit.com', 'type': 'run', 'distance': 5},
            {'user': 'spiderman@octofit.com', 'type': 'cycle', 'distance': 20},
            {'user': 'batman@octofit.com', 'type': 'swim', 'distance': 2},
            {'user': 'wonderwoman@octofit.com', 'type': 'run', 'distance': 10},
        ]
        db['activities'].insert_many(activities)

        leaderboard = [
            {'team': 'Marvel', 'points': 100},
            {'team': 'DC', 'points': 120},
        ]
        db['leaderboard'].insert_many(leaderboard)

        workouts = [
            {'user': 'ironman@octofit.com', 'suggestion': 'HIIT'},
            {'user': 'spiderman@octofit.com', 'suggestion': 'Yoga'},
            {'user': 'batman@octofit.com', 'suggestion': 'Strength'},
            {'user': 'wonderwoman@octofit.com', 'suggestion': 'Cardio'},
        ]
        db['workouts'].insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Đã populate dữ liệu mẫu cho octofit_db!'))
