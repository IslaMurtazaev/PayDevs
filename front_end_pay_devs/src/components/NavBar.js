import React from 'react';
import logo from "./icons/favicon.png";
import { Link } from "react-router-dom";
import { authHeader } from "../service/helpers";



const NavBar = () => {
    return (
        <div className="navbar">
            <img src={logo} />          
            <span><Link  className="paydevs1" to= '/'>PayDevs</Link></span>
            {authHeader() ? <Link className="link" to="/login">Logout</Link> : <Link className="link" to="/sign_up">Sign up</Link>}
            {}
        </div>
    );
}
 
export default NavBar;
