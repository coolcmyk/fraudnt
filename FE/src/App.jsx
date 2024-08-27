import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import './App.css'
import HomePage from './components/HomePage'
import Login from './components/auth/login/index.jsx'
const App = () => (
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to={"/home"} />} />

        {/* <Route path="/login" element={<Login />} /> */}
        <Route path="/home" element={<HomePage />} />
      </Routes>
    </BrowserRouter>
);



export default App;

// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';  

// import Homepage from '../../FE/src/components/HomePage.jsx';

// function App() {
// return (
//  <BrowserRouter>
//    <Routes>
//      <Route path="/" element={<Homepage />} />
//      {/* Other routes */}
//    </Routes>
//  </BrowserRouter>
// );
// }

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);
