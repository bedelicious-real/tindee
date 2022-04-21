import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import React, { Component, useState } from 'react';
import { Form, Select, InputNumber, Button, Upload, Input } from 'antd';


const { Option } = Select;
const formItemLayout = {
    labelCol: {
      span: 24,
      offset: 1,
    },
    wrapperCol: {
      span: 24,
      offset: 1,
    },
};

function MenteeProfile() {
    
    const onFinish = (form) => {
        console.log('Received values of form: ', form);
        fetch(`http://172.20.16.58:5000/profile/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(form),
    
        })
        .then(res => {
          console.log(JSON.stringify(`${res.message}, status: ${res.status}`));
        })
    };
    
    return (
        <div className='editprofile_page' >
            <h1>Edit Your Profile</h1>
            <Form
              name="validate_other"
              {...formItemLayout}
              onFinish={onFinish}
            >
  
            <Form.Item
                name="first-name"
                label="First Name"
                rules={[
                    {
                        required: true,
                        message: 'Please input your first name!',
                    },
                ]}
            >
                <Input />
            </Form.Item>
            <Form.Item
                name="last-name"
                label="Last Name"
                rules={[
                    {
                        required: true,
                        message: 'Please input your last name!',
                    },
                ]}
            >
                <Input />
            </Form.Item>
            <Form.Item
                name="organization"
                label="Organization/Company"
                rules={[
                    {
                        required: true,
                        message: 'Please input your organization or company!',
                    },
                ]}
            >
                <Input />
            </Form.Item>

            <Form.Item
                name="level"
                label="Education Level"
                hasFeedback
                rules={[
                {
                    required: true,
                    message: 'Please select your education level!',
                },
                ]}
            >
                <Select placeholder="Please select your education level">
                    <Option value="highschool">High School </Option>
                    <Option value="bachelor">Bachelor Degree</Option>
                    <Option value="master">Master Degree</Option>
                    <Option value="higher">Higher Education</Option>
                </Select>
            </Form.Item>
            <Form.Item
                name="status"
                label="Full-time status"
                hasFeedback
                rules={[
                {
                    required: true,
                    message: 'Please select your full-time status!',
                },
                ]}
            >
                <Select placeholder="Please select your full-time status!">
                    <Option value="student"> Student </Option>
                    <Option value="worker"> Worker </Option>
                    <Option value="searcher"> Job Searcher </Option>
                </Select>
            </Form.Item>
            <Form.Item
                name="intro"
                label="Introduction"
                rules={[
                {
                    required: true,
                    message: 'Please input introduction',
                },
                ]}
            >
                <Input.TextArea showCount minLength={50} maxLength={1000} />
            </Form.Item>
    

            <Form.Item wrapperCol={{
                offset: 1,
                }}
            >
                <Button className="big_button" htmlType="submit">
                SUBMIT
                </Button>
            </Form.Item>
            </Form>


    </div>
    );
}
 
export default MenteeProfile;

const rootElement = document.getElementById("root");
ReactDOM.render(<MenteeProfile/>, rootElement);