import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import React, { Component, useContext, useState } from 'react';
import { Form, Select, InputNumber, Button, Upload, Input } from 'antd';
import './UserProfile.css';
import UploadImage from './UploadImage';
import {useNavigate} from 'react-router';


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

function MenteeProfile({ onFinish }) {
    return (
        <div className='editprofile_page' >
            <h1>Edit Your Profile</h1>
            <div className='upload_container'>
                <UploadImage/>
            </div>
            <Form
              name="validate_other"
              {...formItemLayout}
              onFinish={onFinish}
            >
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
                <Button className="big_button" htmlType="submit" >
                    UPDATE PROFILE
                </Button>
            </Form.Item>
            </Form>


    </div>
    );
}
 
export default MenteeProfile;