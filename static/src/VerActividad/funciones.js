const url = 'http://localhost:8000/verActividad/';

/**
 * Realiza un peticion al servidor para obtener las
 * publicaciones del usuario
 */
const obtenerPost = async () => {
  let publicaciones = await fetch(url+'publicaciones');
  publicaciones = await publicaciones.json();
  return publicaciones;
}

const listarPosts = async (contenedor) => {
  let publicaciones = await obtenerPost();
  if (!publicaciones.post.length) {
    contenedor.innerHTML = `
    <div class="vacio">
      <p class="vacio__titulo">No tienes publicaciones nuevas</p>
      <div class="vacio__icono">
        <i class="bi bi-clock-history"></i>
      </div>
    </div>
    `;
  }
}

export { listarPosts };
