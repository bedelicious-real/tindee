import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import { Image } from 'antd';
import React, { Component, useState } from 'react';
import { Form, Select, InputNumber, Button, Upload } from 'antd';
//import ImgCrop from 'antd-img-crop';

const { Option } = Select;
const formItemLayout = {
    labelCol: {
      span: 6,
    },
    wrapperCol: {
      span: 14,
    },
};


const onFinish = (values) => {
    console.log('Received values of form: ', values);
    console.log(JSON.stringify(values));
};

const dummyRequest = ({ file, onSuccess }) => {
  setTimeout(() => {
    onSuccess("ok");
  }, 0);
};

const beforeUpload = (file) => {
  const isJpgOrPng = file.type === "image/jpeg" || file.type === "image/png" || file.type === "image/jpg";
  if (!isJpgOrPng) {
    alert("You can only upload JPG/PNG/JPEG file!");
  }
  const isLt2M = file.size / 1024 / 1024 < 2;
  if (!isLt2M) {
    alert("Image must smaller than 2MB!");
  }
  return isJpgOrPng && isLt2M;
}

class MentorProfile extends Component {
  state = {
    selectedFile: null,
    selectedFileList: []
  };

  onChange = info => {
    const nextState = {};
    switch (info.file.status) {
      case "uploading":
        nextState.selectedFileList = [info.file];
        break;
      case "done":
        nextState.selectedFile = info.file;
        nextState.selectedFileList = [info.file];
        break;

      default:
        // error or removed
        nextState.selectedFile = null;
        nextState.selectedFileList = [];
    }
    this.setState(() => nextState);
  };
  


    render() { 
        return (
        <div>
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
                label="Organization:Company"
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




      <Form.Item
        wrapperCol={{
          span: 12,
          offset: 6,
        }}
      >
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>

    <Upload
          fileList={this.state.selectedFileList}
          customRequest={dummyRequest}
          onChange={this.onChange}
          beforeUpload={beforeUpload}
        >
          <Button>Choose File</Button>
    </Upload>



        <pre>{JSON.stringify(this.state, null, 2)}</pre>

        </div>
        );
    }
}
 
export default MentorProfile;

const rootElement = document.getElementById("root");
ReactDOM.render(<MentorProfile/>, rootElement);