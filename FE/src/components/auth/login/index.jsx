// import React, {useState} from "react";
// import { Navigate, Link } from "react-router-dom";
// import {doSignInWithEmailAndPassword, doSignInWithGoogle} from "../../../firebase/auth";
// import { useAuth } from "../../../contexts/authContext";


// const Login = () => {
//     const {userLoggedIn} = useAuth();
//     const [email, setEmail] = useState("");
//     const [password, setPassword] = useState("");
//     const [isSigningIn, setSigningIn] = useState(false);
//     const [errorMessages, setErrorMessage] = useState('');

//     const onSubmit = async (e) => {
//         e.preventDefault();
//         setSigningIn(true);
//         try {
//             await doSignInWithEmailAndPassword(email, password);
//         } catch (error) {
//             setErrorMessage(error.message);
//         }
//         setSigningIn(false);
//     }

//     const onGoogleSignIn = async () => {
//         setSigningIn(true);
//         try {
//             await doSignInWithGoogle();
//         } catch (error) {
//             setErrorMessage(error.message);
//         }
//         setSigningIn(false);
//     }

// }



import React, { useState } from "react";
import { Navigate, Link } from "react-router-dom";
import { doSignInWithEmailAndPassword, doSignInWithGoogle } from "../../../firebase/auth";
import { useAuth } from "../../../contexts/authContext";
import styled from 'styled-components'; // Import styled-components for styling

const LoginContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
`;

const LoginForm = styled.form`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
`;

const InputField = styled.input`
  padding: 10px;
  margin: 5px 0;
  border: 1px solid #ccc;
  border-radius: 3px;
`;

const Button = styled.button`
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 10px;
`;

const ErrorMessage = styled.p`
  color: red;
  margin-top: 5px;
`;

const Login = () => {
  const { userLoggedIn } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSigningIn, setSigningIn] = useState(false);
  const [errorMessages, setErrorMessage] = useState('');

  const onSubmit = async (e) => {
    e.preventDefault();
    setSigningIn(true);
    try {
      await doSignInWithEmailAndPassword(email, password);
    } catch (error) {
      setErrorMessage(error.message);
    }
    setSigningIn(false);
  };

  const onGoogleSignIn = async () => {
    setSigningIn(true);
    try {
      await doSignInWithGoogle();
    } catch (error) {
      setErrorMessage(error.message);
    }
    setSigningIn(false);
  };

  if (userLoggedIn) {
    return <Navigate to="/" />;
  }

  return (
    <LoginContainer>
      <LoginForm onSubmit={onSubmit}>
        <h2>Login</h2>
        <InputField type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <InputField type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        {errorMessages && <ErrorMessage>{errorMessages}</ErrorMessage>}
        <Button type="submit" disabled={isSigningIn}>
          {isSigningIn ? 'Signing in...' : 'Login'}
        </Button>
        <Button onClick={onGoogleSignIn} disabled={isSigningIn}>
          {isSigningIn ? 'Signing in with Google...' : 'Sign in with Google'}
        </Button>
        <p>Don't have an account? <Link to="/signup">Sign up</Link></p>
      </LoginForm>
    </LoginContainer>
  );
};

export default Login;