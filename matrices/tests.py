from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ViewsTest(TestCase):
    def test_ingresar_view(self):
        # Simula una solicitud GET a la vista 'ingresar'
        response = self.client.get(reverse('ingresar'))
        
        # Verifica que la respuesta tenga un código de estado 200 (éxito)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que la plantilla utilizada sea la correcta
        self.assertTemplateUsed(response, 'ingresado.html')
        
    def test_suma_view(self):
        # Simula una solicitud POST a la vista 'suma'
        response = self.client.post(reverse('suma'), {'n': 3})
        
        # Verifica que la respuesta tenga un código de estado 200 (éxito)
        self.assertEqual(response.status_code, 200)
        
        # Verifica que la plantilla utilizada sea la correcta
        self.assertTemplateUsed(response, 'suma.html')
        
        # Verifica que los datos de la respuesta sean los esperados
        self.assertIn('i', response.context)
        self.assertIn('matriz', response.context)
        self.assertIn('suma_filas', response.context)
        self.assertIn('suma_columnas', response.context)