import React, { useState } from 'react';

function UserForm() {
  const [userData, setUserData] = useState({
    name: '',
    email: ''
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setUserData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/usuarios', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        throw new Error(`Error al enviar el usuario: ${response.statusText}`);
      }

      const result = await response.json();
      console.log('Usuario enviado con éxito:', result);
    } catch (error) {
      console.error('Error al enviar el usuario:', error);
    }
  };

  return (
    <form id="user-form" className="form" onSubmit={handleSubmit}>
      <h2>Crear o Editar Usuario</h2>
      <div className="form-group">
        <label htmlFor="name">Nombre:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={userData.name}
          onChange={handleInputChange}
          required
        />
      </div>

      <div className="form-group">
        <label htmlFor="email">Correo Electrónico:</label>
        <input
          type="text"
          id="email"
          name="email"
          value={userData.email}
          onChange={handleInputChange}
          required
        />
      </div>

      <button type="submit" className="btn">Guardar</button>
    </form>
  );
}

export default UserForm;
