this.http.get('/api/horarios/', {}).subscribe(horarios => {
    this.horario = horarios;
});

// este va hacer una peticion para ver horarios asignados