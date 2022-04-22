import React from 'react';
import './NavBar.css';
import {MdSwipe} from 'react-icons/md';
import {AiFillHome} from'react-icons/ai';
import {GiTeacher} from 'react-icons/gi';
import {RiLoginBoxLine} from 'react-icons/ri';

export default function NavBar() {
    return (
        <div class="navbar">
            <a href="/"><AiFillHome/></a>
            <a href="/swipe"><MdSwipe/></a>
            <a href="/login"><GiTeacher/></a>
            <a href="/messages"><RiLoginBoxLine/></a>
        </div>
    )
}
