import './App.css';
import Login from './pages/Login/Login';
import Messages from './pages/Messages/Messages';
import EditProfile from './pages/EditProfile/EditProfile';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

function App() {
  return (
    <div className="App">
      
      <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login/>} />
            <Route path="/editprofile" element={<EditProfile/>} />
            <Route path="/messages" element={<Messages/>} />
          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
