import { BrowserModule } from "@angular/platform-browser";
import { HttpClientModule } from "@angular/common/http";
import { HorarioComponent } from "./components/horario.component";
import { FormsModule } from "@angular/forms";
import { NgModule } from "@angular/core";

@NgModule({
    declarations: [
        HorarioComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpClientModule

    ],
    bootstrap: [HorarioComponent]
})
export class AppModule { }
