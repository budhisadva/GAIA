const url = 'http://localhost:8000/solicitud/';

const solicitarUsuarios = async () => {
  let datos = await fetch(url+'usuarios/');
  datos = await datos.json();
  return datos;
}

const despliegaMenu = (lista, objetivo) => {
  let menu = document.getElementsByClassName('buscar__menu')['0'];
  menu.innerHTML = '';
  if (objetivo != '') {
    let usuarios = lista.usuarios;
    usuarios = usuarios.filter((usuario) => usuario.nombre.toUpperCase().includes(objetivo.toUpperCase()));
    usuarios.forEach(usuario => {
      if (usuario.enviada) {
        menu.innerHTML += `
          <div class="buscar__perfil">
            <div class="buscar__contenedor">
              <div class="buscar__perfil__foto"></div>
              <span class="buscar__perfil__nombre">${usuario.nombre}</span>
            </div>
            <button type="button">Solicitud enviada</button>
          </div>
        `;
      } else {
        menu.innerHTML += `
          <div class="buscar__perfil">
            <div class="buscar__contenedor">
              <div class="buscar__perfil__foto"></div>
              <span class="buscar__perfil__nombre">${usuario.nombre}</span>
            </div>
            <a href="/solicitud/enviar/${usuario.id}/"><button type="button">Enviar solicitud</button></a>
          </div>
        `;
      }
    });
  }
}

const busquedaListener = async () => {
  let lista = await solicitarUsuarios();
  let busqueda = [...document.getElementsByClassName('cabecera__busqueda')][0];
  busqueda.addEventListener('input', (e) => {
    let entrada = document.getElementsByClassName('cabecera__busqueda')['0'];
    despliegaMenu(lista, entrada.value);
  });
  busqueda.addEventListener('focus', (e) => {
    let menu = document.getElementsByClassName('buscar__menu')['0'];
    menu.toggleAttribute('hidden');
  });
}

export { busquedaListener };
