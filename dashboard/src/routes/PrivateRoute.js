//@format
import React from 'react';
import {Route, Redirect} from 'react-router-dom';

const PrivateRoute = ({Component, path}) => {
  let isAuthenticated = false;
  const token = localStorage.getItem('token');
  if (token && token.length > 10) {
    isAuthenticated = true;
  }

  return (
    <Route
      path={path}
      render={props =>
        isAuthenticated ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{pathname: '/login', location: props.location.pathname}}
          />
        )
      }
    />
  );
};

export default PrivateRoute;
