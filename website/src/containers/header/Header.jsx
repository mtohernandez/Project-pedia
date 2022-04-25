import React from 'react';
import './header.css';
import { Photo } from '../../components';


const Header = ({project}) => {
    return (
        <div>
            <Photo state={project._state} background={project._background}/>
        </div>
    )
}

export default Header