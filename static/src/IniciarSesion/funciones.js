/**
 * Ejecuta las validaciones cuando el formulario
 * intenta ser.
 * @param formulario : <form>
 */
const iniciarSesion = (formulario) => {
  formulario.onsubmit = (e) => {
    e.preventDefault();
    // validaciones
    formulario.submit();
  }
}

export { iniciarSesion };
