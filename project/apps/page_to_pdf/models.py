from django.db import models


class Url(models.Model):
    name = models.CharField("Name", max_length=512)

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"

    def __str__(self):
        return self.name


class Page(models.Model):
    class UrlTypeChoice(models.TextChoices):
        DOCUMENT = "document", "Document"
        BLOG = "blog", "Blog"
        OTHER = "other", "Other"

    name = models.CharField("Name")
    url_type = models.CharField("URL type", choices=UrlTypeChoice.choices)
    url = models.ManyToManyField(Url, verbose_name="Url", related_name="page")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.name
