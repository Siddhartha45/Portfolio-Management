from django.db import models


class PortfolioUser(models.Model):
    """
    Model for storing user information whose portfolio website is being built.
    """
    # User basic details
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100, blank=True)
    # User education/professional
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    specific_title = models.CharField(max_length=80, blank=True)
    #Social links
    twitter = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    insta = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    github = models.CharField(max_length=200, blank=True)
    website = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.first_name
    
    def fullname(self):
        return f"{self.first_name}  {self.middle_name}  {self.last_name}"