import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './Signup.css'
import logo from "../../assets/hands-helping-solid.svg";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';
import { Spin } from 'antd';
import { MenteeProfile, MentorProfile } from '../../components/UserProfile/index.js';


function Signup () {
    const [first, setFirst] = useState('');
    const [last, setLast] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isMentor, setIsMentor] = useState(false);
    const [loading, setLoading] = useState(false);
    const [next, setNext] = useState(false);


    const onMentorFinish = (form) => {
        console.log('Received values of form: ', form);
        const object = {
            first: first,
            last: last,
            email: email,
            pwd: password,
        }
        //console.log(loading);
        fetch(`${process.env.REACT_APP_BACKEND_HOST}/user`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(object),
        })
        .then(res => res.json())
        .then(data => {
            console.log(data); // key for authorization: store it somewhere for later use
            window.sessionStorage.setItem('token', data);
            window.sessionStorage.setItem('mentor', isMentor);
        })
        .then(() => {
            const token = window.sessionStorage.getItem('token');
            fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile?mentor=true`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(form),
            })
        })
        .then(res => res.json())
        .then(data => {
          console.log(data);
        })
        .then(setLoading(false));
    };

    const onMenteeFinish = (form) => {
        console.log(loading);
        console.log('Received values of form: ', form);
        const object = {
            first: first,
            last: last,
            email: email,
            pwd: password,
        }
        fetch(`${process.env.REACT_APP_BACKEND_HOST}/user`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(object),
        })
        .then(res => res.json())
        .then(data => {
            console.log(data); // key for authorization: store it somewhere for later use
            window.sessionStorage.setItem('token', data);
            window.sessionStorage.setItem('mentor', isMentor);
        })
        .then(() => {
            const token = window.sessionStorage.getItem('token');
            fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile?mentor=true`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(form),
            })
        })
        .then(res => res.json())
        .then(data => {
          console.log(data);
        })
        .then(setLoading(false));
    };

    return (
        <Spin spinning={loading} >
            <div className='signup_page'>
                <div className="signup_logo">
                    <img src={logo} />
                    <span className="title"> tindee </span>
                    <p> where <span className="extra_bold">MENTORS</span> and <span className="extra_bold">MENTEES</span> are meant to <span className="extra_bold">MEET</span> </p>
                </div>
                {!next 
                ?
                <div className="signup_auth_buttons">
                    <Form>
                        <Form.Group className="mb-3" controlId="formBasicFirstName">
                            <div className='left'><Form.Label>First Name</Form.Label></div>
                            <Form.Control type="text" placeholder="Enter first name" required onChange={e => setFirst(e.target.value)} />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicLastName">
                            <div className='left'><Form.Label>Last Name</Form.Label></div>
                            <Form.Control type="text" placeholder="Enter last name" required onChange={e => setLast(e.target.value)} />
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicEmail">
                            <div className='left'><Form.Label>Email address</Form.Label></div>
                            <Form.Control type="email" placeholder="Enter email" required onChange={e => setEmail(e.target.value)} />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="formBasicPassword">
                            <div className='left'><Form.Label>Password</Form.Label></div>
                            <Form.Control type="password" placeholder="Password" required onChange={e => setPassword(e.target.value)} />
                        </Form.Group>
                        <ButtonGroup className="d-grid gap-2">
                            <ToggleButton
                                id="mentee"
                                type="radio"
                                variant="outline-dark"
                                value="1"
                                onChange={(e)=>setIsMentor(false)}
                                >
                                MENTEE
                            </ToggleButton>
                            <ToggleButton
                                id="mentor"
                                type="radio"
                                variant="outline-dark"
                                value="2"
                                onChange={(e)=>setIsMentor(true)}
                                >
                                MENTOR
                            </ToggleButton>
                        </ButtonGroup>
                        <div className="d-grid gap-2" >
                            <Button className="submit_button" variant='outline-dark' 
                                style={{backgroundColor: 'rgb(244, 73, 101)', border: 'none', fontWeight: 700, color: 'white'}}
                                onClick={() => setNext(true)}
                            >
                                NEXT
                            </Button>
                        </div>
                    </Form>
                </div>
                :  
                <div style={{margin: 'auto'}}>
                    {isMentor
                    ? <MentorProfile onFinish={onMentorFinish} />
                    : <MenteeProfile onFinish={onMenteeFinish} />
                    }   
                </div>
                }
            </div>
    </Spin>    
    );
};
  

export default Signup;
