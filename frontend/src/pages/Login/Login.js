import 'antd/dist/antd.css'
import { Button } from 'antd';
import React from 'react';
import "./Login.css";
import logo from "../../assets/hands-helping-solid.svg";
import { DownloadOutlined } from '@ant-design/icons';

export default function Login() {
    return (
        <div className="login_page">
            <div className="login_logo">
                <img src={logo} /> 
                <span className="title"> tindee </span>
            </div>
            <div className="login_auth_buttons">
                <p> where <span className="extra_bold">MENTORS</span> and <span className="extra_bold">MENTEES</span> are meant to <span className="extra_bold">MEET</span> </p>
                <Button type="default" shape="round" className="big_button" ghost icon={<DownloadOutlined />} size="large">
                    CONTINUE WITH LINKEDIN
                </Button>
                <p> By clicking Log In, you agree with our Terms</p>
                <p> Learn how we process your data in our Privacy Policy and Cookies Policy </p>
            </div>
        </div>
    );
}