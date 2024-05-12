import { opcionesListener } from './Eventos/opciones.js';
import { listarPosts } from './VerActividad/funciones.js';
import { actualizarCuenta } from './ActualizarCuenta/funciones.js';

const renderApp = () => {
  opcionesListener();
}

window.onload = () => {
  renderApp();
  let feed = document.getElementById('posts');
  if (feed) {
    listarPosts(feed);
  }
  let actualizar = [...document.getElementsByClassName('actualizar__titulo')][0];
  if (actualizar) {
    actualizarCuenta();
  }
}
