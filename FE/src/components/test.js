fetch('https://australia-southeast2-rich-agency-372104.cloudfunctions.net/aiko-testing-1/chat', {
    method: 'POST', // Change to POST method
    mode: 'cors',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json' // Specify JSON content type
    },
    body: JSON.stringify({  // Add data to send in the body
      message: 'hi' // Replace with your actual message
    })
  })
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Handle the response data here (e.g., display on UI)
    console.log('Response:', data);
  })
  .catch(error => {
    console.error('Error:', error);
  });