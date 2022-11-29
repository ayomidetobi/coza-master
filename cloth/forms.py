from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError



PAYMENT_CHOICES = (
    ('F', 'Flutterwave'),
    ('P', 'Paystack')
)

def validator_fields(value):
        if  len(value) <= 0:
            raise ValidationError('this field is required')
        else:
            return value


class CheckoutForm(forms.Form):
    
    shipping_address = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class': ' stext-111 w-100 cl8 plh3 size-111 p-lr-15',
        'placeholder':'Apartment or suite'
        }),label='',validators=[validator_fields])
        
    shipping_address2 = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class': ' stext-111 w-100 cl8 plh3 size-111 p-lr-15',
        'placeholder':'Apartment or suite'
        }),label='',validators=[validator_fields])
    shipping_country = CountryField(blank_label='Shipping Country').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'rs1-select2 rs2-select2 w-100 bor8 bg0 stext-111 cl8 plh3 size-111 p-lr-15 m-t-9',
            
        }), label='',validators=[validator_fields])
    shipping_zip = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'class': ' stext-111 w-100 cl8 plh3 size-111 p-lr-15',
        'placeholder':'Postcode / Zip'
        }), label='',validators=[validator_fields])

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': ' stext-104 cl2 plh4 size-117 bor13 p-lr-20 m-r-10 m-t-16',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


# class PaymentForm(forms.Form):
#     stripeToken = forms.CharField(required=False)
#     save = forms.BooleanField(required=False)
#     use_default = forms.BooleanField(required=False)