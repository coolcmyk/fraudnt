import React from 'react';
import styled from 'styled-components';

const TitleContainer = styled.div`
  margin-bottom: 40px;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const BubbleContainer = styled.div`
  background: rgba(0, 0, 0, 0.8);
  padding: 20px 40px;
  border-radius: 30px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
  display: inline-block;
`;

const TitleText = styled.h1`
  font-size: 3rem;
  font-family: 'Poppins', sans-serif;
  background: white;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0;
`;

const Title = () => {
  return (
    <TitleContainer>
      <BubbleContainer>
        <TitleText>FRAUDN'T</TitleText>
      </BubbleContainer>
    </TitleContainer>
  );
};

export default Title;
