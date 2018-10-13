from django.db import models


class student2(models.Model):
    name = models.CharField(max_length = 50)
    email_id = models.EmailField(max_length = 50)
    contact_no = models.CharField(max_length = 11)
    date = models.DateTimeField()


    def __str__(self):
        return self.email_id