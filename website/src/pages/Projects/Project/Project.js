import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom';
import { Comments, Header, Content } from '../../../containers';
import './project.css'

const Project = () => {

    const {id} = useParams();

    const [project, setProject] = useState('');

    const getProject = async () => {
        const response = await fetch(`/findProject${id}`)
        const data = await response.json();
        setProject(data)
    }
    
    useEffect(()=>{
        getProject();
    }, [])

    return (
        <div className='App'>
        <div>
            <Header project={project}/> 
        </div>         
            <Content project={project}/>
        <div className='divider'></div>
            <Comments/>
        </div>
  )
}

export default Project