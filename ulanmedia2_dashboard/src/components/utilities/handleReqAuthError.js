//@format

function handleReqAuthError(res) {
  const refresh_token = localStorage.getItem('refresh_token');

  if (!refresh_token) {
    localStorage.removeItem('access_token');
  }

  if (!res.ok) {
    if (res.status == 401) {
      localStorage.removeItem('access_token');
    } else {
      fetch(`/jsonapi/token/refresh`, {
        method: 'POST',
        headers: {Authorization: `Bearer ${refresh_token}`},
      })
        .then(res => {
          if (!res.ok) {
            if (res.status == 401) {
              localStorage.removeItem('access_token');
              return 'you need to login again';
            }
          }
          return res.json();
        })
        .then(res => {
          localStorage.setItem('access_token', res.access_token);
        })
        .catch(err => console.log(err));
    }
  }
}

export default handleReqAuthError;
