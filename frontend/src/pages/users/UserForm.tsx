import React, { useState } from 'react';
import { createUser } from '@scripts/users';

const UserForm = () => {
  const [userData, setUserData] = useState({
    nombre: '',
    email: ''
  });
  const [message, setMessage] = useState('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setUserData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = createUser(userData);
      const result = await response;
      console.log('Usuario creado con éxito:', result);
      setMessage(`Usuario creado con id: ${result.id}`);
    } catch (error) {
      setMessage('Error al enviar el usuario');
      console.error('Error al enviar el usuario:', error);
    }
  };

  return (
    <form id="user-form" className="form" onSubmit={handleSubmit}>
      <h2>Crear o Editar Usuario React</h2>
      <div className="form-group">
        <label htmlFor="nombre">Nombre:</label>
        <input
          type="text"
          id="nombre"
          name="nombre"
          value={userData.nombre}
          onChange={handleInputChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={userData.email}
          onChange={handleInputChange}
        />
      </div>
      <button type="submit">Enviar</button>
      {message && <p>{message}</p>}
    </form>
  );
};

export default UserForm;