// src/scripts/users.ts

import { User } from './types';

const apiUrl = 'http://localhost:5000';

// Función para crear un nuevo usuario
export const createUser = async (user: User): Promise<User> => {
  const response = await fetch(`${apiUrl}/usuarios`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(user),
  });
  const data = await response.json();
  return data.usuario;
};

// Función para actualizar un usuario existente
export const updateUser = async (userId: string, user: User): Promise<User> => {
  const response = await fetch(`${apiUrl}/usuarios/${userId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(user),
  });
  const data = await response.json();
  return data.usuario;
};

// Función para eliminar un usuario
export const deleteUser = async (userId: string): Promise<void> => {
  await fetch(`${apiUrl}/usuarios/${userId}`, {
    method: 'DELETE',
  });
};
