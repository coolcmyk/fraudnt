import React, { useState } from 'react';
import styled from 'styled-components';

const InteractionsContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  padding: 20px;
  background: #2d2d2d;
  color: white;
  border: 2px solid #6a11cb;
  border-radius: 10px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
`;

const InteractionsTitle = styled.h2`
  font-size: 1.5rem;
  margin-bottom: 15px;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
`;

const ChatWindow = styled.div`
  flex-grow: 1;
  overflow-y: auto;
  background: #1c1c1c;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
`;

const ChatMessage = styled.div`
  margin-bottom: 10px;
  padding: 10px;
  background: #333;
  border-radius: 5px;
`;

const InteractionsArea = styled.textarea`
  width: 100%;
  background: #1c1c1c;
  color: white;
  border: 1px solid #6a11cb;
  border-radius: 5px;
  padding: 10px;
  resize: none;
  height: 60px;
  margin-bottom: 10px;
`;

const SendButton = styled.button`
  padding: 10px;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background: linear-gradient(45deg, #5a0db7, #1d5de8);
  }
`;

const Interactions = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSendMessage = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, sender: 'User' }]);
      setInput("");
      // Here you can add the logic to send the message to the AI and get the response
    }
  };

  return (
    <InteractionsContainer>
      <InteractionsTitle>Interactions</InteractionsTitle>
      <ChatWindow>
        {messages.map((message, index) => (
          <ChatMessage key={index}>
            <strong>{message.sender}:</strong> {message.text}
          </ChatMessage>
        ))}
      </ChatWindow>
      <InteractionsArea
        placeholder="Type your message here..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <SendButton onClick={handleSendMessage}>Send</SendButton>
    </InteractionsContainer>
  );
};

export default Interactions;
