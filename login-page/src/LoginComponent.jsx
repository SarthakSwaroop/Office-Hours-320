import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; 
import './LoginComponent.css'; 

const LoginComponent = () => {
  const navigate = useNavigate(); 
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleEmailChange = (e) => setEmail(e.target.value);
  const handlePasswordChange = (e) => setPassword(e.target.value);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('https://your-api.com/login', {
        email,
        password
      });
      // Handle response here. For example, saving the token and redirecting
      console.log(response.data);
      navigate('/HomePage'); // Redirect to dashboard upon successful login
    } catch (err) {
      // Handle error here. For example, displaying an error message
      setError(err.response.data.message || 'An error occurred');
    }
  };

  const navigateToSignUp = () => {
    navigate('/signup'); 
  };

  return (
    <div className="login-wrapper">
      <header className="login-header">
        <div className="header-content">OFFICE HOURS SCHEDULER</div>
      </header>
      <div className="login-container">
        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <input 
              type="email"
              className="login-input" 
              value={email}
              onChange={handleEmailChange}
              placeholder="Enter your UMass Email"
              required
            />
          </div>
          <div className="input-container">
            <input 
              type="password" 
              className="login-input"
              value={password}
              onChange={handlePasswordChange}
              placeholder="Enter your Password"
              required
            />
          </div>
          {error && <div className="error-message">{error}</div>}
          <button type="submit" className="login-button">LOGIN</button>
          <div className="divider">OR</div>
          <button type="button" className="signup-button" onClick={navigateToSignUp}>SIGN UP</button>
        </form>
      </div>
      <footer className="login-footer"></footer>
    </div>
  );
};

export default LoginComponent;
