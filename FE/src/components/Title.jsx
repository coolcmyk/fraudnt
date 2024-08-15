import React from 'react';

const Title = ({ toggleVisibility, isVisible }) => {
  return (
    <header className="w-full flex justify-between items-center navbar fill px-4">
      <h1 className="text-white text-6xl font-bold">
        www.preman.com
      </h1>
    </header>
  );
};

export default Title;
