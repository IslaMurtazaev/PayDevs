import React from "react";
// import logo from "./icons/favicon.png";
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
      {/* <img alt="PayDev logo" src={logo} /> */}
      <span>
        <Link className="paydevs1" to="/">
          PayDevs
        </Link>
      </span>

      {isLogged() ? (
        <a href="/login">
          <button className="logout link" onClick={logOut}>
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
