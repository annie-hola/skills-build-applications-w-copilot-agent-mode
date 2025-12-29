"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from pymongo import MongoClient

def get_collection_data(collection):
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']
    data = list(db[collection].find({}, {'_id': 0}))
    return JsonResponse(data, safe=False)

def users_api(request):
    return get_collection_data('users')

def teams_api(request):
    return get_collection_data('teams')

def activities_api(request):
    return get_collection_data('activities')

def leaderboard_api(request):
    return get_collection_data('leaderboard')

def workouts_api(request):
    return get_collection_data('workouts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', users_api),
    path('api/teams/', teams_api),
    path('api/activities/', activities_api),
    path('api/leaderboard/', leaderboard_api),
    path('api/workouts/', workouts_api),
]
