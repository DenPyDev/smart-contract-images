from django import forms

from eth_api.accounts import get_accounts
from eth_api.listing import image_counter


def get_img_choices():
    return [(i, i) for i in range(1, image_counter() + 1)]


def get_acc_choices():
    return list(enumerate(get_accounts()))


class UploadForm(forms.Form):
    f_path = forms.FileField()
    description = forms.CharField(label='description', max_length=500)
    who_ami = forms.CharField(label='who_ami', widget=forms.Select(choices=get_acc_choices()))

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['who_ami'] = forms.CharField(label='who_ami', widget=forms.Select(choices=get_acc_choices()))


class TipForm(forms.Form):
    value = forms.IntegerField(label='value')
    imd_n = forms.IntegerField(label='imd_n', widget=forms.Select(choices=get_img_choices()))
    who_ami = forms.CharField(label='who_ami', widget=forms.Select(choices=get_acc_choices()))

    def __init__(self, *args, **kwargs):
        super(TipForm, self).__init__(*args, **kwargs)
        self.fields['imd_n'] = forms.IntegerField(label='imd_n', widget=forms.Select(choices=get_img_choices()))
        self.fields['who_ami'] = forms.CharField(label='who_ami', widget=forms.Select(choices=get_acc_choices()))
