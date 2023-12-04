import React from 'react';
import './Sidebar.css'; 
import HomeIcon from '../../assets/icons/home.svg';
import ProfileIcon from '../../assets/icons/profile.svg';
import NotificationIcon from '../../assets/icons/notification.svg';
import CalenderIcon from '../../assets/icons/calender.svg';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <div className="sidebar">
      <Link to="/">
        <img src={HomeIcon} alt="Home" className="sidebar-icon" />
      </Link>
      <Link to="/profile">
        <img src={ProfileIcon} alt="Profile" className="sidebar-icon" />
      </Link>
      <Link to="/calendar">
        <img src={CalenderIcon} alt="Calendar" className="sidebar-icon" />
      </Link>
    </div>
  );
}

export default Sidebar;
