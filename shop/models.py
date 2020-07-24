from django.db import models
from askdjango.utils import uuid_name_upload_to
from django.shortcuts import reverse


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'<{self.pk}> {self.name}'

    class Meta:
        ordering=['id']

    def get_absolute_url(self):
        return reverse('shop:item_detail',kwargs={'pk': self.pk})



