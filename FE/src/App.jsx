import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import './App.css'
import HomePage from './components/HomePage'

const App = () => (
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to={"/home"} />} />

        <Route path="/home" element={<HomePage />} />
      </Routes>
    </BrowserRouter>
);



export default App;
