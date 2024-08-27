import React, { useState } from 'react';
import styled from 'styled-components';

const CompilerContainer = styled.div`
  padding: 20px;
  background: #2d2d2d;
  color: white;
  border: 2px solid #6a11cb;
  border-radius: 10px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  height: 100%;
`;

const CodeArea = styled.textarea`
  width: 100%;
  height: calc(100% - 50px);
  background: #1c1c1c;
  color: white;
  border: 1px solid #6a11cb;
  border-radius: 5px;
  padding: 10px;
  font-family: 'Courier New', Courier, monospace;
  resize: none;
  font-size: 14px;
`;

const RunButton = styled.button`
  padding: 10px;
  margin-top: 10px;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;

  &:hover {
    background: linear-gradient(45deg, #5a0db7, #1d5de8);
  }
`;

const Compiler = () => {
  const [code, setCode] = useState("");

  const handleRunCode = () => {
    // Here you can add logic to actually compile or run the code
    console.log("Code to run:", code);
  };

  return (
    <CompilerContainer>
      <CodeArea 
        value={code} 
        onChange={(e) => setCode(e.target.value)} 
        placeholder="Type your code here..." 
      />
      <RunButton onClick={handleRunCode}>Run Code</RunButton>
    </CompilerContainer>
  );
};

export default Compiler;

