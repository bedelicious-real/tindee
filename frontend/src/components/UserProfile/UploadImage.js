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
    console.log(formData);
    const token = window.sessionStorage.getItem('token');
    fetch(`${process.env.REACT_APP_BACKEND_HOST}/profile/avatar`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`
      },
      body: formData,
    })
    .then(res => res.json())
    .then(data => {
      console.log(data);
    })
  }

  return (
    <div style={{marginTop: 50, marginBottom: 10, marginLeft: 12}}>
      <form onSubmit={onSubmit}>
        <label className="upload_input_container">
          {file == null ? "Choose Image" : file.name}
          <input
            type="file" 
            required
            size="sm" 
            onChange={(e) => {
              if (validateImage(e.target.files[0]))
                setFile(e.target.files[0]);
            }}
          />
        </label>
        <button className="button_container" type="submit">Upload Image</button>
      </form>
 
    </div>
  );
}
