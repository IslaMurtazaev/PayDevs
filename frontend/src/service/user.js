import axios from "axios";

export const UserService = {
  login,
  logout,
  create_user
};

function login(username, password) {
  return axios
    .post(
      "/api/users/login",
      JSON.stringify({ username, password })
    )
    .then(res => {
      let user = res.data;
      if (user.token) localStorage.setItem("user", JSON.stringify(user));
      return res.data;
    })
}

function create_user(username, email, password) {
  return axios
    .post(
      "/api/users/create",
      JSON.stringify({ username, email, password })
    )
    .then(res => {
      let user = res.data;
      if (user.token) localStorage.setItem("user", JSON.stringify(user));
      return res.data;
    });
}

function logout() {
  localStorage.removeItem("user");
}
