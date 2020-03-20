from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    city = forms.CharField(label='City', max_length=25)
    CHOICES = [('yes', 'Yes, I am happy!'),
               ('no', 'No, I am not happy.')]
    is_happy = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean(self):
        super(ContactForm, self).clean()
        name = self.cleaned_data.get('name')
        city = self.cleaned_data.get('city')

        if len(name) > 30:
            self._errors['name'] = self.error_class(['Maximum 30 characters.'])

        if len(city) > 25:
            self._errors['city'] = self.error_class(['Maximum 25 characters.'])

        return self.cleaned_data