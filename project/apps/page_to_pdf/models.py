from django.db import models


class Page(models.Model):
    class UrlTypeChoice(models.TextChoices):
        DOCUMENT = "document", "Document"
        BLOG = "blog", "Blog"
        OTHER = "other", "Other"

    name = models.CharField("Name")
    url = models.URLField("URL Field")
    url_type = models.CharField("URL type", choices=UrlTypeChoice.choices)
