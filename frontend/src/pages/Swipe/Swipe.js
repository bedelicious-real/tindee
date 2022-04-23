import ActionBar from '../../components/ActionBar/ActionBar';
import NavBar from '../../components/NavBar/NavBar';
import UserCard from '../../components/UserCard/UserCard';

import './Swipe.css';

export default function Swipe() {
    return (
        <div class="user-card">
            <UserCard/>
            <ActionBar/>
            <NavBar/>
        </div>
    )
}