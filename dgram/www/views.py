from django.core.files.storage import FileSystemStorage, default_storage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from eth_api.accounts import get_accounts_balances
from eth_api.listing import get_list
from eth_api.tip import tip
from eth_api.uploader import upl_file
from .forms import UploadForm, TipForm


def save_file(request, key):
    my_file = request.FILES[key]
    fs = FileSystemStorage()
    filename = fs.save(my_file.name, my_file)
    return default_storage.path(filename)


def upload_form(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            f_path = save_file(request, 'f_path')
            description = form.data['description']
            who_ami = int(form.data['who_ami'])

            upl_file(path_to_file=f_path,
                     description_of_file=description,
                     who_ami=who_ami)

            return HttpResponseRedirect(reverse(upload_form))
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


def tip_form(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            value = int(form.data['value'])
            imd_n = int(form.data['imd_n'])
            who_ami = int(form.data['who_ami'])
            tip(imd_n=imd_n,
                value=value,
                who_ami=who_ami)
            return HttpResponseRedirect(reverse(tip_form))
    else:
        form = TipForm()

    return render(request, 'tip.html', {'form': form})


def im_list(request):
    if request.method == 'GET':
        data = get_list()
        if len(data) > 0:
            cols = data[0].keys()
            vals = [d.values() for d in data]
            return render(request, "im_list.html", {'allTriples': vals, 'cols': cols})
        return render(request, 'im_list.html', )


def acc_list(request):
    if request.method == 'GET':
        data = get_accounts_balances()
        if len(data) > 0:
            return render(request, "acc_list.html", {'allTriples': data, 'cols': ['acc', 'balance']})
        return render(request, 'acc_list.html', )
