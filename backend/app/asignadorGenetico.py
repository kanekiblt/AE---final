import random
from datetime import time
from collections import defaultdict

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
horas = [time(hour=h) for h in range(7, 21)]

def calcular_fitness(asignaciones):
    puntaje = 0
    penalizacion = 0
    cursos_asignados = []
    lab_cargas = defaultdict(int)

    for (curso, lab, dia, hora) in asignaciones:
        # Restricción: Software requerido
        if curso.software_requerido not in lab.software.all():
            penalizacion += 10

        # Restricción: Capacidad del laboratorio
        if curso.total_alumnos > lab.capacidad:
            penalizacion += (curso.total_alumnos - lab.capacidad) * 2

        # Restricción: Disponibilidad del profesor
        bloque = f"{dia}-{hora.strftime('%H:%M')}"
        if bloque not in curso.profesor.disponibilidad:
            penalizacion += 5

        # Restricción: No solapamientos
        for (c2, l2, d2, h2) in cursos_asignados:
            if d2 == dia and h2 == hora:
                if lab.id == l2.id:
                    penalizacion += 20  # Mismo laboratorio
                if curso.profesor.id == c2.profesor.id:
                    penalizacion += 20  # Mismo profesor

        puntaje += curso.peso * 2  # Puntaje por asignación exitosa

        # Restricción: Prerequisitos
        if curso.prerequisito:
            for (c2, _, d2, h2) in cursos_asignados:
                if c2.id == curso.prerequisito.id:
                    if dias.index(d2) > dias.index(dia) or (d2 == dia and h2 >= hora):
                        penalizacion += 10  # Prerequisito después

        # Control de carga por laboratorio
        lab_cargas[(lab.id, dia)] += 1
        if lab_cargas[(lab.id, dia)] > 3:
            penalizacion += 5

        cursos_asignados.append((curso, lab, dia, hora))

    return puntaje - penalizacion

def mutar(asignaciones, cursos, laboratorios):
    nuevo = list(asignaciones)
    idx = random.randint(0, len(nuevo) - 1)
    curso = nuevo[idx][0]
    
    # Busca una asignación válida
    for _ in range(10):  # Máximo 10 intentos
        lab = random.choice(laboratorios)
        dia = random.choice(dias)
        hora = random.choice(horas)
        
        if (curso.software_requerido in lab.software.all() and 
            curso.total_alumnos <= lab.capacidad):
            nuevo[idx] = (curso, lab, dia, hora)
            break
            
    return nuevo

def hill_climbing(cursos, laboratorios, iteraciones=1000):
    asignaciones = [(c, random.choice(laboratorios), random.choice(dias), random.choice(horas)) 
                   for c in cursos]
    mejor = asignaciones
    mejor_fitness = calcular_fitness(mejor)

    for _ in range(iteraciones):
        vecino = mutar(mejor, cursos, laboratorios)
        fitness_vecino = calcular_fitness(vecino)
        if fitness_vecino > mejor_fitness:
            mejor = vecino
            mejor_fitness = fitness_vecino

    return mejor

def asignar_horarios_geneticos():
    from app.models import Curso, Laboratorio
    
    cursos = list(Curso.objects.all().prefetch_related(
        'profesor', 'software_requerido'
    ).order_by('-peso'))
    
    laboratorios = list(Laboratorio.objects.all().prefetch_related('software'))
    
    mejor_solucion = hill_climbing(cursos, laboratorios)
    
    return [{
        'curso': curso.id,
        'laboratorio': lab.id,
        'dia': dia,
        'hora_inicio': hora.strftime('%H:%M:%S')
    } for (curso, lab, dia, hora) in mejor_solucion]