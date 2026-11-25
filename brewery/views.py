from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import BuyerRegistrationForm, EventRegistrationForm, ProjectApplicationForm


def home(request):
    return render(request, "brewery/index.html")


@require_POST
def register_buyer(request):
    form = BuyerRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Регистрация прошла успешно. Мы скоро свяжемся!")
    else:
        messages.error(request, "Проверьте данные регистрации и попробуйте снова.")
    return redirect("home")


@require_POST
def register_event(request):
    form = EventRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Вы записаны на мероприятие!")
    else:
        messages.error(request, "Не удалось записать вас. Проверьте данные формы.")
    return redirect("home")


@require_POST
def submit_project(request):
    form = ProjectApplicationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Заявка отправлена. Спасибо за идею!")
    else:
        messages.error(request, "Проверьте данные заявки и попробуйте снова.")
    return redirect("home")
