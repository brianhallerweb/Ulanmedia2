//@format
const User = require('../../models/user');

function login(req, res) {
  // this conditional is my temporary way of validating the user password
  // I don't know the correct way to validate so, for now, I am just
  // checking that the password isn't too long.
  if (req.body.password.length > 15) {
    res.status(404).send('password too long');
  } else {
    User.findByCredentials(req.body.email, req.body.password)
      .then(user => {
        return user.generateAuthToken().then(token => {
          res.header('x-auth', token).send(user);
        });
      })
      .catch(err => {
        res.status(500).send(err);
      });
  }
}

module.exports = login;
