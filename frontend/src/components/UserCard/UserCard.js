import React from 'react';
import "./UserCard.css";
import {Card, Button} from 'react-bootstrap';
import image from '../../assets/pexels-harsh-kushwaha-1689731.jpg';

export default function UserCard() {
    const mentee = [
        {name : "Escanord", url:image, job: "Software Engineer", company:"Padthai", offer:["resume", "leetcode"], concentration:["AI", "database"]}
    ]
    return (     
        <Card style={{ width: '25rem' }}>
            <Card.Img className="card-img" variant="top" src={mentee[0].url} height='450px'/>
            <Card.Body>
                <Card.Title >{mentee[0].name}</Card.Title>
                <Card.Text>
                {mentee[0].job} at {mentee[0].company}
                <br/>
                {mentee[0].offer.join(", ")}  
                <br/>
                {mentee[0].concentration.join(", ")}  
                </Card.Text>
            </Card.Body>
        </Card>
    );
}