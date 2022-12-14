from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Projektas
# REGISTER IMPORTS
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.db.models import Q
from .forms import MyForm
from django.core.paginator import Paginator
# REGISTER IMPORTS END
from django.contrib.auth.mixins import UserPassesTestMixin

from django.utils.translation import gettext as _




# Create your views here.
def login(request):
  return render(request, 'login.html')

def index(request):

    context = {
        "projektai": Projektas.objects.all().count(),
    }
    return render(request,'index.html', context=context)

def projektai(request):
    paginator = Paginator(Projektas.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_projects = paginator.get_page(page_number)


    context = {
        # "projektai": Projektas.objects.all(),
        'projektai': paged_projects
    }
    return render(request,'projektai.html',context=context)
def projektasView(request, projektas_id):

    vienas_projektas = get_object_or_404(Projektas, pk=projektas_id)
    return render(request,'projektas.html',{'projektas':vienas_projektas})

@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            # if User.objects.filter(username=username).exists():
            #     messages.error(request, f'Vartotojo vardas {username} užimtas!')
            #     return redirect('register')
            # else:
            # tikriname, ar nėra tokio pat email
            if User.objects.filter(email=email).exists():
                messages.error(request, _(f'Vartotojas su el. paštu {email} jau užregistruotas!'))
                return redirect('register')
            else:
                # jeigu viskas tvarkoje, sukuriame naują vartotoją
                User.objects.create_user(username=username, email=email, password=password)
                messages.info(request, _(f'Vartotojas {username} užregistruotas!'))
                return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


from django.contrib.auth.mixins import LoginRequiredMixin


class UserProjektasListView(LoginRequiredMixin, generic.ListView):
    model = Projektas
    template_name = 'user_projektai.html'
    paginate_by = 3

    def get_queryset(self):
        return Projektas.objects.filter(vadovas_user=self.request.user)

class UserProjektasUpdateView(LoginRequiredMixin,UserPassesTestMixin, generic.UpdateView):
    model = Projektas
    form_class = MyForm
    # fields = ['pavadinimas','pradzios_data','pabaigos_data', 'klientas_id', 'vadovas_user','darbuotojas_id','darbas_id','saskaita_id','nuotrauka','aprasymas']
    success_url = '/user-project/'
    template_name = 'user-project-form.html'

    def form_valid(self, form):
        form.instance.vadovas_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        projektas = self.get_object()
        return self.request.user == projektas.vadovas_user
class UserProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Projektas
    success_url = '/user-project/'
    template_name = 'user-project-delete.html'

    def test_func(self):
        projektas = self.get_object()
        return self.request.user == projektas.vadovas_user



def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Projektas.objects.filter(Q(pavadinimas__icontains=query) | Q(pradzios_data__icontains=query))
    return render(request, 'search.html', {'projektas': search_results, 'query': query})


# class PersonCreateView(CreateView):
#     model = Projektas
#     fields = ('pavadinimas', 'pradzios_data', 'pabaigos_data', 'klientas_id')
#     # template_name = "add-listing.html"
@login_required
def addlisting (request):

    # if request.method == "POST":
    #     pavadinimas = request.POST['pavadinimas']
    #     prad_data = request.POST['prad-data']
    #     pab_data= request.POST['pab-data']
    #     klientas = request.POST['klientas']
    #     vadovas = request.POST['vadovas']
    #     darbuotojas = request.POST ['darbuotojas']
    #     darbas = request.POST ['darbas']
    #     saskaita = request.POST ['saskaita']
    #     aprasymas = request.POST ['aprasymas']
    #     nuotrauka = request.POST ['nuotrauka']

    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Projektas Irasytas")
    else:
        form = MyForm()
        messages.info(request, "Uzpildykite visus privalomus laukus")


    return render(request, 'add-listing.html', {'form': form} )


    # context = {
    #     "projektai": Projektas.objects.all()
    # }
    #
    # return render(request, 'add-listing.html', context=context)

# def uploadok(request):
#     return HttpResponse(' upload successful')