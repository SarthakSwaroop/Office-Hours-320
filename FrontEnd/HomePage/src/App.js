import React from 'react';
import Header from './components/Header/Header';
import Sidebar from './components/Sidebar/Sidebar';
import OfficeHoursList from './components/OfficeHoursList/OfficeHoursList';
import SuggestedTimings from './components/SuggestedTimings/SuggestedTimings';
import TopBar from './components/TopBar/TopBar';
import './App.css';

function App() {
  return (
    <div className="app">
      <Header />
      <div className="main-content">
        <Sidebar />
        <div className="content-wrapper">
          <TopBar />
          <OfficeHoursList />
          <SuggestedTimings />
        </div>
      </div>
    </div>
  );
}

export default App;
