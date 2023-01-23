from django.shortcuts import render
from django.http import HttpResponse
from . models import user_acc
from django.views.generic import TemplateView, ListView
# Create your views here.


class AccountsView(TemplateView):
    template_name = 'accounts/user.html'

    def list(request):
        all_accs = user_acc.objects.all()
        return render(request,'accounts/accounts_list.html',{'user_acc': all_accs})

    def user(request,pk):
        users = user_acc.objects.get(pk=pk)
        return render(request, 'accounts/user.html', {'user_acc':users})