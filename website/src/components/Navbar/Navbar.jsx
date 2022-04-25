import React, {useEffect, useState} from 'react'
import './navbar.css'
import { NavLink as Link } from 'react-router-dom';
import logo from '../../assets/logowhite.svg'

const Navbar = () => {

  const [activeuser, setActiveuser] = useState([])

  const getActive = async () => {
    const res = await fetch(`/getUser`)
    const data = await res.json();
    console.log(data)
    setActiveuser(data)
  }

  const deleteActive = async () => {
    const res = await fetch(`/deleteActive`, {
      method: 'DELETE'
    })
    const data = await res.json();
    console.log(data)
  }

  useEffect(()=>{
   getActive()
  },[])

  return (
    <div className='navbar'>
        <div className='navbar-links'>
            <div className='navbar-links_logo'>
            <a href='/'><img src={logo} alt='logo' width={50} className='zoom-text'></img></a>
            </div>
            <div className='navbar-links_container'>
                <div className='zoom-text'><p><a href='/'>HOME</a></p></div>
                <div className='zoom-text'><p><a href='/projects'>PROJECTS</a></p></div>
                <div className='zoom-text'><p><a href='/organizations'>ORGANIZATIONS</a></p></div>
                <div className='zoom-text'><p><a href='/FAQ'>FAQ</a></p></div>
                <div className='zoom-text'><p><a href='/about'>ABOUT</a></p></div>
                {activeuser['_typeu'] == 'manager' ? (
                  <>
                  <div className='zoom-text'><p><a href='/manager'>DASHBOARD</a></p></div>
                  </>
                ):(
                  <>
                  </>
                )}
            </div>
            <div className='navbar-user'>
              <h1>{console.log(activeuser)}</h1>
            </div>
                {activeuser.length === 0 ? (
                  <>
                  <div className='navbar-signin'>
                  <a href='/signIn'><button type='button'>SIGN IN</button></a>
                  </div>
                  <div className='navbar-signup'>
                  <a href='/signUp'><button type='button'>SIGN UP</button></a>
                  </div>
                  </>
                ):( 
                  <>
                  <div className='navbar-signin'>
                  <a href='/signIn'><button type='button' onClick={deleteActive}>LOG OFF</button></a>
                  </div>
                  </>
                )}
        </div>
    </div>
  )
}

export default Navbar