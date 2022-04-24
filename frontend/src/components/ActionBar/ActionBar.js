import { Divider } from 'antd';
import React from 'react';
import {Button} from 'react-bootstrap';
import './ActionBar.css';
import {FaHeart} from 'react-icons/fa';
import {ImCross} from 'react-icons/im';
import {AiFillStar} from 'react-icons/ai';

export default function ActionBar({
  candidate,
  targetEmail,
  removeTopCandidate
}) {
  const handleLike = () => {
    const token = window.sessionStorage.getItem('token');
    fetch(`${process.env.REACT_APP_BACKEND_HOST}/matches`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(targetEmail)
    })
    .then(res => res.json())
    .then(data => {
      console.log(data);
      if (data === "OK"){
        toastr['success']("You are matched with " + candidate['first-name'] + " " + candidate['last-name'],"It's a match!!!")
      }
      removeTopCandidate();
    })
    .catch(err => console.error(err));
  };

  const handleIgnore = () => {
    removeTopCandidate();
  };

  return (
    <div className = "actionBar">
      <Button 
        className="dislike rounded-circle" 
        disabled={targetEmail == null}
        onClick={(e) => handleIgnore()}
      >
        <ImCross/>
      </Button>
      <Button 
        className="superlike rounded-circle" 
        disabled={targetEmail == null}
        onClick={(e) => handleLike()}
      >
        <FaHeart/>
      </Button>
    </div>
  )
}