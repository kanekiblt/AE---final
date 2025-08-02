import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Horario {
    id: number;
    curso: {
        id: number;
        nombre: string;
        profesor: {
            id: number;
            nombre: string;
        };
        software_requerido: {
            id: number;
            nombre: string;
        };
    };
    laboratorio: {
        id: number;
        nombre: string;
        capacidad: number;
        software: {
            id: number;
            nombre: string;
        }[];
    };
    dia: string;
    hora_inicio: string;
}

@Injectable({
    providedIn: 'root'
})
export class HorarioService {
    private readonly API_URL = 'http://localhost:8000/api';

    constructor(private http: HttpClient) { }

    getHorarios(): Observable<Horario[]> {
        return this.http.get<Horario[]>(`${this.API_URL}/horarios/`);
    }

    generarHorarios(): Observable<{status: string, message: string, data?: Horario[]}> {
        return this.http.post<{status: string, message: string, data?: Horario[]}>(
            `${this.API_URL}/horarios/generar/`, 
            {}
        );
    }

    getHorario(id: number): Observable<Horario> {
        return this.http.get<Horario>(`${this.API_URL}/horarios/${id}/`);
    }

    actualizarHorario(id: number, datos: Partial<Horario>): Observable<Horario> {
        return this.http.patch<Horario>(`${this.API_URL}/horarios/${id}/`, datos);
    }

    eliminarHorario(id: number): Observable<void> {
        return this.http.delete<void>(`${this.API_URL}/horarios/${id}/`);
    }
}