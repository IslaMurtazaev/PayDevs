export function authHeader() {
  let user = JSON.parse(localStorage.getItem("user"));

  if (user && user.token) {
    return { Authorization: user.token };
  } else {
    return {};
  }
}

export function handleError(error) {
  if (error.response) {
    alert(error.response.data.error.message);
  } else {
    alert(error.response.data.error.message);
  }
}

export function configAxios() {
  return { headers: authHeader };
}
