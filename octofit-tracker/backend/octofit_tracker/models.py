from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    is_superhero = models.BooleanField(default=False)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField(help_text='Duration in minutes')
    calories = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activities'
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.IntegerField()
    rank = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
    def __str__(self):
        return f"{self.team.name} - {self.points} pts"