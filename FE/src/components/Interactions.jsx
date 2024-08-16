// import React from 'react';

// const Interactions = () => {
//   return (
//     <div className="box-border h-full p-4 border-4 border-white flex justify-center items-center text-white">
//       Interactions
//     </div>
//   );
// };

// export default Interactions;

import React, { useState } from 'react';
import axios from 'axios';

// Remove the process import, as it's not needed in browser environments
// import process from 'process';

const API_URL = process.env.NODE_ENV === 'production'
  ? `${process.env.PROD_URL}/home`
  : 'https://rich-agency-372104-us-central1.cloudfunctions.net/chat';

const Interactions = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setMessages(prev => [...prev, { type: 'user', content: input }]);
    
    try {
      const response = await axios.post('https://rich-agency-372104.web.app/chat', { message: input });
      setMessages(prev => [...prev, { type: 'bot', content: response.data.response }]);
    } catch (error) {
      console.error('Error:', error);
    }

    setInput('');
  };

  return (
    <div className="box-border h-full p-4 border-4 border-white flex flex-col justify-between text-white">
      <div className="overflow-auto mb-4">
        {messages.map((msg, index) => (
          <div key={index} className={`mb-2 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block p-2 rounded ${msg.type === 'user' ? 'bg-blue-500' : 'bg-green-500'}`}>
              {msg.content}
            </span>
          </div>
        ))}
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