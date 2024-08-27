import React from 'react';
import styled from 'styled-components';
import Title from './Title';
import Navbar from './Navbar';
import History from './History';
import Interactions from './Interactions';
import Stickers from './Sticker';
import Compiler from './Compiler';
import Submit from './Submit';

const GradientBackground = styled.div`
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0;
  margin: 0;
`;

const ContentWrapper = styled.div`
  width: 100%;
  max-width: 1200px;
  flex-grow: 1;
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
  padding: 20px;
  box-sizing: border-box;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
`;

const FullWidthWrapper = styled.div`
  grid-column: 1 / -1;
  margin-bottom: 20px;
`;

const Section = styled.div`
  background: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.4);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
`;

const FullHeightSection = styled(Section)`
  height: 100%;
`;

const SubmitWrapper = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 20px;
`;

const Footer = styled.footer`
  margin-top: 20px;
  text-align: center;
  color: white;
  font-size: 0.9rem;
  padding: 10px;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
`;

const HomePage = () => {
  return (
    <>
      <Navbar />
      <GradientBackground>
        <FullWidthWrapper>
          <Title />
        </FullWidthWrapper>
        <ContentWrapper>
          <FullHeightSection id="interactions">
            <Interactions />
          </FullHeightSection>
          <FullHeightSection id="stickers">
            <Stickers />
          </FullHeightSection>
          <FullWidthWrapper>
            <FullHeightSection id="compiler">
              <Compiler />
            </FullHeightSection>
          </FullWidthWrapper>
          <FullHeightSection id="history">
            <History items={['Item 1', 'Item 2', 'Item 3']} />
          </FullHeightSection>
        </ContentWrapper>
        <SubmitWrapper id="submit">
          <Submit />
        </SubmitWrapper>
        <Footer>© 2024 www.preman.com - All Rights Reserved</Footer>
      </GradientBackground>
    </>
  );
};

export default HomePage;

