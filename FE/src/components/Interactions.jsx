  // // import React from 'react';

  // // const Interactions = () => {
  // //   return (
  // //     <div className="box-border h-full p-4 border-4 border-white flex justify-center items-center text-white">
  // //       Interactions
  // //     </div>
  // //   );
  // // };

  // // export default Interactions;

  // import React, { useState } from 'react';
  // import axios from 'axios';

  // // Remove the process import, as it's not needed in browser environments
  // // import process from 'process';

  // // const API_URL = process.env.NODE_ENV === 'production'
  // //   ? `${process.env.PROD_URL}/home`
  // //   : 'https://test-aiko-h63gkfe66q-et.a.run.app/chat';
  //   // : 'https://asia-southeast2-rich-agency-372104.cloudfunctions.net/test-aiko/chat';
  //   // : ' http://192.168.180.38:8080/chat';

  // const Interactions = () => {
  //   const [input, setInput] = useState('');
  //   const [messages, setMessages] = useState([]);

  //   const handleSubmit = async (e) => {
  //     e.preventDefault();
  //     if (!input.trim()) return;

  //     setMessages(prev => [...prev, { type: 'user', content: input }]);
      
  //     try {
  //       // const response = await axios.post('http://192.168.180.38:8080/chat', { message: input });

  //       const response = await axios.post('https://test-aiko-h63gkfe66q-et.a.run.app/chat', { message: input }
  //         // headers: {
  //         //   'Content-Type': 'application/json',
  //         //   'Access-Control-Allow-Origin': '*',
  //         //   'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
  //         //   'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  //         //   'Access-Control-Allow-Credentials': 'true',
  //         // }
          
  //       );
  //       setMessages(prev => [...prev, { type: 'bot', content: response.data.response }]);
  //     } catch (error) {
  //       console.error('Error:', error);
  //     }

  //     setInput('');
  //   };
  //   // const handleSubmit = async (e) => {
  //   //   e.preventDefault();
  //   //   if (!input.trim()) return;
  //   //   setMessages(prev => [...prev, { type: 'user', content: input }]);
  //   //   try {
  //   //     const response = await axios.post('https://asia-southeast2-rich-agency-372104.cloudfunctions.net/test-aiko/chat', { message: input }, {
  //   //       headers: {
  //   //         'Content-Type': 'application/json'
  //   //       }
  //   //     });
  //   //     console.log('Response:', response.data); // Log the entire response
  //   //     if (response.data && response.data.response) {
  //   //       setMessages(prev => [...prev, { type: 'bot', content: response.data.response }]);
  //   //     } else {
  //   //       console.error('Unexpected response structure:', response.data);
  //   //       setMessages(prev => [...prev, { type: 'bot', content: 'Sorry, I encountered an error.' }]);
  //   //     }
  //   //   } catch (error) {
  //   //     console.error('Error:', error);
  //   //     if (error.response) {
  //   //       console.error('Error response:', error.response.data);
  //   //       console.error('Error status:', error.response.status);
  //   //     }
  //   //     setMessages(prev => [...prev, { type: 'bot', content: 'Sorry, I encountered an error.' }]);
  //   //   }
  //   //   setInput('');
  //   // };
  //   return (
  //     <div className="box-border h-full p-4 border-4 border-white flex flex-col justify-between text-white">
  //       <div className="overflow-auto mb-4">
  //         {messages.map((msg, index) => (
  //           <div key={index} className={`mb-2 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
  //             <span className={`inline-block p-2 rounded ${msg.type === 'user' ? 'bg-blue-500' : 'bg-green-500'}`}>
  //               {msg.content}
  //             </span>
  //           </div>
  //         ))}
  //       </div>
  //       <form onSubmit={handleSubmit} className="flex">
  //         <input
  //           type="text"
  //           value={input}
  //           onChange={(e) => setInput(e.target.value)}
  //           className="flex-grow mr-2 p-2 text-black"
  //           placeholder="Type your message..."
  //         />
  //         <button type="submit" className="bg-blue-500 p-2 rounded">Send</button>
  //       </form>
  //     </div>
  //   );
  // };
    
  // export default Interactions;


//   import React, { useState } from 'react';
// import axios from 'axios';

// const Interactions = () => {
//   const [input, setInput] = useState('');
//   const [messages, setMessages] = useState([]);

//   const handleSubmit = async (e) => {
//     const cors = require('cors');
//     const express = require('express');
//     const app = express();

