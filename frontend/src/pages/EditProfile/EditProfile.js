import React, { Component } from 'react';
import { MentorProfile, MenteeProfile } from '../../components/UserProfile/index.js';
import './EditProfile.css';

function EditProfile() {
        return (
            <div>
                <MentorProfile />
                <MenteeProfile />
            </div>
        );
}
 
export default EditProfile;