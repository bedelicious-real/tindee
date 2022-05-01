import React from 'react';
import UserCard from '../UserCard/UserCard';
import ActionBar from '../ActionBar/ActionBar';
import { Row } from 'antd';


export default function MentorsGrid({ mentors }) {
    return (
        <Row gutter={[16, 32]}>
            {mentors.map((mentor) => (
                <div className="mentorcard-container">
                    <UserCard candidate={mentor} />
                    <ActionBar 
                        candidate={mentor}
                        targetEmail={mentor['email']}
                    />
                </div>
            ))}
        </Row>
    )
}