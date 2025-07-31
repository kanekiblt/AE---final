
import { Component, OnInit } from '@angular/core';
import { HorarioService, Service } from './horario.service';

@Component({
    selector: 'app-horario',
    templateUrl: './horario.component.html',
    styleUrls: ['./horario.component.css']
})

export class HorarioComponent implements OnInit {
    horarios: Service[] = [];
    mensaje: string = '';
    cargando: boolean = false;

    constructor(private horarioService: HorarioService) { }

    ngOnInit(): void {
        this.obtenerHorarios();
    }
    

    obtenerHorarios(): void {
        this.cargando = true;
        this.horarioService.asignarHorarios().subscribe({
            next: response => {
                this.mensaje = 'Horarios asignados correctamente';
                this.cargando = false;
                this.obtenerHorarios();
            },
            error: error => {
                this.mensaje = 'Error al asignar horarios';
                this.cargando = false;
            },
            complete: () => this.cargando = false
        });
    }

    asignarHorarios(): void {
        this.cargando = true;
        this.horarioService.asignarHorarios().subscribe(response => {
            this.mensaje = 'Horarios asignados correctamente';
            this.cargando = false;
            this.obtenerHorarios();
        }, error => {
            this.mensaje = 'Error al asignar horarios';
            this.cargando = false;
        });
    }
}
