from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_time = models.DateTimeField(default=datetime.now)
    leave_time = models.DateTimeField(null=True)
    working_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    break_time = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    attendance = models.IntegerField(default=1, choices=[(1, '出勤'), (0, '未出勤')])
