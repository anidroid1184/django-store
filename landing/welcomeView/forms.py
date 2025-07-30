from django import forms
from django.contrib.auth.models import User
from django.contrib import messages as msg


class Registro(forms.Form):
    """
    Formulario para el registro de usuarios.
    Este formulario hereda de forms.Form y define los campos necesarios
    para crear un nuevo usuario en el sistema.
    Attributes:
        username (CharField): Campo para el nombre de usuario.
        email (EmailField): Campo para el correo electrónico.
        password (CharField): Campo para la contraseña.
        password2 (CharField): Campo para confirmar la contraseña.
    """
    username = forms.CharField(
        required=True,
        min_length=8,
        max_length=40,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs=(
            {
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre de usuario',
                }
        )))
    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        max_length=254,
        widget=forms.EmailInput(attrs=(
            {
                'class': 'form-control',
                'placeholder': 'example@domain.com',
            }
        )))
    password = forms.CharField(
        required=True,
        min_length=8,
        max_length=40,
        label='Contraseña',
        widget=forms.PasswordInput(attrs=(
            {
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
            }
        )))
    password2 = forms.CharField(
        required=True,
        min_length=8,
        max_length=40,
        label='Contraseña',
        widget=forms.PasswordInput(attrs=(
            {
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
            }
        )))

    # es importante que el nombre de la función sea así
    # modificamos un método de la clase forms.Form
    # para validar el campo username
    def clean_username(self):
        """
        Método para validar el campo username.
        Este método se llama automáticamente al validar el formulario.
        Raises:
            ValidationError: Si el nombre de usuario ya está en uso.
        """
        username = self.cleaned_data.get('username')

        # verificar si ya hay otro usuario con ese nombre
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya creado, ingrese otro')

        # si no existe el nombre, se retorna el usuario
        return username

    def clean_email(self):
        """
        Método para validar el campo email.
        Este método se llama automáticamente al validar el formulario.
        Raises:
            ValidationError: Si el email ya está en uso.
        """
        email = self.cleaned_data.get('email')

        # verificar si ya hay otro usuario con ese nombre
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'El email {email}ya está siendo usado, ingrese otro'
                )

        # si no existe el nombre, se retorna el usuario
        return email

    def clean(self):
        """
        Método para validar que las contraseñas coincidan.
        Este método se llama automáticamente al validar el formulario.
        Raises:
            ValidationError: Si las contraseñas no coinciden.
        """
        # heredamos los metodos y la inicialización de la clase padre
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            # se agregara un error si las contraseñas no son iguales
            self.add_error('password2', 'Las contraseñas no coinciden')

    # almacenar usuarios creados
    def save(self):
        """
        Crea un usuario con los datos del formulario depurados.
        Returns:
            User: El usuario creado.
        """
        return User.objects.create_user(
            # retornamos los datos del formulario depurados
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
