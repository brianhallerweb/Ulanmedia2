//@format
require('../../../config/config');
const mongoose = require('mongoose');
const User = require('../models/user');

// this script is for removing extra tokens in the database
// tokens can accumulate in they database if they
// are removed or manipulated by the user in the browser.
// Accumulating tokens won't cause any problems but keeping
// the database clean would be nice. Regularly removing tokens
// from the database would also be a way of effectively expiring
// tokens in the browser. Tokens never expire in the HTML 5
// localStorage API.

// As of 10/31/18, I decided not to set up a CRON job for this script
// because I don't think excess tokens are likely to ever be a problem.
// If they do become a problem, or if you just want to clear them out
// to clean the database, then this is the script to use.

function removeTokens(email) {
  return User.findOne({email}).then(user =>
    User.findByIdAndUpdate(user.id, {tokens: []}),
  );
}

mongoose
  .connect(process.env.MONGODB_URI)
  .then(() => removeTokens('michael@hallerweb.com'))
  .then(() => mongoose.disconnect());
