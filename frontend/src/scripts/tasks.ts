// src/scripts/tasks.ts
import type { Task } from './types'; // Importa la interfaz solo como tipo

const apiUrl = 'http://service-a:5000'; // URL base del backend Flask

// Función para obtener todas las tareas
export const fetchTasks = async (): Promise<Task[]> => {
  const response = await fetch(`${apiUrl}/tareas`);
  const data = await response.json();
  return data.tareas;
};

// Función para crear una nueva tarea
export const createTask = async (task: Task): Promise<Task> => {
  const response = await fetch(`${apiUrl}/tareas`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  return data.tarea;
};

// Función para actualizar una tarea existente
export const updateTask = async (taskId: string, task: Task): Promise<Task> => {
  const response = await fetch(`${apiUrl}/tareas/${taskId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(task)
  });
  const data = await response.json();
  return data.tarea;
};

// Función para eliminar una tarea
export const deleteTask = async (taskId: string): Promise<boolean> => {
  const response = await fetch(`${apiUrl}/tareas/${taskId}`, {
    method: 'DELETE'
  });
  return response.ok;
};
