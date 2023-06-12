 // Almacena el valor seleccionado en localStorage
 function guardarValorSeleccionado(selectElement) {
    var selectedValue = selectElement.value;
    localStorage.setItem('colegioSeleccionado', selectedValue);
    selectElement.form.submit(); // Envía el formulario cuando se cambia la selección del colegio
}

// Recupera el valor almacenado en localStorage y establece la selección en el campo de selección del colegio
document.addEventListener('DOMContentLoaded', function() {
    var colegioSeleccionado = localStorage.getItem('colegioSeleccionado');
    if (colegioSeleccionado) {
        var selectElement = document.getElementById('colegio');
        selectElement.value = colegioSeleccionado;
    }
});