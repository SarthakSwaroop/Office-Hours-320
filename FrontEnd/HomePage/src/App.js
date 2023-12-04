import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Header from './components/Header/Header';
import Sidebar from './components/Sidebar/Sidebar';
import OfficeHoursList from './components/OfficeHoursList/OfficeHoursList';
import SuggestedTimings from './components/SuggestedTimings/SuggestedTimings';
import StudentOfficeHoursList from './components/StudentOfficeHoursList/StudentOfficeHoursList';
import TopBar from './components/TopBar/TopBar';
import './App.css';
import CalendarPage from './components/CalendarPage/CalendarPage';
const ProfilePage = () => <div>Profile Page Content</div>;

function App() {
  const [isStudent, setIsStudent] = useState(false); 

  return (
    <Router>
      <div className="app">
        <Header />
        <div className="main-content">
          <Sidebar />
          <div className="content-wrapper">
            <Routes>
              <Route path="/" element={isStudent ? <><TopBar /><StudentOfficeHoursList /></> : <><TopBar /><OfficeHoursList /><SuggestedTimings /></>} />
              <Route path="/profile" element={<ProfilePage />} />
              <Route path="/calendar" element={<CalendarPage />} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
