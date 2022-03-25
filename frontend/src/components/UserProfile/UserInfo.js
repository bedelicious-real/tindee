import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import { Image } from 'antd';
import React, { Component } from 'react';

class UserInfo extends Component {
    state = {  } 
    render() { 
        return (
        <div>
            <h1>Edit Your Profile</h1>
            <Image width={200} src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"/>

        </div>
        );
    }
}
 
export default UserInfo;