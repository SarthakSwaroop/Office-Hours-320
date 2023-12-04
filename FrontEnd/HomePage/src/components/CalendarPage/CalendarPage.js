import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import { parse, set } from 'date-fns';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import './CalendarPage.css';

const localizer = momentLocalizer(moment);

const CalendarPage = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchOfficeHours = async () => {
      try {
        const response = await axios.get('http://localhost:3001/office-hours');
        const formattedEvents = response.data.map(hour => {
          const parsedDate = parse(hour.date, 'EEEE, MMMM d, yyyy', new Date());
          const [startHours, startMinutes] = hour.time.split(':').map(Number);
    
          const startDate = set(parsedDate, { hours: startHours, minutes: startMinutes });
          const endDate = new Date(startDate.getTime() + 60 * 60 * 1000); // Add 1 hour to start time
          return {
            title: `${hour.course} `,
            start: startDate,
            end: endDate,
            allDay: false
          };
        });
        setEvents(formattedEvents);
        //console.log(formattedEvents);
      } catch (error) {
        console.error('Error fetching office hours:', error);
      }
    };

    fetchOfficeHours();
  }, []);

  return (
    <div className="calendar-container">
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
        style={{ height: '500px' }}
        views={['month']}
      />
    </div>
  );
};

export default CalendarPage;
