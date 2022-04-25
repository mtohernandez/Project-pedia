import React from 'react';
import './content.css';
import { Author, Description, Title } from '../../components';


const Content = ({project}) => {
    return (
        <div>
            <Author autor={project._author} fecha={project._submissionDate}/>
            <Title title={project._name}/>
            <Description description={project._description}/>
        </div>
    )
}

export default Content