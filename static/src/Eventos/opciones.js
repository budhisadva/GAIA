const opcionesListener = () => {
  let perfil = [...document.getElementsByClassName('perfil__nombre')][0];
  perfil.addEventListener('click', (e) => {
    let opciones = [...document.getElementsByClassName('opciones')][0];
    opciones.toggleAttribute('hidden');
  });
}

export { opcionesListener };
