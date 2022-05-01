import React, { useState } from 'react';
import { MentorProfile, MenteeProfile } from '../../components/UserProfile/index.js';
import { Spin } from 'antd';

function EditProfile() {
  const isMentor = window.sessionStorage.getItem('mentor');
  const token = window.sessionStorage.getItem('token');
  const [loading, setLoading] = useState(false);
  const [profile, setProfile] = useState({
    organization: '',
    status: '',
    level: '',
    offers: [],
    intro: '',
    role: '',
    concentrations: [],
    years: 0
  });

  const getProfile = (isMentor) => {
    const url = '';
    if (isMentor) {
      url = `${process.env.REACT_APP_BACKEND_HOST}/profile?mentor=true`;
    }
    else {
      url = `${process.env.REACT_APP_BACKEND_HOST}/profile?mentor=false`;
    }
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(form),
    })
    .then(res => res.json())
    .then(data => {
      setProfile(data);
      console.log(data);
      console.log(profile);
    })
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
      setProfile(data);
      console.log(profile);
    })
  };

  getProfile(isMentor);

  const onMenteeFinish = (form) => {
    setLoading(true);
    console.log('Received values of form: ', form);
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
      setProfile(data);
    })
  };

  return (
      <Spin spinning={loading}>
        {isMentor
        ? <MentorProfile onFinish={onMentorFinish} profile={profile}/>
        : <MenteeProfile onFinish={onMenteeFinish} profile={profile} />
        }
      </Spin>
  );
}
 
export default EditProfile;