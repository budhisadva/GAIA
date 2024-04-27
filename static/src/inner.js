import { opcionesListener } from './Eventos/opciones.js';
import { listarPosts } from './VerActividad/funciones.js';

const renderApp = () => {
  opcionesListener();
}

window.onload = () => {
  renderApp();
  let feed = document.getElementById('posts');
  if (feed) {
    listarPosts(feed);
  }
}
