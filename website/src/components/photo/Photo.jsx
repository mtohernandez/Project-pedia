import React from 'react';
import './photo.css';
import goBackArrow from '../../assets/goBackArrow.svg';


const Photo = ({state, background}) => {
    return (
        <div className='image' style={{backgroundImage: `url(${background})`}}> 
            <div className='image_container-arrow' >    
                <a href='/projects'><img className='image-container-arrow' src={goBackArrow}/></a>
                </div>
                <div className='state_container'>
                {state === 'CLOSED' ? (
                    <div style={{background: '#FF0000', borderRadius: '40px', height: '40px'}}>
                    <p>{state}</p>
                    </div>
                ): state === 'RESOURCING' ? (
                    <div style={{background: '#EC7F00', borderRadius: '40px', height: '40px'}}>
                    <p>{state}</p>
                    </div>

                ): state === 'PROGRESS' ? (
                    <div style={{background: '#04B500', borderRadius: '40px', height: '40px'}}>
                    <p>{state}</p>
                    </div>
                ):(
                    <div>
                    <p>UNKNOWN</p>
                    </div>
                )}
                </div>
            
        </div>
    )
}

export default Photo