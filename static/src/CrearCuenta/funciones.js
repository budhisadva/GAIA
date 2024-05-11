import { validarNombre, validarContrasena, validarCorreo } from '../Validaciones/funciones.js';

/**
 * Verifica que se haya ingresado una fecha posterior a la actual.
 * @param fecha : <input>
 */
const validarFecha = (fecha) => {
  let fechaFinal = fecha.value.substring(0, 8);
  fechaFinal += parseInt(fecha.value.substring(8))+1;
  let ingresado = new Date(fechaFinal);
  let actual = new Date(Date.now());
  return actual > ingresado;
}

/**
 * Verifica que se haya ingresado un valor para el campo genero.
 * @param listaValores : [<input>]
 */
const validarGenero = (listaValores) => {
  let genero = [];
  listaValores.forEach(x => {
    if (x.checked) genero.push(x.value);
  });
  if (!genero.length) return false;
  return true;
}

/**
 * Ejecuta las validaciones cuando el formulario intenta ser
 * enviado.
 * @param formulario : <form>
 */
const crearCuenta = (formulario) => {
  formulario.onsubmit = (e) => {
    e.preventDefault();
    switch (validarNombre(formulario.nombre)) {
      case 101:
        alert('Nombre muy corto');
        return;
      case 102:
        alert('Nombre muy largo');
        return;
    }
    if (!validarFecha(formulario.fecha)) {
      alert('Ingrese una fecha correcta');
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
