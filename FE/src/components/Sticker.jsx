import React, { useState } from 'react';

const Sticker = ({ toggleVisibility }) => {
  const [isToggled, setIsToggled] = useState(false);

  const handleClick = () => {
    toggleVisibility();
    setIsToggled(!isToggled);
  };

  return (
    <div 
      className="box-border h-[300px] w-[300px] p-4 border-4 border-white flex justify-center items-center text-white cursor-pointer"
      onClick={handleClick}
    >
      <img 
        src={isToggled ? "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif" : "https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif"} 
        alt="GIF" 
        className="h-full w-full object-cover"
      />
    </div>
  );
};

export default Sticker;
