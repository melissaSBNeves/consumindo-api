from django import forms

class HolidayForm(forms.Form):
    ano = forms.IntegerField(label=False)

    def __init__(self, *args, **kwargs):
        super(HolidayForm, self).__init__(*args, **kwargs)

        self.fields['ano'].widget.attrs['placeholder'] = 'Pesquise o ano...'

