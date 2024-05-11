/**
 * Verifica que el nombre sea entre 4 y 15 caracteres.
 * @param nombre : <input>
 */
const validarNombre = (nombre) => {
  if (nombre.value.length < 4) return 101;
  if (nombre.value.length > 15) return 102;
  return 100;
}

/**
 * Verifica que el valor de ambas entradas sean iguales.
 * @param contrasena : <input>
 * @param confirmaContrasena : <input>
 */
const validarContrasena = (contrasena, confirmaContrasena) => {
  if (contrasena.value === "" || confirmaContrasena.value === "") {
    return false;
  } else if (contrasena.value !== confirmaContrasena.value) {
    return false;
  }
  return true;
}

/**
 * Verifica que el valor de ambas entradas sean iguales.
 * @param correo : <input>
 * @param confirmaCorreo : <input>
 */
const validarCorreo = (correo, confirmaCorreo) => {
  if (correo.value === "" || confirmaCorreo.value === "") {
    return false;
  } else if (correo.value !== confirmaCorreo.value) {
    return false;
  }
  return true;
}

export { validarNombre, validarContrasena, validarCorreo };
