import React, { useState, useRef } from "react";
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import './UserProfile.css';

export default function UploadImage() {
  const validateImage = (file) => {
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
  const [file, setFile] = useState(null)
  const onSubmit = event => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('file', file);
    // console.log(file);
    fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile/avatar`, {
      method: 'POST',
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      body: formData,
    })
    .then(res => res.json())
    .then(data => {
        window.sessionStorage.setItem('token', data);
        window.sessionStorage.setItem('email', email);
    })
  }

  return (
    <div style={{marginTop: 20, marginBottom: 10}}>
      <form onSubmit={onSubmit}>
        <label className="upload_input_container">
          Choose Image
          <input
            type="file" 
            required
            size="sm" 
            onChange={(e) => {
              validateImage(e.target.files[0])
              setFile(e.target.files[0])
            }}
          />
        </label>
        <button className="upload_input_container" type="submit">Upload Image</button>
      </form>
 
    </div>
  );
}
