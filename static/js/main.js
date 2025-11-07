// Función para abrir el modal con los ejercicios
function openModal(muscleGroupId) {
    const modal = document.getElementById('exerciseModal');
    const modalTitle = document.getElementById('modalTitle');
    const exercisesList = document.getElementById('exercisesList');
    
    // Establecer el título del modal
    modalTitle.textContent = `Ejercicios de ${muscleNames[muscleGroupId]}`;
    
    // Limpiar la lista de ejercicios
    exercisesList.innerHTML = '';
    
    // Obtener los ejercicios para el grupo muscular seleccionado
    const exercises = exercisesData[muscleGroupId];
    
    // Crear elementos para cada ejercicio
    exercises.forEach(exercise => {
        const exerciseItem = document.createElement('div');
        exerciseItem.className = 'exercise-item';
        exerciseItem.innerHTML = `
            <div class="exercise-image" style="background-image: url('${exercise.image}')"></div>
            <div class="exercise-name">${exercise.name}</div>
            <div class="exercise-muscle">${exercise.muscle}</div>
        `;
        exercisesList.appendChild(exerciseItem);
    });
    
    // Mostrar el modal
    modal.style.display = 'block';
}

// Función para cerrar el modal
function closeModal() {
    const modal = document.getElementById('exerciseModal');
    modal.style.display = 'none';
}

// Cerrar el modal al hacer clic fuera de él
window.onclick = function(event) {
    const modal = document.getElementById('exerciseModal');
    if (event.target === modal) {
        closeModal();
    }
}