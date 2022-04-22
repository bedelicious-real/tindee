import logo from './logo.svg';
import './App.css';
import Login from './pages/Login/Login';
import UserCard from './components/UserCard/UserCard';
import ActionBar from './components/ActionBar/ActionBar';
import Swipe from './pages/Swipe/Swipe';
import NavBar from './components/NavBar/NavBar';
import Info from './components/Info/Info';
import Filter from './components/Filter/Filter';

function App() {
  return (
    <div className="App">
      <Filter />
    </div>
  );
}

export default App;
