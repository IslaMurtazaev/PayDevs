import React from "react";
import logo from "../assets/icons/favicon.png";
import { Link } from "react-router-dom";

const NavBar = () => {
  const logOut = () => {
    localStorage.clear();
  };

  const isLogged = () => {
    return localStorage.getItem("user") !== null;
  };

  return (
    <div className="navbar">
        <div>
          <Link to="/">
            <img alt="PayDev logo" src={logo} />
            <strong className="navbarPaydevs">PayDevs</strong>
          </Link>
        </div>

      {isLogged() ? (
        <a href="/login">
          <button className="btn logout link" onClick={logOut}>
            Logout
          </button>
        </a>
      ) : (
        <span>
          <Link className="link" to="/sign_up">
            Sign up
          </Link>
          <Link className="link" to="/login">
            Login
          </Link>
        </span>
      )}
    </div>
  );
};

export default NavBar;
