import React, { Component, useState } from 'react';
import ReactDOM, { render } from 'react-dom';
import 'antd/dist/antd.css';
import './Login.css'
import logo from "../../assets/hands-helping-solid.svg";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

function Login () {
    const onFinish = (values) => {
      console.log('Success:', values);
    };
  
    const onFinishFailed = (errorInfo) => {
      console.log('Failed:', errorInfo);
    };
  
    
    return (
        <div className='login_page'>
            <div className="login_logo">
                <img src={logo} />
                <span className="title"> tindee </span>
                <p> where <span className="extra_bold">MENTORS</span> and <span className="extra_bold">MENTEES</span> are meant to <span className="extra_bold">MEET</span> </p>
            </div>
            <div className="login_auth_buttons">
            <Form>
                <Form.Group className="mb-3" controlId="formBasicEmail">
                    <div className='left'><Form.Label>Email address</Form.Label></div>
                    <Form.Control type="email" placeholder="Enter email" />
                </Form.Group>

                <Form.Group className="mb-3" controlId="formBasicPassword">
                <div className='left'><Form.Label>Password</Form.Label></div>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                <Button variant='outline-light' type="submit" className='big_button'>
                    LOG IN
                </Button>
            </Form>
            </div>
            <p> By clicking Log In, you agree with our Terms. </p>
            <p> Learn how we process your data in our Privacy Policy and Cookies Policy </p>
            
    </div>

    );
};
  

export default Login;

const rootElement = document.getElementById("root");
ReactDOM.render(<Login/>, rootElement);