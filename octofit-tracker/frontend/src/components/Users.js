import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://solid-fishstick-q7r57x45vw436xw-8000.app.github.dev/api/users/?format=json')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center text-warning">Users</h1>
      <table className="table table-striped table-hover">
        <thead className="thead-dark">
          <tr>
            <th>Username</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user._id}>
              <td>{user.username}</td>
              <td>{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Users;
