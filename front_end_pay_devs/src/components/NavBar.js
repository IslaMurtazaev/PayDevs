import React from "react";
import logo from "./icons/favicon.png";
import { Link } from "react-router-dom";
import {PrivateRoute} from '../route/PrivateRoute'


const NavBar = () => {

  return (
    <div className="navbar">
    

      <img src={logo} />
      <span >
        <Link className="paydevs" to="/">
          PayDevs
        </Link>
      </span>
      
      <span>
       { PrivateRoute ?    
      <Link className="link" to="/login">
          Logout
      </Link> : null }
      </span>
    
    </div>
  );
};

export default NavBar;
