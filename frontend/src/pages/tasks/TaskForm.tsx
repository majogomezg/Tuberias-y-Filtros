// TaskForm.tsx
import React, { useState } from 'react';

function TaskForm() {
  const [taskData, setTaskData] = useState({
    description: '',
    userId: ''
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setTaskData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/tareas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
      });

      if (!response.ok) {
        throw new Error(`Error al enviar la tarea: ${response.statusText}`);
      }

      const result = await response.json();
      console.log('Tarea enviada con éxito:', result);
    } catch (error) {
      console.error('Error al enviar la tarea:', error);
    }
  };

  return (
    <form id="task-form" className="form" onSubmit={handleSubmit}>
      <h2>Crear Tarea</h2>
      <div className="form-group">
        <label htmlFor="description">Descripción:</label>
        <input
          type="text"
          id="description"
          name="description"
          value={taskData.description}
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="usuario_id">ID de Usuario:</label>
        <input
          type="text"
          id="usuario_id"
          name="usuario_id"
          value={taskData.userId}
          onChange={handleInputChange}
          required
        />
      </div>

      <button type="submit" className="btn">Enviar Tarea</button>
    </form>
  );
}

export default TaskForm;
