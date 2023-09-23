from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_discription = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    doctor_name = models.CharField(max_length=255)
    doctor_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.doctor_name +' - (' + self.doctor_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_on = models.DateField(auto_now=True)
