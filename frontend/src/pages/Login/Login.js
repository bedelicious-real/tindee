import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import { Form, Input, Button, Checkbox } from 'antd';
import { UserOutlined, LockOutlined, DownloadOutlined } from '@ant-design/icons';
import './Login.css'
import logo from "../../assets/hands-helping-solid.svg";

export default function Login () {
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
            <Form
                name="basic"

                initialValues={{
                remember: true,
                }}
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
                autoComplete="off"
            >
                <Form.Item
                label="Username"
                name="username"

                rules={[
                    {
                    required: true,
                    message: 'Please input your username!',
                    },
                ]}
                >
                <Input className="big_button"/>
                </Form.Item>
        
                <Form.Item
                label="Password"
                name="password"
                rules={[
                    {
                    required: true,
                    message: 'Please input your password!',
                    },
                ]}
                >
                <Input.Password className="big_button"/>
                </Form.Item>
        
                <Form.Item
                name="remember"
                valuePropName="checked"
                wrapperCol={{
                    offset: 8,
                    span: 16,
                }}
                >
                <Checkbox>Remember me</Checkbox>
                </Form.Item>
        



                <Form.Item>
                
                            <Button htmlType="submit" type="default" shape="round" className="big_button" ghost size="large">
                                LOG IN
                            </Button>
                            </Form.Item>
                    <p> By clicking Log In, you agree with our Terms</p>
                    <p> Learn how we process your data in our Privacy Policy and Cookies Policy </p>
                
            </Form>
            </div>
      </div>
    );
  };
  


const rootElement = document.getElementById("root");
ReactDOM.render(<Login/>, rootElement);