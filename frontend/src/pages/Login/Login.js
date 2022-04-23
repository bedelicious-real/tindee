import React, { Component, useContext, useState } from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './Login.css'
import logo from "../../assets/hands-helping-solid.svg";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

function Login () {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

		

    const onSubmit = event => {
        console.log(email);
        console.log(password);
        event.preventDefault();
        const object = {
            email: email,
            pwd: password,
        }
        console.log(JSON.stringify(object))
        fetch(`${process.env.REACT_APP_BACKEND_HOST}/user/session`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(object),
        })
        .then(res => res.json())
        .then(data => {
            window.sessionStorage.setItem('token', data);
						window.sessionStorage.setItem('email', email);
        })
    };
     

    

    return (
        <div className='login_page'>
            <div className="login_logo">
                <img src={logo} />
                <span className="title"> tindee </span>
                <p> where <span className="extra_bold">MENTORS</span> and <span className="extra_bold">MENTEES</span> are meant to <span className="extra_bold">MEET</span> </p>
            </div>
            <div className="login_auth_buttons">
                <Form onSubmit={onSubmit}>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                        <div className='left'><Form.Label>Email address</Form.Label></div>
                        <Form.Control type="email" placeholder="Enter email" onChange={e => setEmail(e.target.value)} />
                    </Form.Group>

                    <Form.Group className="mb-3" controlId="formBasicPassword">
                        <div className='left'><Form.Label>Password</Form.Label></div>
                        <Form.Control type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
                    </Form.Group>
                    <div className="d-grid gap-2" >
                        <Button type="submit" className="submit_button" variant='outline-dark' style={{backgroundColor: 'rgb(244, 73, 101)', border: 'none', fontWeight: 700, color: 'white'}}>
                            LOG IN
                        </Button>
                    </div>

                </Form>
            <p> By clicking Log In, you agree with our Terms. </p>
            <p> Learn how we process your data in our Privacy Policy and Cookies Policy </p>
            </div>

            
    </div>

    );
};
  

export default Login;

// const rootElement = document.getElementById("root");
// ReactDOM.render(<Login/>, rootElement);