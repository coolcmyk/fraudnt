import React from 'react';
import styled from 'styled-components';

const HistoryContainer = styled.div`
  box-sizing: border-box;
  height: 500px;
  width: 100%;  /* Adjusted to take full width of the container */
  max-width: 400px;  /* Set a max width so it doesn't get too large */
  padding: 20px;
  border: 2px solid #6a11cb;
  background: linear-gradient(45deg, #1c1c1c, #2d2d2d);
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: auto;
  color: white;
`;

const HistoryTitle = styled.h2`
  font-size: 1.5rem;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 20px;
`;

const HistoryItem = styled.div`
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  background: #333;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
  font-size: 0.9rem;
  text-align: center;
`;

const History = () => {
  const historyItems = [
    "AI analyzed your code.",
    "User interacted with the AI.",
    "Code compilation was successful.",
    // Add more history items as needed
  ];

  return (
    <HistoryContainer>
      <HistoryTitle>History</HistoryTitle>
      {historyItems.map((item, index) => (
        <HistoryItem key={index}>
          {item}
        </HistoryItem>
      ))}
    </HistoryContainer>
  );
};

export default History;



