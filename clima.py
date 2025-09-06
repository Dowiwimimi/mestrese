temperaturas = [
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [   # Samborondón
        [   # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Loja
        [   # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 21}
        ],
        [   # La Semana 3
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ],
        [   # La Semana 4
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

for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = suma / 7
        print(f"Promedio de temperaturas para {ciudad[i]} en la semana {j+1}: {promedio:.1f}")
