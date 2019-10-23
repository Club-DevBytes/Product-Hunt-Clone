from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField()
    body = models.TextField(blank=True, null=True)
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(
        'Manufacturer', null=True, on_delete=models.SET_NULL
    )



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# # Method for indexing the model
#     def indexing(self):
#         obj = PostDocument(
#             meta={'id': self.id},
#             title=self.title,
#             body=self.body
#         )
#         # obj.save()
#         return obj.to_dict(include_meta=True)
