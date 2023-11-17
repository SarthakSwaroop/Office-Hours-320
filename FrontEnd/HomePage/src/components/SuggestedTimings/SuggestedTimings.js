import React from 'react';
import './SuggestedTimings.css';
import CalendarIcon from '../../assets/icons/calender2.svg'; 

function SuggestedTimings() {
  const suggestedTimings = [
    {
      courseId: 'CS 320',
      times: [
        { day: 'Monday', hours: ['09:00 - 11:00', '13:00 - 15:00', '17:30 - 18:30'] },
        { day: 'Wednesday', hours: ['09:00 - 11:00', '14:00 - 16:00'] },
      ],
    },
  ];

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
