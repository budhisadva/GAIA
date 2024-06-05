import { opcionesListener } from './Eventos/opciones.js';
import { busquedaListener } from './Eventos/busqueda.js';
import { actualizarCuenta } from './ActualizarCuenta/funciones.js';

const renderApp = () => {
  opcionesListener();
  busquedaListener();
}

window.onload = () => {
  renderApp();
  let actualizar = [...document.getElementsByClassName('actualizar__titulo')][0];
  if (actualizar) {
    actualizarCuenta();
  }
}
