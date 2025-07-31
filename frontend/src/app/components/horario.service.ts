import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Service {

    curso: {
        nombre : String;
        profesor : {nombre : String};
        software_requerido : {nombre : String}
    };

    laboratorio: {
        nombre : String;
    };

    dia: String;
    hora_inicio: String;
}

@Injectable({
    providedIn: 'root' 
})

export class HorarioService {

    private API_URL = 'http://localhost:8000/api';

    constructor(private http: HttpClient) { }

    asignarHorarios(): Observable<any> {
        return this.http.post(`${this.API_URL}/asignar/`, {});
    }

    addHorario(horario: Service): Observable<Service> {
        return this.http.post<Service>(this.API_URL, horario);
    }

    deleteHorario(id: number): Observable<void> {
        return this.http.delete<void>(`${this.API_URL}${id}/`);
    }

}