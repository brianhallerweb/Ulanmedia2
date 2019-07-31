//@format
const User = require('../../models/user');

function logout(req, res) {
  req.user
    .removeToken(req.token)
    .then(() => {
      res.status(200).send();
    })
    .catch(() => {
      res.status(500).send();
    });
}

module.exports = logout;
