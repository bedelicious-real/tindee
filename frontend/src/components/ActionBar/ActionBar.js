import { Divider } from 'antd';
import React from 'react';
import {Button} from 'react-bootstrap';
import './ActionBar.css';
import {FaHeart} from 'react-icons/fa';
import {ImCross} from 'react-icons/im';
import {AiFillStar} from 'react-icons/ai';

export default function ActionBar() {
    return (
        <div className = "actionBar">
            <Button className="dislike rounded-circle"><ImCross/></Button>
            <Button className="superlike rounded-circle"><FaHeart size={40}/></Button>
            <Button className="like rounded-circle"><AiFillStar size={28}/></Button>
        </div>
    )
}