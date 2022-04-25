import React, {useState, useEffect} from 'react';
import './project_table.css';

const ProjectTable = () => {

    const [search, setSearch] = useState([])

    const getProjects = async () => {
        const response = await fetch(`/getProjects`)
        const data = await response.json();
        setSearch(data)
    }

    const publishProject = async (id) => {
        const response = await fetch(`/publishProject${id}`)
        const data = await response.json();
        console.log(data)
    }

    const deleteProject = async (id) => {
        const response = await fetch(`/deleteProject${id}`, {
            method:'DELETE'
        });
        const data = await response.json();
        console.log(data)
    }

    useEffect(() => {
        getProjects();
    }, [])

  return (
      <div className='container'>
        <div className='project_text'>
            <h1>Projects</h1>
        </div>
        <div className='project_table_container'>
            <table className='projects_table' border=''>
                <thead className='project_titles'>
                    <tr className='text_head'>
                        <th>Project Title</th>
                        <th>Author</th>
                        <th>Submittion Date</th>
                        <th>State</th>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody className="project_table-body">
                        {search.map(project => (
                            <tr className='text_body'>
                            <td>{project._name}</td>
                            <td>{project._author}</td>
                            <td>{project._submissionDate}</td>
                            <td>{project._state}</td>
                            <td>
                            <div>
                                <button 
                                className='publish_button'
                                onClick={()=> publishProject(project._id_project)}
                                >
                                Publish
                                </button>
                            </div>
                            </td>
                            <td>
                            <div>
                                <button 
                                className='discard_button'
                                onClick={()=> deleteProject(project._id_project)}
                                >
                                Discard
                                </button>
                            </div>
                            </td>
                        </tr>
                        ))}
                </tbody>
            </table>
        </div>
      </div>
  )
}

export default ProjectTable