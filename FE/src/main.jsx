import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    
  </StrictMode>,
)



// import { StrictMode } from 'react';
// import { createRoot } from 'react-dom/client';
// import App from './App.jsx';
// import './index.css';
// import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import Login from './components/auth/login/index.jsx'; // Import the Login component

// const root = createRoot(document.getElementById('root'));
// root.render(
//   <StrictMode>
//     <BrowserRouter>
//       <Routes>
//         <Route path="/login" element={<Login />} />
//         {/* Other routes */}
//       </Routes>
//     </BrowserRouter>
//   </StrictMode>
// );