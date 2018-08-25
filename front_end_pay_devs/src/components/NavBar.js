import React from "react";
import logo from "./icons/favicon.png";
import { Link } from "react-router-dom";
import { authHeader } from "../service/helpers";

const NavBar = () => {

  return (
    <div className="navbar">
      <img src={logo} />
      <span>
        <Link className="paydevs" to="/">
          PayDevs
        </Link>
      </span>
      {authHeader() ? (
        <Link className="link" to="/sign_up">
          Sign up
        </Link>
      ) : (
        <Link className="link" to="/login">
          Login
        </Link>
      )}
      <Link className="link" to="/login">
        Logout
      </Link>
      {}
    </div>
  );
};

export default NavBar;
