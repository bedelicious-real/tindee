import 'antd/dist/antd.css'
import { Button } from 'antd';
import React from 'react';
import "./Message.css";
import { Card, Avatar } from 'antd';

const { Meta } = Card;

export default function Message() {
    return (
        <div className="">
            <Card style={{ width: 300, marginTop: 10 }}>
                <Meta
                    avatar={<Avatar src="https://joeschmoe.io/api/v1/random" />}
                    title="First Name - Last Name"
                />
                <Button style={{ marginLeft: 40 }} shape="round" size="medium">
                    SCHEDULE MEETING
                </Button>
         

            </Card>
        </div>
    );
}