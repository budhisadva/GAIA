import { opcionesListener } from './Eventos/opciones.js';
import { actualizarCuenta } from './ActualizarCuenta/funciones.js';

const renderApp = () => {
  opcionesListener();
}

window.onload = () => {
  renderApp();
  let actualizar = [...document.getElementsByClassName('actualizar__titulo')][0];
  if (actualizar) {
    actualizarCuenta();
  }
}
