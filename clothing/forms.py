from django import forms



SIZES_CHOICES = (
    ('x-small', 'X-Small'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('x-large', 'X-Large'),
)

class SizeForm(forms.Form):
    sizes = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=SIZES_CHOICES)