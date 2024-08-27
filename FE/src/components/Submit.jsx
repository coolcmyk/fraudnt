import React from 'react';
import styled from 'styled-components';

const Button = styled.button`
  padding: 15px 30px;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;

  &:hover {
    background: linear-gradient(45deg, #5a0db7, #1d5de8);
    transform: scale(1.05);
  }
`;

const Submit = () => {
  return (
    <Button>
      Submit
    </Button>
  );
};

export default Submit;