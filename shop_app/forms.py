from django import forms
from psutil import users
from .models import Order, Customer, Product
from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email"]

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100)


class ProductForm(forms.ModelForm):

    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))


    class Meta:
        model = Product
        fields = ["title", "slug", "category", "image", "marked_price",
                  "selling_price", "description", "warranty", "return_policy"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nhập tên sản phẩm"
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nhập đường dẫn đến sản phẩm"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "marked_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Giá niêm yết"
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Giá khuyến mãi"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Mô tả sản phẩm",
                "rows": 5
            }),
            "warranty": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Thông tin bảo hành"
            }),
            "return_policy": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Chính sách đổi trả"
            }),

        }


class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter the email used in customer account..."
    }))

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError(
                "Customer with this account does not exists..")
        return e
