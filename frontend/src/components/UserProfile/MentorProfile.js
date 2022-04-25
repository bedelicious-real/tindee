import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import React, { Component, useState } from 'react';
import { Form, Select, InputNumber, Button, Upload, Input } from 'antd';
import UploadImage from './UploadImage';
import './UserProfile.css';

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


function MentorProfile({ onFinish }) {
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
            name="role"
            label="Role"
            hasFeedback
            rules={[
              {
                required: true,
                message: 'Please select your job role!',
              },
            ]}
          >
            <Select placeholder="Please select your job role">
              <Option value="Software Engineer">Software Engineer</Option>
              <Option value="Data Scientist">Data Scientist</Option>
              <Option value="AI/ML Engineer">AI/ML Engineer</Option>
              <Option value="Product Manager">Product Manager</Option>
              <Option value="Electrical Engineer">Electrical Engineer</Option>
            </Select>
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
            name="years"
            label="Years of Experience"
            rules={[
              {
                required: true,
                message: 'Please input your years of experience!',
              },
            ]}
          >
            <InputNumber
              min={0}
              style={{
                width: '100%',
              }}
            />
          </Form.Item>

          <Form.Item
            name="concentrations"
            label="Concentrations"
            rules={[
              {
                required: true,
                message: 'Please select max 3 concentrations!',
                type: 'array',
              },
            ]}
          >
            <Select mode="multiple" placeholder="Please select your concentrations (max 3)">
              <Option value="Front End">Front End</Option>
              <Option value="Back End">Back End</Option>
              <Option value="Database"> Database</Option>
              <Option value="Researching">Researching</Option>
              <Option value="AI/ML">AI/ML</Option>
              <Option value="Infrastructure"> Infrastructure</Option>
              <Option value="Business Analytics">Business Analytics </Option>
              <Option value="Cloud Solutions">Cloud Solutions </Option>
              <Option value="Automation"> Automation</Option>
              <Option value="Product Management"> Product Management </Option>
              <Option value="Testing">Testing </Option>
            </Select>
          </Form.Item>

          <Form.Item
            name="offers"
            label="Offers"
            rules={[
              {
                required: true,
                message: 'Please select what you can help with!',
                type: 'array',
              },
            ]}
          >
            <Select mode="multiple" placeholder="Please select your offers (max 3)">
              <Option value="Resume Review">Resume Review</Option>
              <Option value="Mock Interview">Mock Interview</Option>
              <Option value="Career Advice">Career Advice</Option>
              <Option value="Referral">Referral</Option>
            </Select>
          </Form.Item>
          <Form.Item wrapperCol={{
              offset: 1,
            }}
          >
            <Button className="big_button" htmlType="submit">
              UPDATE PROFILE
            </Button>
          </Form.Item>
        </Form>
        </div>
        );
    }
 
export default MentorProfile;

const rootElement = document.getElementById("root");
ReactDOM.render(<MentorProfile/>, rootElement);