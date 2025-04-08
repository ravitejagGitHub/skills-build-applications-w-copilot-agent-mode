from django.http import JsonResponse
from django.views import View
from django.conf import settings
from bson.json_util import dumps

class UserViewSet(View):
    def get(self, request):
        users = settings.MONGO_DB.users.find()
        return JsonResponse(dumps(users), safe=False)

class TeamViewSet(View):
    def get(self, request):
        teams = settings.MONGO_DB.teams.find()
        return JsonResponse(dumps(teams), safe=False)

class ActivityViewSet(View):
    def get(self, request):
        activities = settings.MONGO_DB.activities.find()
        return JsonResponse(dumps(activities), safe=False)

class LeaderboardViewSet(View):
    def get(self, request):
        leaderboards = settings.MONGO_DB.leaderboards.find()
        return JsonResponse(dumps(leaderboards), safe=False)

class WorkoutViewSet(View):
    def get(self, request):
        workouts = settings.MONGO_DB.workouts.find()
        return JsonResponse(dumps(workouts), safe=False)
