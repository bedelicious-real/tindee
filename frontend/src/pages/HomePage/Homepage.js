import { useState, useEffect } from "react";
import Filter from "../../components/Filter/Filter";
import MentorsGrid from "../../components/Mentors/MentorsGrid";

export default function Homepage() {

    const [mentors, setMentors] = useState([]);
    const [filteredMentors, setFilteredMentors] = useState([]);
    const token = window.sessionStorage.getItem('token');

    const getMentors = () => {
        return fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile/mentors`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            }
        })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            return data;
        })
    };

    useEffect(() => {
      getMentors().then((result) => setMentors(result));
    }, []);




    return (
        <div>
            Hello World
            <Filter setFilteredMentors={setFilteredMentors}/>
            <div className="mentor-grid">
                {filteredMentors.length > 0
                ? <MentorsGrid mentors={filteredMentors} />
                : <MentorsGrid mentors={mentors} />
                }
            </div>
        </div>
    )

    
}