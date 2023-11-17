import React from 'react';
import './OfficeHoursList.css';
import CalendarIcon from '../../assets/icons/calender1.svg';

function OfficeHoursList() {
  const officeHours = [
    { id: 1, date: 'Monday, October 23, 2023', time: '15:00', professor: 'Professor Mathew Rattigan', course: 'CS 320' },
    { id: 2, date: 'Monday, October 23, 2023', time: '15:00', professor: 'Professor Mathew Rattigan', course: 'CS 320' },
    { id: 3, date: 'Monday, October 23, 2023', time: '15:00', professor: 'Professor Mathew Rattigan', course: 'CS 320' },
  ];

  return (
    <div className="office-hours-list">
      <h2>Upcoming Office Hours</h2>
      {officeHours.map((session) => (
        <div key={session.id} className="office-hour-entry">
          <div className="office-hour-date">{session.date}</div>
          <div className="office-hour-details">
            <div className="office-hour-time">
              <span>{session.time}</span>
              <img src={CalendarIcon} alt="Calendar" className="calendar-icon" />
            </div>
            <span className="office-hour-professor">{session.professor}</span>
            <span className="office-hour-course">{session.course}</span>
            <button className="modify-button">Modify</button>
          </div>
        </div>     
      ))}
    </div>
  );
}

export default OfficeHoursList;