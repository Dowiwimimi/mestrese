# lista de ciudades con las que voy a trabajar 
ciudades = ["Guayaquil", "Samborondón", "Loja"]

# la matriz 3D que usare para guardar las temperaturas
temperaturas = [
    # Datos de Guayaquil
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    # Datos de Samborondón
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    # Datos de Loja
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 21}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 19}
        ]
    ]
]

# funcion para sacar los promedios de temperatura
def calcular_promedio_temperaturas(temperaturas, ciudades):
    """Saca el promedio de temperaturas por ciudad y semana, y lo muestra"""
    for i, ciudad in enumerate(temperaturas):
        for j, semana in enumerate(ciudad):
            suma = 0
            for dia in semana:
                suma += dia["temp"]
            promedio = suma / 7
            print(f"Promedio en {ciudades[i]} para la semana {j+1}: {promedio:.1f}°C")

# y se va a calcular y ver los promedios
print("Calculando promedios...")
calcular_promedio_temperaturas(temperaturas, ciudades)
