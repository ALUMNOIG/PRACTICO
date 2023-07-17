from django.shortcuts import render

# Create your views here.
import numpy as np

# Definimos ingresar y valores y diccionario que nos retorna a ingresado.html

def ingresar(request):
    range_values = range(0, 10)  # Variable con el rango de valores del 1 al 10
    context = {'range_values': range_values} # Crea diccionario con los valores
    return render(request, 'ingresado.html', context) # Para solicitud ingresar, llama plantilla html , diccionario


# Definimos suma y generamos la matriz aleatoria
def suma(request):
    i = request.POST.get('n', 0)
    if request.method == 'POST':
        try:
            n = int(request.POST.get('n'))
            if n < 1 or n > 9:
                raise ValueError("N debe ser un número entero entre 1 y 9.")
        except ValueError as e:
            range_values = range(0, 10)
            context = {
                'range_values': range_values,
                'error': str(e)
            }
            return render(request, 'ingresado.html', context)

        matriz = np.random.randint(10, size=(n, n))
        suma_filas = matriz.sum(axis=1)
        suma_columnas = matriz.sum(axis=0)
        context = {
            'i': i,
            'matriz': matriz,
            'suma_filas': suma_filas,
            'suma_columnas': suma_columnas
        }
        return render(request, 'suma.html', context)
