import React from 'react';
import styled from 'styled-components';

const StickersContainer = styled.div`
  padding: 20px;
  background: #2d2d2d;
  color: white;
  border: 2px solid #6a11cb;
  border-radius: 10px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
`;

const Sticker = styled.div`
  width: 50px;
  height: 50px;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  transition: transform 0.3s ease;

  &:hover {
    transform: scale(1.1);
  }
`;

const Stickers = () => {
  return (
    <StickersContainer>
      <Sticker>😊</Sticker>
      <Sticker>👍</Sticker>
      <Sticker>💬</Sticker>
      <Sticker>🔥</Sticker>
      {/* Add more stickers as needed */}
    </StickersContainer>
  );
};

export default Stickers;
