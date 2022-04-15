import logo from './logo.svg';
import './App.css';
import Login from './pages/Login/Login';
import LoginForm from './pages/Login/LoginForm';
import EditProfile from './pages/EditProfile/EditProfile';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      
      <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login/>} />
            <Route path="/loginform" element={<LoginForm/>} />
            <Route path="/editprofile" element={<EditProfile/>} />
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
