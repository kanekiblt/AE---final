import { Component, OnInit } from '@angular/core';
import { HorarioService, Horario } from './horario.service';

@Component({
    selector: 'app-horario',
    templateUrl: './horario.component.html',
    styleUrls: ['./horario.component.css']
})
export class HorarioComponent implements OnInit {
    horarios: Horario[] = [];
    cargando = false;
    mensaje = '';
    tipoMensaje: 'success' | 'error' | 'info' = 'info';

    constructor(private horarioService: HorarioService) { }

    ngOnInit(): void {
        this.cargarHorarios();
    }

    cargarHorarios(): void {
        this.cargando = true;
        this.horarioService.getHorarios().subscribe({
            next: (horarios) => {
                this.horarios = horarios;
                this.cargando = false;
            },
            error: (err) => {
                this.mostrarMensaje('Error al cargar horarios', 'error');
                this.cargando = false;
            }
        });
    }

    generarHorarios(): void {
        this.cargando = true;
        this.horarioService.generarHorarios().subscribe({
            next: (response) => {
                this.mostrarMensaje(response.message, 'success');
                if (response.data) {
                    this.horarios = response.data;
                } else {
                    this.cargarHorarios();
                }
                this.cargando = false;
            },
            error: (err) => {
                this.mostrarMensaje(err.error?.message || 'Error generando horarios', 'error');
                this.cargando = false;
            }
        });
    }

    private mostrarMensaje(mensaje: string, tipo: 'success' | 'error' | 'info'): void {
        this.mensaje = mensaje;
        this.tipoMensaje = tipo;
        setTimeout(() => this.mensaje = '', 5000);
    }
}