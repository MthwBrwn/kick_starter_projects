from django.db import models


class Project(models.Model):
    pass


class Project(models.Model):
    """ model for a kickstarter project """
    name = models.CharField(max_length=1028)
    category = models.CharField(max_length=1028)
    main_category = models.CharField(max_length=1028)
    currency = models.CharField(max_length=1028)
    deadline = models.DateField()
    goal = models.FloatField()
    launched = models.DateTimeField()
    pledged = models.FloatField()
    state = models.CharField(max_length=1028)
    backers = models.IntegerField()
    country = models.CharField(max_length=1028)
    usd_pledged = models.FloatField()
    usd_pledged_real = models.FloatField()
    usd_goal_real = models.FloatField()

    def __repr__(self):
        return f'<Project: {self.name}>'

    def __str__(self):
        return f'Project {self.name} ({self.state})'
