import './App.css';
import Login from './pages/Login/Login';
import Messages from './pages/Messages/Messages';
import Signup from './pages/Signup/Signup';
import EditProfile from './pages/EditProfile/EditProfile';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Swipe from './pages/Swipe/Swipe';

function App() {

  return (
    <div className="App">
        <BrowserRouter>
            <Routes>
              <Route path="/" element={<Login/>} />
              <Route path="/login" element={<Login/>} />
              <Route path="/signup" element={<Signup/>} />
              <Route path="/editprofile" element={<EditProfile/>} />
              <Route path="/messages" element={<Messages/>} />
              <Route path="/swipe" element={<Swipe />} />
            </Routes>
          </BrowserRouter>
    </div>
  );
}

export default App;
