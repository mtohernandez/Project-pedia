import React, {useEffect, useState} from 'react'
import './createP.css'

const CreateP = () => {

    const [name, setName] = useState('')
    const [submissionDate, setSubmission] = useState('')
    const [description, setDescription] = useState('')
    const [background, setBackground] = useState('')
    const [active, setActiveuser] = useState([])

    const handleSubmit = async (e) => {
        e.preventDefault();
        const res = await fetch(`/createP`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name,
                description,
                background,
                submissionDate,
            })
        })
        const data = await res.json();
        console.log(data)
    }

    const getActive = async () => {
        const res = await fetch(`/getUser`)
        const data = await res.json();
        setActiveuser(data)
    }

    function isOk(name, description, link, date){
        if(name.trim() !== "" && description.trim() !== "" && link.trim() !== "" && date.trim() !== ""){
            return true
        }else{
            return false
        }
    }

    useEffect(() => {
        getActive();
    }, [])


    return (
        <div className='project-form-whole'>
            <div className='project-form'>
                <h1>CREATE NEW PROJECT</h1>
                <form onSubmit={handleSubmit} className='project-form-body' method='post'>
                    <div className='project-form-input'>
                    <label>Title</label>
                        <input
                        type='text'
                        onChange={e => setName(e.target.value)}
                        value={name}
                        className='form-control'
                        placeholder='Name'/>
                    </div>
                    <div className='project-form-input'>
                    <label>Author</label>
                    <input
                        type='text'
                        onChange={() => {}}
                        value={active['_name'] + ' ' + active['_last_name']}
                        />
                    </div>
                    <div className='project-form-input-description'>
                    <label>Description</label>
                    <textarea
                        rows='8'
                        cols='43'
                        onChange={e => setDescription(e.target.value)}
                        value={description}
                        placeholder='Description'
                        />
                    </div>
                    <div className='project-form-input'>
                    <label>Background Image (URL/ADDRESS)</label>
                    <input
                        type='text'
                        onChange={e => setBackground(e.target.value)}
                        value={background}
                        placeholder='Please copy link address of image and paste it here'
                        />
                    </div>
                    <img className='fade-in' src={background}></img>
                    <div className='project-form-input'>
                    <label>Submission Date</label>
                    <input
                        type='date'
                        onChange={e => setSubmission(e.target.value)}
                        value={submissionDate}
                        />
                    </div>
                    {
                        isOk(name, description, background, submissionDate) ? (
                            <>
                            <button>
                                UPLOAD
                            </button>
                            </>
                        ):(
                            <>
                            </>
                        )
                    }
                </form>
            </div>
        </div>
    )
}

export default CreateP