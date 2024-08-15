import React, { useEffect, useState } from 'react';
import Title from './Title';
import History from './History';
import Interactions from './Interactions';
import Compiler from './Compiler';
import Sticker from './Sticker';
import Submit from './Submit';

const HomePage = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [isTransitioning, setIsTransitioning] = useState(false);

  useEffect(() => {
    document.body.style.display = 'block';
    document.body.style.margin = '0';
    document.body.style.padding = '0';
  }, []);

  const toggleVisibility = () => {
    if (isVisible) {
      setIsTransitioning(true);
      setTimeout(() => {
        setIsVisible(false);
        setIsTransitioning(false);
      }, 500);
    } else {
      setIsVisible(true);
    }
  };

  return (
    <div className="w-full h-full min-h-screen flex flex-col">
      <Title toggleVisibility={toggleVisibility} isVisible={isVisible} />
      <div className="flex flex-row justify-between flex-grow transition-all duration-500 ease-in-out">
        <div className={`flex flex-col w-[830px]`}>
          <div className={`transition-all duration-500 ease-in-out ${isVisible ? 'w-[830px]' : 'w-[1130px]'}`}>
            <div className="h-[500px]">
              <Interactions />
            </div>
          </div>
          <div className="h-[100px]">
            <Submit />
          </div>
          <div className="h-[200px]">
            <Compiler />
          </div>
        </div>
        <div className="flex flex-col w-1/3">
          <div className={`transform transition-transform duration-500 ease-in-out ${isVisible || isTransitioning ? 'translate-x-0 opacity-100' : 'translate-x-full opacity-0'}`}>
            <History />
          </div>
          <div className="h-[300px]">
            <Sticker toggleVisibility={toggleVisibility} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
