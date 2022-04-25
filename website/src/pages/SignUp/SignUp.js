import React, { useState, useEffect } from 'react'
import './signUp.css'

const SignUp = () => {

    // Company
    // Professor
    // Student 
    // Manager
    // Person 

    // Id User
    // Name
    // Email
    // Password
    // Address

    const [name, setName] = useState("");
    const [lastname, setlastName] = useState("");
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [addressZipCode, setAddressZipCode] = useState("")
    const [addressStreet, setAddressStreet] = useState("")
    const [addressCity, setAddressCity] = useState("")
    const [addressCountry, setAddressCountry] = useState("")
    const [addressDeparment, setAddressDeparment] = useState("")
    const [type, setType] = useState("")

    const [studentCode, setCode] = useState("")
    const [coursenumber, setCourse] = useState("")
    const [professor, setProfessor] = useState("")
    const [nitnumber, setNitnumber] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault();
        const res = await fetch(`/signUp${type}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name,
                lastname,
                email,
                password,
                addressZipCode,
                addressCity,
                addressCountry,
                addressDeparment,
                addressStreet,
                studentCode,
                coursenumber,
                professor,
                nitnumber,
            })
        })
        const data = await res.json();
        console.log(data)
    }

    const searchProfessor = async (cnumber) => {
        const res = await fetch(`/searchProfessor${cnumber}`)
        const data = await res.json();
        setProfessor(data['professor'])
    }

    useEffect(()=>{
        searchProfessor(coursenumber)
    }, [coursenumber])
    
    function isOk(name, lastname, email, password, addressZipCode, addressCity, addressCountry, addressDeparment, addressStreet){
        if(name.trim() !== "" && lastname.trim() !== "" && email.trim() !== "" && password.trim() !== "" && addressZipCode.trim() !== "" && addressCity.trim() !== "" && addressCountry.trim() !== "" && addressDeparment.trim() !== "" && addressStreet.trim() !== ""){
            return true
        } else {
            return false
        } 
    }

    return (
        <div className='signup-whole'>
            <div className='signup-form'>
                <form onSubmit={handleSubmit} className='signup-form_body' method='post'>
                    <h1>JOIN THE FUTURE</h1>
                    <div className='signup-form_body-input'>
                        <label>Name</label>
                        <input
                        type='text'
                        onChange={e => setName(e.target.value)}
                        value={name}
                        className='form-control'
                        placeholder='Name'
                        autoFocus/>
                    </div>
                    {
                       type !== 'company' ? (
                           <>
                           <div className='signup-form_body-input'>
                            <label>Last Name</label>
                            <input
                            type='text'
                            onChange={e => setlastName(e.target.value)}
                            value={lastname}
                            className='form-control'
                            placeholder='Last Name'
                            autoFocus/>
                        </div>
                           </>
                       ):(<></>)
                    }
                    <div className='signup-form_body-input'>
                        <label>Email</label>
                        <input
                        type='text'
                        onChange={e => setEmail(e.target.value)}
                        value={email}
                        className='form-control'
                        placeholder='Email'/>
                    </div>
                    <div className='signup-form_body-input'>
                        <label>Password</label>
                        <input
                        type='password'
                        onChange={e => setPassword(e.target.value)}
                        value={password}
                        placeholder='Password'/>
                    </div>
                    <div className='signup-form_body-input'>
                        <label>Address</label>
                        <input
                        type='text'
                        onChange={e => setAddressZipCode(e.target.value)}
                        value={addressZipCode}
                        placeholder='Zip Code'
                        />
                        <input
                        type='text'
                        onChange={e => setAddressStreet(e.target.value)}
                        value={addressStreet}
                        placeholder='Street'
                        />
                        <input
                        type='text'
                        onChange={e => setAddressCity(e.target.value)}
                        value={addressCity}
                        placeholder='City'
                        />
                        <input
                        type='text'
                        onChange={e => setAddressCountry(e.target.value)}
                        value={addressCountry}
                        placeholder='Country'
                        />
                        <input
                        type='text'
                        onChange={e => setAddressDeparment(e.target.value)}
                        value={addressDeparment}
                        placeholder='Department'
                        />
                    </div>
                    <div className='signup-form_body-input'>
                        <label>Account Type</label>
                        <select onChange={e => setType(e.target.value)}>
                                <option selected disabled>Category:</option>
                                <option value="student">Student</option>
                                <option value="company">Company</option>
                                <option value="professor">Professor</option>
                                <option value="manager">Manager</option>
                                <option value="person">Person</option>
                        </select> 
                    </div>
                    <div>
                    {type === '' ? (
                        <>
                        </>
                    ): type === 'student' ? (
                        <>
                        <div className='signup_form-addition'>
                            <label>Student Code</label>
                            <input
                            type='text'
                            onChange={e => setCode(e.target.value)}
                            value={studentCode}
                            placeholder='Student Code'
                            />
                        </div>
                        <div className='signup_form-addition'>
                            <label>Course Number</label>
                            <select onChange={e => setCourse(e.target.value)}>
                                <option selected disabled>NRC:</option>
                                <option value="1493">1493</option>
                                <option value="1243">1243</option>
                                <option value="4930">4930</option>
                                <option value="2077">2077</option>
                                <option value="3072">3072</option>
                            </select>
                        </div>
                        <div className='signup_form-addition'>
                            <label>Professor</label>
                            <h1>{professor}</h1>
                        </div>
                        </>
                    ): type === 'company' ? (
                        <>
                        <div className='signup_form-addition'>
                            <label>NIT NUMBER</label>
                            <input
                            type='text'
                            onChange={e => setNitnumber(e.target.value)}
                            value={nitnumber}
                            placeholder='Nit Number'
                            />
                        </div>
                        </>
                    ): type === 'professor' ? (
                        <>
                        <div className='signup_form-addition'>
                        <label>Course Number</label>
                            <select onChange={e => setCourse(e.target.value)}>
                                <option selected disabled>NRC:</option>
                                <option value="1493">1493</option>
                                <option value="1243">1243</option>
                                <option value="4930">4930</option>
                                <option value="2077">2077</option>
                                <option value="3072">3072</option>
                            </select>
                        </div>
                        </>
                    ):(
                        <>
                        </>
                    )}
                    {isOk(name, lastname, email, password, addressZipCode, addressCity, addressCountry, addressDeparment, addressStreet) ? (
                        <>
                        <button className="signup-form_body-input">
                            SIGN UP
                        </button>
                        </>
                    ):(
                        <>
                        </>
                    )}
                    </div>
                </form>
                
            </div>
        </div>
    )
}

export default SignUp;