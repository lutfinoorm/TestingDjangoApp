from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, null=True)

  def __str__(self):
    return f"({self.id}) {self.firstname} {self.lastname}"