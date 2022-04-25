import React from 'react'

const ProjectCard = ({project}) => {
  return (
      <div className='project'>
        <a href={`/project/${project._id_project}`}>
        {project._state === 'CLOSED' ? (
            <div style={{background: '#FF0000'}}>
            <p>{project._state}</p>
            </div>
        ): project._state === 'RESOURCING' ? (
            <div style={{background: '#EC7F00'}}>
            <p>{project._state}</p>
            </div>

        ): project._state === 'PROGRESS' ? (
            <div style={{background: '#04B500'}}>
            <p>{project._state}</p>
            </div>
        ):(
            <div>
            <p>UNKNOWN</p>
            </div>
        )}
        <div>
            <img src={project._background !== '' ? project._background : 'https://via.placeholder.com/400'}/>
        </div>
        <div>
            <span>{project._submissionDate}</span>
            <h3>{project._name}</h3>
            <h2>{project._author}</h2>
        </div>
        </a>
    </div>
  )
}

export default ProjectCard