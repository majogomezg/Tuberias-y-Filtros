// src/scripts/users.ts

import { User } from './types';

const apiUrl = 'http://service-a:5000';

//Get all users
export const fetchUsers = async (): Promise<User[]> => {
  const response = await fetch(`${apiUrl}/usuarios`);
  const data = await response.json();
  return data.usuarios;
};

// Función para crear un nuevo usuario
export const createUser = async (user: User): Promise<User> => {
  console.log('user', user);
  const response = await fetch(`${apiUrl}/usuarios`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(user),
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error);
  }
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
