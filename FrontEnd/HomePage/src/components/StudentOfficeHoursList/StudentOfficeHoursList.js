import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './StudentOfficeHoursList.css';
import CalendarIcon from '../../assets/icons/calender1.svg';

function StudentOfficeHoursList() {
  const [officeHours, setOfficeHours] = useState([]);
  const [isLoading, setIsLoading] = useState(true); // State to track loading status

  useEffect(() => {
    const fetchOfficeHours = async () => {
      try {
        const response = await axios.get('http://localhost:3001/office-hours');
        setOfficeHours(response.data);
      } catch (error) {
        console.error('Error fetching office hours:', error);
        // Handle error here (e.g., show user feedback)
      } finally {
        setIsLoading(false); // Set loading to false after fetching data
      }
    };

    fetchOfficeHours();
  }, []);

  return (
    <div className="office-hours-list">
      <h2>Upcoming Office Hours</h2>
      {isLoading ? (
        <div>Loading...</div>
      ) : officeHours.length > 0 ? (
        officeHours.map((session) => (
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
        ))
      ) : (
        <div>No upcoming office hours</div>
      )}
    </div>
  );
}

export default StudentOfficeHoursList;
