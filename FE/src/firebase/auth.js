import {auth} from './firebase';
// import {createUserWithEmailAndPassword, signInWithEmailAndPassword, GoogleAuthProvider} from "./firebase";


// Create user with email and password
export const createUserWithEmailAndPassword = async (email, password) => {
  try {
    const userCredential = await firebaseCreateUser(auth, email, password);
    return userCredential.user;
  } catch (error) {
    console.error("Error creating user:", error.message);
    throw error;
  }
};

// Sign in with email and password
export const signInWithEmailAndPassword = async (email, password) => {
  try {
    const userCredential = await firebaseSignIn(auth, email, password);
    return userCredential.user;
  } catch (error) {
    console.error("Error signing in:", error.message);
    throw error;
  }
};

// Sign in with Google
export const signInWithGoogle = async () => {
  try {
    const provider = new GoogleAuthProvider();
    const result = await signInWithPopup(auth, provider);
    return result.user;
  } catch (error) {
    console.error("Error signing in with Google:", error.message);
    throw error;
  }
};


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
    url: '${window.location.origin}/home',
  });
};


