import React from 'react';
import './Sidebar.css'; 
import HomeIcon from '../../assets/icons/home.svg';
import ProfileIcon from '../../assets/icons/profile.svg';
import NotificationIcon from '../../assets/icons/notification.svg';
import CalenderIcon from '../../assets/icons/calender.svg';

function Sidebar() {
  console.log('Sidebar is rendering');

  return (
    
    <div className="sidebar">
      <img src={HomeIcon} alt="Home" className="sidebar-icon" />
      <img src={ProfileIcon} alt="Profile" className="sidebar-icon" />
      <img src={NotificationIcon} alt="Notification" className="sidebar-icon" />
      <img src={CalenderIcon} alt="Calender" className="sidebar-icon" />
    </div>
  );
}
export default Sidebar;