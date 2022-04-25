import React, { useEffect, useState, useRef } from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';


import Home from './pages/Home/Home.js'
import Projects from './pages/Projects/Projects.js'
import Organizations from './pages/Organizations/Organizations.js'
import FAQ from './pages/FAQ/FAQ.js'
import About from './pages/About/About.js'
import SignUp from './pages/SignUp/SignUp';
import SignIn from './pages/SignIn/SignIn';
import CreateP from './pages/Projects/CreateP/CreateP';

import Navbar from './components/Navbar/Navbar';
import Project from './pages/Projects/Project/Project';

import * as THREE from 'three'
import FOG from '../node_modules/vanta/dist/vanta.fog.min'
import TOPOLOGY from '../node_modules/vanta/dist/vanta.topology.min'
import ProjectTable from './pages/manager/ProjectTable';


function App(){
  const [vantaEffect, setVantaEffect] = useState(0)
  
  useEffect(() => {
     if (!vantaEffect) {
        setVantaEffect(FOG({
          el: "#background",
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          highlightColor: 0x72582a,
          midtoneColor: 0x7d7d0d,
          lowlightColor: 0xffffff,
          baseColor: 0x0,
          blurFactor: 0.50,
          speed: 0.50,
          zoom: 0.60,
        })
      )}       
  
      return () => {
        if (vantaEffect) vantaEffect.destroy()
      }
    }, [vantaEffect])

  
  return (
    <div className='App'> 
      <div>
      <Router>        
            <Navbar/>    
            <Route path= "/" exact component={Home}/>
            <Route path= "/projects" exact component={Projects}/>
            <Route path= "/organizations" component={Organizations}/>
            <Route path= "/FAQ" component={FAQ}/>
            <Route path= "/about" component={About}/>    
            <Route path= "/signUp" component={SignUp}/> 
            <Route path= "/signIn" component={SignIn}/>   
            <Route path= "/createP" component={CreateP}/> 
            <Route path='/project/:id' component={Project}/>
            <Route path='/manager' component={ProjectTable}/>
        </Router>
      </div> 
    </div>
    
  );
}

export default App;
