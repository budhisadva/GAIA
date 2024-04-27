const validarNombre = (nombre) => {
  return nombre.value !== "";
}

const validarCorreo = (correo, confirmaCorreo) => {
  if (correo.value === "" || confirmaCorreo.value === "") {
    return false;
  } else if (correo.value !== confirmaCorreo.value) {
    return false;
  }
  return true;
}

const validarGenero = (listaValores) => {
  let genero = [];
  listaValores.forEach(x => {
    if (x.checked) genero.push(x.value);
  });
  if (!genero.length) return false;
  return true;
}

const validarContrasena = (contrasena, confirmaContrasena) => {
  if (contrasena.value === "" || confirmaContrasena.value === "") {
    return false;
  } else if (contrasena.value !== confirmaContrasena.value) {
    return false;
  }
  return true;
}

const crearCuenta = (formulario) => {
  formulario.onsubmit = (e) => {
    e.preventDefault();
    if (!validarNombre(formulario.nombre)) {
      alert('Ingrese un nombre');
      return;
    }
    if (!validarCorreo(formulario.correo, formulario.correo_c)) {
      alert('Los correos no coinciden');
      return;
    }
    if (!validarGenero([...formulario.genero])) {
      alert('Ingrese un género');
      return;
    }
    if (!validarContrasena(formulario.contrasena, formulario.contrasena_c)) {
      alert('Las contraseñas no coinciden');
      return;
    }
    formulario.submit();
  }
}

export { crearCuenta };
