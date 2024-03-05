from django.db import models

# from django.contrib.auth.hashers import make_password


class PostJob(models.Model):

    class JOB_TYPE(models.TextChoices):
        FULL_TIME = "fulltime", "Full Time"
        PART_TIME = "parttime", "Part Time"
        CONTRACT = "contract", "Contract"
        INTERNSHIP = "intership", "Internship"
        FREELANCE = "freelance", "Freelance"

    class JOB_LOCATION_TYPE(models.TextChoices):
        ONSITE = "onsite", "Onsite"
        REMOTE = "remote", "Remote"
        HYBRID = "hybrid", "Hybrid"

    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    jobType = models.CharField(
        max_length=255, choices=JOB_TYPE.choices, default=JOB_TYPE.FULL_TIME
    )
    jobLocationType = models.CharField(
        max_length=255,
        choices=JOB_LOCATION_TYPE.choices,
        default=JOB_LOCATION_TYPE.ONSITE,
    )
    url = models.URLField(max_length=1500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def to_string(self):
        return f"(id: {self.id}, title: {self.title}, place: {self.place}, companyName: {self.companyName}, description: {self.description}, jobType: {self.jobType}, )"
