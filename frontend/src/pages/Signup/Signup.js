import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './Signup.css'
import logo from "../../assets/hands-helping-solid.svg";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';

function Signup () {
    const [first, setFirst] = useState('');
    const [last, setLast] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isMentor, setIsMentor] = useState(false);

    const onSubmit = event => {
        event.preventDefault();
        const object = {
            first: first,
            last: last,
            email: email,
            pwd: password,
        }
        console.log(JSON.stringify(object))
        fetch(`${process.env.REACT_APP_BACKEND_HOST}/user`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(object),
        })
        .then(res => res.json())
        .then(data => {
          console.log(data);   // key for authorization: store it somewhere for later use
        })
    };
     

    

    return (
        <div className='signup_page'>
            <div className="signup_logo">
                <img src={logo} />
                <span className="title"> tindee </span>
                <p> where <span className="extra_bold">MENTORS</span> and <span className="extra_bold">MENTEES</span> are meant to <span className="extra_bold">MEET</span> </p>
            </div>
            <div className="signup_auth_buttons">
                <Form onSubmit={onSubmit}>
                    <Form.Group className="mb-3" controlId="formBasicFirstName">
                        <div className='left'><Form.Label>First Name</Form.Label></div>
                        <Form.Control type="text" placeholder="Enter first name" onChange={e => setFirst(e.target.value)} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicLastName">
                        <div className='left'><Form.Label>Last Name</Form.Label></div>
                        <Form.Control type="text" placeholder="Enter last name" onChange={e => setLast(e.target.value)} />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <div className='left'><Form.Label>Email address</Form.Label></div>
                        <Form.Control type="email" placeholder="Enter email" onChange={e => setEmail(e.target.value)} />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <div className='left'><Form.Label>Password</Form.Label></div>
                        <Form.Control type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
                    </Form.Group>
                    <ButtonGroup className="d-grid gap-2">
                        <ToggleButton
                            id="mentee"
                            type="radio"
                            variant="outline-light"
                            value="1"
                            onChange={(e)=>setIsMentor(true)}
                            >
                            MENTEE
                        </ToggleButton>
                        <ToggleButton
                            id="mentOR"
                            type="radio"
                            variant="outline-light"
                            value="2"
                            onChange={(e)=>setIsMentor(true)}
                            >
                            MENTOR
                        </ToggleButton>
                    </ButtonGroup>
                    <Button variant='dark' type="submit" className='big_button' >
                        SIGN UP
                    </Button>
                </Form>
            </div>
            <p> By clicking Signup, you agree with our Terms. </p>
            <p> Learn how we process your data in our Privacy Policy and Cookies Policy </p>
            
    </div>

    );
};
  

export default Signup;

const rootElement = document.getElementById("root");
ReactDOM.render(<Signup/>, rootElement);