import React, { useState, useRef } from "react";
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

export default function UploadImage() {
  const [file, setFile] = useState(null)
  const onSubmit = event => {
    //setFile(event.target.files[0]);
    console.log(file);
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
    <div>
      <form onSubmit={onSubmit}>
            <input
              type="file" 
              required
              size="sm" 
              onChange={(e) => setFile(e.target.files[0])}
              />
        <button type="submit">Upload</button>
      </form>
 
    </div>
  );
}
