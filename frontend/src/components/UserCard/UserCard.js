import React from 'react';
import "./UserCard.css";
import {Card, Button} from 'react-bootstrap';
import image from '../../assets/pexels-harsh-kushwaha-1689731.jpg';

export default function UserCard({ candidate }) {
  return (
    <Card style={{ width: '25rem' }}>
      {
        candidate == null 
        ? <h2>Loading</h2>
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