import { crearCuenta } from './CrearCuenta/funciones.js';
import { iniciarSesion } from './IniciarSesion/funciones.js';

window.onload = () => {
  let formRegistrar = document.getElementById('form-registrar');
  let formIngresar = document.getElementById('form-ingresar');
  if (formRegistrar) {
    crearCuenta(formRegistrar);
  }
  if (formIngresar) {
    iniciarSesion(formIngresar);
  }
}
