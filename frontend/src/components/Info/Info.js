import React from 'react';
import image from '../../assets/pexels-harsh-kushwaha-1689731.jpg';
import Image from 'react-bootstrap/Image';
import ActionBar from '../ActionBar/ActionBar';
import './Info.css'

export default function Info() {
    const mentee = [
        {name : "Escanord", url:image, job: "Software Engineer", company:"Padthai", offer:["resume", "leetcode"], concentration:["AI", "database"], description:"Stupid"}
    ]
    return (
        <div className="info" style={{width: '350px', height: 'auto'}}>
            <div className="image"> 
                <Image fluid src={image}/>
            </div>
            <ActionBar/>

            <div class="userin4">
                <p className="bold">{mentee[0].name}</p>
                <p>{mentee[0].job}</p>
                <p className="bold">About</p>
                <p>{mentee[0].description}</p>
            </div>
        </div>
    )
}