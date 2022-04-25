import './App.css';
import Login from './pages/Login/Login';
import Signup from './pages/Signup/Signup';
import EditProfile from './pages/EditProfile/EditProfile';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import Swipe from './pages/Swipe/Swipe';
import Info from './components/Info/Info';
import Filter from './components/Filter/Filter';

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