//     app.use(cors({
//       origin: 'https://rich-agency-372104.web.app', // Allow requests from your web app
//       methods: 'GET, POST, OPTIONS', // Allow GET, POST, and OPTIONS requests
//       allowedHeaders: 'Content-Type', // Allow Content-Type header
//     }));

// // Your existing code for handling requests...

//     e.preventDefault();
//     if (!input.trim()) return;

//     setMessages(prev => [...prev, { type: 'user', content: input }]);

//     try {
//       const response = await axios.post('https://asia-southeast1-rich-agency-372104.cloudfunctions.net/aiko/chat', { message: input }, 
//         headers = {
//           'Content-Type': 'application/json',
//           'Access-Control-Allow-Origin': 'https://rich-agency-372104.web.app/home'

//         }
//       );
//       setMessages(prev => [...prev, { type: 'bot', content: response.data.response }]);
//     } catch (error) {
//       console.error('Error:', error);
//       setMessages(prev => [...prev, { type: 'bot', content: 'Sorry, I encountered an error.' }]);
//     }

//     setInput('');
//   };

// import React, { useState } from 'react';
// import axios from 'axios';

// const Interactions = () => {
//   const [input, setInput] = useState('');
//   const [messages, setMessages] = useState([]);
//   var cors = require('cors')
//   var express = require('express')
//   var app = express()
//   app.use(cors()) // Use this after the variable declaration


//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     if (!input.trim()) return;

//     setMessages(prev => [...prev, { type: 'user', content: input }]);

//     try {
//       const response = await axios.post('https://asia-southeast1-rich-agency-372104.cloudfunctions.net/aiko/chat', { message: input }, {
//         // headers: {
//         //   'Content-Type': 'application/json',
//         //   'Access-Control-Allow-Origin': 'https://rich-agency-372104.web.app/home'
//         // }
//       });
//       setMessages(prev => [...prev, { type: 'bot', content: response.data.response }]);
//     } catch (error) {
//       console.error('Error:', error);
//       setMessages(prev => [...prev, { type: 'bot', content: 'Sorry, I encountered an error.' }]);
//     }

//     setInput('');
//   };


//   return (
//     <div className="box-border h-full p-4 border-4 border-white flex flex-col justify-between text-white">
//       <div className="overflow-auto mb-4">
//         {messages.map((msg, index) => (
//           <div key={index} className={`mb-2 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
//             <span className={`inline-block p-2 rounded ${msg.type === 'user' ? 'bg-blue-500' : 'bg-green-500'}`}>
//               {msg.content}
//             </span>
//           </div>
//         ))}
//       </div>
//       <form onSubmit={handleSubmit} className="flex">
//         <input
//           type="text"
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           className="flex-grow mr-2 p-2 text-black"
//           placeholder="Type your message..."
//         />
//         <button type="submit" className="bg-blue-500 p-2 rounded">Send</button>
//       </form>
//     </div>
//   );
// };

// export default Interactions;


import React, { useState } from 'react';
import axios from 'axios';

const Interactions = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = async (e) => {
    // const cors = require('cors');
    // const express = require('express');
    // const app = express();
    // app.use(cors());


    // app.use(function(req, res, next) {
    //   res.header("Access-Control-Allow-Origin", "*");
    //   res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    //   next();
    // });

    e.preventDefault();
    if (!input.trim()) return;
    
    
    setMessages(prev => [...prev, { type: 'user', content: input }]);
      const response = await axios.post('https://australia-southeast1-rich-agency-372104.cloudfunctions.net/aiko-testing/chat', 
        { message: input }
      );
      console.log('Response:', response.data); // Log the entire response

    setInput('');
  };

  return (
    <div className="box-border h-full p-4 border-4 border-white flex flex-col justify-between text-white">
      <div className="overflow-auto mb-4">
        {messages.length === 0 ? (
          <p>No messages yet. Start a conversation!</p>
        ) : (
          messages.map((msg, index) => (
            <div key={index} className={`mb-2 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
              <span className={`inline-block p-2 rounded ${msg.type === 'user' ? 'bg-blue-500' : 'bg-green-500'}`}>
                {msg.content}
              </span>
            </div>
          ))
        )}
      </div>
      <form onSubmit={handleSubmit} className="flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-grow mr-2 p-2 text-black"
          placeholder="Type your message..."
        />
        <button type="submit" className="bg-blue-500 p-2 rounded">Send</button>
      </form>
    </div>
  );
};

export default Interactions;