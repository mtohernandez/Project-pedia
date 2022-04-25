import React, {useEffect, useState} from "react";
import './projects.css'

import ProjectCard from "./ProjectCard";

const Projects = () => {

    const [search, setSearch] = useState([])
    const [title, setTitle] = useState('')

    const [activeuser, setActiveuser] = useState([])

    const getActive = async () => {
        const res = await fetch(`/getUser`)
        const data = await res.json();
        setActiveuser(data)
    }

    const getProjects = async () => {
        const response = await fetch(`/getProjects`)
        const data = await response.json();
        setSearch(data)
    }

    const searchProjects = async (title) => {
        const response = await fetch(`/searchProjects${title}`)
        const data = await response.json();
        setSearch(data)
    }

    useEffect(() => {
        getProjects();
        getActive();
    }, [])

    return(
        <div className="app">
        <div className="project-search">
            <input
            type='text'
            placeholder="Seach project"
            value={title}
            onChange={e => setTitle(e.target.value)}
            />
            {console.log(activeuser)}
            <button onClick={e => searchProjects(title)}>
                SEARCH
            </button>
            {activeuser['_typeu'] === 'student' ? (
                <a href="createP"><button>
                    CREATE
                </button></a>
            ):(
                <>
                </>
            )}
        </div>
            {
            search?.length > 0 ? (
            <div className="container">
                {search.map((project)=>
                <ProjectCard project={project}/>  
                )}
            </div>
            ):(
            <div className="text">
                <h2>NOTHING FOUND</h2>
            </div>
            )}
        </div>
    )
}

export default Projects;