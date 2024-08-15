import {auth} from './firebase';
import {createUserWithEmailAndPassword, signInWithEmailAndPassword, GoogleAuthProvider} from "firebase/auth";
export const doCreateUserWithEmailAndPassword  = async (email, password) => {
    return createUserWithEmailAndPassword(email, password);
};

export const doSignInWithEmailAndPassword  = async (email, password) => {
    return signInWithEmailAndPassword(email, password);
};


export const doSignInWithGoogle  = async () => {
  const provider = new GoogleAuthProvider();
  const result = await signInWithPopup(auth, provider);
  return result;
};

export const doSignOut  = async () => {
  return signOut(auth);
};

export const doPasswordReset  = async (email) => {
  return sendPasswordResetEmail(auth, email);
  };

export const doPasswordChange  = async (password) => {
  return updatePassword(auth.currentUser, password);
  };


export const doSendEmailVerification  = async () => {
  return sendEmailVerification(auth.currentUser, {
    url: ${window.location.origin}/home,
  });
  };


