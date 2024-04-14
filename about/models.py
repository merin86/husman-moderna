from django.db import models

# AboutPage model to store content for the About page on the website


class AboutPage(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Page Content"
