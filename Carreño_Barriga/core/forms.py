from dataclasses import fields
from django import forms
from .models import *



class EmpresaForm(forms.ModelForm):
     class Meta:
            model=Empresa
            fields = ['nombre', 'direccion','contacto']

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class SucursalForm(forms.ModelForm):
        class Meta:
            model=Sucursal
            fields = ['nombre', 'direccion','contacto']

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class DoctorForm(forms.ModelForm):
        class Meta:
            model=Doctor
            fields = ['nombre', 'contacto']

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class PacienteForm(forms.ModelForm):
            class Meta:
                model=Paciente
                fields = ['nombreCompleto','Doctor','direccion','telefono','tipoSangre','estatura','diagnostico']
              
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class VisitaForm(forms.ModelForm):
            class Meta:
                model=Visita
                fields= ['Doctor','Paciente','fecha','Motivo']

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class ProductosForm(forms.ModelForm):
            class Meta:
                model=Productos
                fields= ['nombre','estado']

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class RecetaForm(forms.ModelForm):
            class Meta:
                    model=Receta
                    fields= ['Visita','Producto','cantidad']
                    
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for field in iter(self.fields):
                    self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })