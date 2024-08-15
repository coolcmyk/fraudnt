// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBPT5fCozXz7cGJPYuzVSuno5aX-lTZyr0",
  authDomain: "fraudnt-47398.firebaseapp.com",
  projectId: "fraudnt-47398",
  storageBucket: "fraudnt-47398.appspot.com",
  messagingSenderId: "864625540295",
  appId: "1:864625540295:web:b2c1cd66d3222539a712e2",
  measurementId: "G-49BXCTZVW9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);

export  {app, auth};

