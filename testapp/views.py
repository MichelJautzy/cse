from django.shortcuts import render, HttpResponse
from .models import ModelTest
from .forms import MonFormulaire, MonFormulaireModelTest
from django.views.generic.edit import CreateView

def my_view(request, id):
    # via manager 
    all_models = ModelTest.objects.all()
    # paramètre via la requête
    print(request.method)
    #field = request.GET.get('filter', None)

    # via manager en mode brute
    req = "select * from testapp_modeltest where id= %s"
    sql_all_models = ModelTest.objects.raw(raw_query=req, params=[id])

    #print(all_models)
    #for o in all_models:
        #print(o.mon_champ)

    return render(
        request,
        "my-view-template.html", 
        context={
            'elemtest': "hello world",
            'modeltest2': sql_all_models, 
            'modeltest': all_models})
    #return HttpResponse("ici c'est Paris")

def form_view(request):
    form = MonFormulaire()
    if request.method == 'POST':
        form = MonFormulaire(request.POST)
        if form.is_valid():
            mon_champ = form.cleaned_data['champ_form']
            obj = ModelTest()
            obj.mon_champ = mon_champ
            obj.save()
            return render(request, "form-template.html", {'myform': form})
        else:
            return render(request, "form-template.html", {'myform': form})
    return render(request, "form-template.html", {'myform': form})

def form_view_model(request):
    form = MonFormulaireModelTest()
    if request.method == 'POST':
        form = MonFormulaireModelTest(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "form-template.html", {'myform': form})
    return render(request, "form-template.html", {'myform': form})

class ModelTestCreateView(CreateView):
    model = ModelTest
    fields = "__all__"
    template_name = "form-template-class.html"