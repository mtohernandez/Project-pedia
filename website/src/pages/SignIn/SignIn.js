import React, {useState, useEffect} from 'react'
import './signIn.css'

const SignIn = () => {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const [active, setActive] = useState('NO')

  // FIX THIS FOR LATER IT NEED A PURPOSE
  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(`/signIn/${email}/${password}`)
    const data = await res.json();
    console.log(data)
  }

  const getActive = async (e) => {
    e.preventDefault();
    const res = await fetch(`/signIn/${email}/${password}`)
    const data = await res.json();
    console.log(data)
    setActive(data['message'])
  }

  function isOk(email, password){
    if(email.trim() !== '' && password.trim() !== ''){
      return true
    }else{
      return false
    }
  }


  return (
    <div className='signin-whole'>
      <div className='signin-form'>
        <form className='signin-form_body' method='post'>
          <h1>SIGN IN</h1>
          <div className='signin-form_body-input'>
            <label>Email</label>
            <input
            type='text'
            onChange={e => setEmail(e.target.value)}
            value={email}
            className='form-control'
            placeholder='Email'
            autoFocus/>
          </div>
          <div className='signin-form_body-input'>
            <label>Password</label>
              <input
              type='password'
              onChange={e => setPassword(e.target.value)}
              value={password}
              className='form-control'
              placeholder='Password'
              autoFocus/>
          </div>
          <div>
            <button className="signup-form_body-input" onClick={getActive}>
                SEARCH
            </button>
          </div> 
        </form>
        {isOk(email, password) && active === 'OK' ? (
              <>
              <a href='projects'><button className="signup-form_body-input">
                SIGN IN
              </button>
              </a>
              </>
            ):(
              <>
              <h1>USER NOT FOUND</h1>
              </>
            )}
      </div>
    </div>
  )
}

export default SignIn