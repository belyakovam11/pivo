from django.db import models


class BuyerRegistration(models.Model):
    PRIVATE = "private"
    WHOLESALE = "wholesale"
    BUYER_TYPES = [
        (PRIVATE, "Частный покупатель"),
        (WHOLESALE, "Оптовый покупатель"),
    ]

    buyer_type = models.CharField(max_length=20, choices=BUYER_TYPES)
    name = models.CharField("Имя и фамилия", max_length=160)
    contact = models.CharField("Телефон или email", max_length=160)
    company = models.CharField("Название компании", max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} — {}".format(self.get_buyer_type_display(), self.name)


class EventRegistration(models.Model):
    event_title = models.CharField("Мероприятие", max_length=200)
    name = models.CharField("Имя и фамилия", max_length=160)
    contact = models.CharField("Телефон или email", max_length=160)
    guests = models.PositiveSmallIntegerField("Количество участников", default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} — {}".format(self.event_title, self.name)


class ProjectApplication(models.Model):
    name = models.CharField("Имя или команда", max_length=160)
    contact = models.CharField("Телефон или email", max_length=160)
    idea = models.TextField("Идея для пива")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Заявка: {}".format(self.name)
