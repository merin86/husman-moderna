from django.db import models


class AboutPage(models.Model):
    """
    AboutPage model to store content for the About page on the website
    """
    content = models.TextField()

    def __str__(self):
        return "About Page Content"
