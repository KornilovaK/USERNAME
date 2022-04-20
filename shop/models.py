from django.db import models


class Table(models.Model):
    number = models.IntegerField(blank=False)
    datetime = models.DateTimeField(blank=False)

    def serialize(self):
        return {
            "number": self.number,
            "datetime": self.datetime.strftime('%Y-%m-%d %H:%M'),
        }


class Reserve(models.Model):
    table = models.ForeignKey("Table", on_delete=models.CASCADE, related_name="tables", blank=False)
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=60, blank=False)

    def serialize(self):
        return {
            "id": self.id,
            "table": self.table,
            "name": self.name,
            "email": self.email,
        }


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category


class Menu(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=64)
    cost = models.IntegerField()

    def serialize(self):
        return {
            "id": self.id,
            "category": self.category,
            "name": self.name,
            "cost": self.cost,
        }