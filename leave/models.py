from django.db import models
from django.contrib.auth.models import User
from profiles.models import SalaryScale, Signatory

# Create your models here.

class LeaveType(models.Model):
    title = models.CharField(max_length=50)
    # duration = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class LeaveDuration(models.Model):
    salary_scale = models.ForeignKey(SalaryScale, on_delete=models.CASCADE)
    cadre = models.IntegerField()
    duration = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by

class LeaveProcess(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    leave_duration = models.ForeignKey(LeaveDuration, on_delete=models.CASCADE)
    requested_duration = models.IntegerField()
    date_from = models.DateField
    date_to = models.DateField
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by

class LeaveApplicationStatus(models.Model):
    status = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by

class LeaveRecommendation(models.Model):
    recommendation_status = models.ForeignKey(Signatory, on_delete=models.CASCADE)
    comment = models.TextField()
    leave_application = models.ForeignKey('LeaveApplication', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by

class LeaveResumption(models.Model):
    leave_application = models.ForeignKey('LeaveApplication', on_delete=models.CASCADE)
    status = models.ForeignKey(Signatory, on_delete=models.CASCADE)
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __str__(self):
        return self.confirmed_by



class LeaveApplication(models.Model):
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    duration = models.IntegerField()
    requested_duration = models.IntegerField()
    date_from = models.DateField
    date_to = models.DateField
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(LeaveApplicationStatus, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user






