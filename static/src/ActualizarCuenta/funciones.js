import { validarNombres, validarContrasena, validarCorreo } from '../Validaciones/funciones.js';

/**
 * Comprueba que los campos del formulario nombre
 * hayan sido llenadas correctamente
 */
const verificaNombre = (formulario) => {
  let entradas = [...formulario.children];
  formulario.onsubmit = (e) => {
    e.preventDefault();
    if (!validarNombres(entradas[2], entradas[3])) {
      alert('Por favor ingrese los datos correctamente');
      return;
    }
    formulario.submit();
  }
}

/**
 * Comprueba que los campos del formulario contrasena
 * hayan sido llenadas correctamente
 */
const verificaContrasena = (formulario) => {
  let entradas = [...formulario.children];
  formulario.onsubmit = (e) => {
    e.preventDefault();
    if (!validarContrasena(entradas[2], entradas[3])) {
      alert('Por favor ingrese los datos correctamente');
      return;
    }
    formulario.submit();
  }
}

/**
 * Comprueba que los campos del formulario correo
 * hayan sido llenadas correctamente
 */
const verificaCorreo = (formulario) => {
  let entradas = [...formulario.children];
  formulario.onsubmit = (e) => {
    e.preventDefault();
    if (!validarCorreo(entradas[2], entradas[3])) {
      alert('Por favor ingrese los datos correctamente');
      return;
    }
    formulario.submit();
  }
}

/**
 * Asocia los botones "Cancelar" de la vista, con la
 * funcion para borrar la informacion de los campos de sus
 * respectivo formularios.
 */
const btnCancelar = () => {
  document.querySelectorAll('.btn-c').forEach(btn => {
    let form = btn.closest('.formulario');
    btn.onclick = () => {
      form.reset();
    }
  });
}
/**
 * Ejecuta las validaciones cuando el formulario intenta ser
 * enviado.
 */
const actualizarCuenta = () => {
  let formulario = [...document.querySelectorAll('.formulario')];
  verificaNombre(formulario[0]);
  verificaContrasena(formulario[1]);
  verificaCorreo(formulario[2]);
  btnCancelar();
}

export { actualizarCuenta };
