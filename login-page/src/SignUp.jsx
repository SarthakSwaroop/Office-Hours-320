import React, { useState } from 'react';
import './SignUp.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; 

const SignUpComponent = () => {
  const navigate = useNavigate(); 
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleSignUp = async (e) => {
    e.preventDefault();
    setErrorMessage(''); 

    if (password !== confirmPassword) {
      setErrorMessage('Passwords do not match.');
      return;
    }

    try {
      const response = await axios.post('https://your-api.com/signup', {
        firstName,
        lastName,
        email,
        password
      });
      // If the sign-up is successful, you might want to do something with the response
      // e.g., store the user token, if the API returns one

      navigate('/'); // Redirect to login page after successful sign-up
    } catch (error) {
      // If the API call fails, display an error message from the server
      setErrorMessage(error.response.data.message || 'An error occurred during sign up.');
    }
  };

  return (
    <div className="signup-wrapper">
      <div className="signup-header">
        <div className="header-content">OFFICE HOURS SCHEDULER</div>
      </div>
      <div className="signup-container">
        <form onSubmit={handleSignUp}>
          <label className="input-label">Enter your Name</label>
          <div className="input-field">
            <input 
              type="text"
              className="name-input" 
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              placeholder="First Name"
              required
            />
            <input 
              type="text"
              className="name-input" 
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
              placeholder="Last Name"
              required
            />
          </div>
          
          <label className="input-label">Enter your UMass Email to Sign up with for the office hour scheduler</label>
          <div className="input-field">
            <input 
              type="email"
              className="email-input"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your UMass Email"
              required
            />
          </div>

          <label className="input-label">Create a strong password with a mix of letters, numbers and symbols</label>
          <div className="input-field">
            <input 
              type="password"
              className="password-input"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter New Password"
              required
            />
            <input 
              type="password"
              className="password-input"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="Confirm your Password"
              required
            />
          </div>
          {errorMessage && <div className="error-message">{errorMessage}</div>}

          <button type="submit" className="signup-button">Sign Up</button>
        </form>
      </div>
      <footer className="signup-footer"></footer>
    </div>
  );
};

export default SignUpComponent;