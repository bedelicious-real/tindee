import React, { Component, useState } from 'react';
import { MentorProfile, MenteeProfile } from '../../components/UserProfile/index.js';
import { Spin } from 'antd';

function EditProfile() {
  const isMentor = window.sessionStorage.getItem('mentor');
  const token = window.sessionStorage.getItem('token');
  const [loading, setLoading] = useState(false);
  
  const getProfile = (isMentor) => {

    console.log(isMentor);


    
  }


  const onMentorFinish = (form) => {
    setLoading(true);
    console.log('Received values of form: ', form);
    //const token = window.sessionStorage.getItem('token');
    fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile?mentor=true`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(form),

    })
    .then(res => res.json())
    .then(data => {
      console.log(data);
    })
  };

  const onMenteeFinish = (form) => {
    setLoading(true);
    console.log('Received values of form: ', form);
    //const token = window.sessionStorage.getItem('token');
    fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(form),

    })
    .then(res => res.json())
    .then(data => {
      console.log(data);
    })
  };

  return (
      <Spin spinning={loading}>
        {isMentor
        ? <MentorProfile onFinish={onMentorFinish}/>
        : <MenteeProfile onFinish={onMenteeFinish} />
        }
      </Spin>
  );
}
 
export default EditProfile;