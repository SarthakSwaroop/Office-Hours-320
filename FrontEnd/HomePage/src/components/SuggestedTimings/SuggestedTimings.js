import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './SuggestedTimings.css';
import CalendarIcon from '../../assets/icons/calender2.svg';

function SuggestedTimings() {
  const [suggestedTimings, setSuggestedTimings] = useState([]);

  useEffect(() => {
    const fetchSuggestedTimings = async () => {
      try {
        const response = await axios.get('http://localhost:3001/suggested-timings');
        setSuggestedTimings(response.data);
      } catch (error) {
        console.error('Error fetching suggested timings:', error);
        // Handle error here (e.g., show user feedback)
      }
    };

    fetchSuggestedTimings();
  }, []);

  return (
    <div className="suggested-timings-container">
      <div className="header-container">
        <h2 className="header-title">Suggested Office Hours Timings</h2>
        <span className="header-subtitle">Based on student preferences</span>
      </div>
      {suggestedTimings.map(course => (
        <div key={course.courseId} className="course-timings">
          <div className="course-id">{course.courseId}</div>
          {course.times.map(time => (
            <div key={time.day} className="time-slot">
              <img src={CalendarIcon} alt="Calendar" className="calendar-icon" />
              <span className="day">{time.day}</span>
              <span className="hours">{time.hours.join(' | ')}</span>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default SuggestedTimings;
