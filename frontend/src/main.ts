import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

// Configuración para modo producción
if (environment.production) {
  enableProdMode();
}

// Inicialización de la aplicación
platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch(err => console.error('Error al iniciar la aplicación:', err));