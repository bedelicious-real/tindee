import React from 'react';
import "./UserCard.css";
import {Card, Button} from 'react-bootstrap';
import image from '../../assets/pexels-harsh-kushwaha-1689731.jpg';

export default function UserCard({ candidate }) {
  return (
    <Card style={{ width: '25rem' }}>
      {
        candidate == null 
        ? <>
            <Card.Img 
              className="card-img" 
              variant="top" 
              src = "https://media.istockphoto.com/vectors/loading-icon-vector-illustration-vector-id1335247217?k=20&m=1335247217&s=612x612&w=0&h=CQFY4NO0j2qc6kf4rTc0wTKYWL-9w5ldu-wF8D4oUBk=" 
              height='450px'
            />
            <Card.Body>
              <Card.Title>Loading</Card.Title>
            </Card.Body>
          </>
        : <>
          <Card.Img 
            className="card-img" 
            variant="top" 
            src={candidate['image-url']} 
            height='450px'
          />
          <Card.Body>
            <Card.Title>
              {candidate['first-name']}&nbsp;{candidate['last-name']}
            </Card.Title>
            <Card.Text>
              <b>{candidate['status']}</b> at <b>{candidate['organization']}</b>
              <br/>
              <b>Intro</b>: {candidate['description'].substring(0, 40)}...
            </Card.Text>
          </Card.Body>
          </>
      }
    </Card>
  );
}