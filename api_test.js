// This function sends a POST request to create a new student availability entry
function createStudentAvailability() {
    const data = {
      email: 'bobross@example.com',
      monday: '9:00-10:00',
      tuesday: '9:00-10:00',
      wednesday: '9:00-10:00',
      thursday: '9:00-10:00',
      friday: '9:00-10:00',
      saturday: '9:00-10:00',
      sunday: '9:00-10:00',
    };
  
    fetch('https://django-deployment-office-hours.vercel.app/student_availability/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
  }
  
  // This function sends a GET request to retrieve all student availability entries
  function getStudentAvailability() {
    fetch('https://django-deployment-office-hours.vercel.app/student_availability/')
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
  }
  
  // Call the functions
  createStudentAvailability();
  getStudentAvailability();
  
// let array = [
//     {email: 'test1@email.com', name: 'Test1'},
//     {email: 'test2@email.com', name: 'Test2'},
//     // more objects...
// ];

// let email = 'test1@email.com';
// let result = array.find(obj => obj.email === email);

// console.log(result);  // Logs: {email: 'test1@email.com', name: 'Test1'}
