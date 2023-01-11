from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView

# Create your views here.
def index(request):
    return render(request, "coding/index.html")

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")     # 오버라이딩: 기존 클래스를 상속받아서 기존 코드를 수정.
