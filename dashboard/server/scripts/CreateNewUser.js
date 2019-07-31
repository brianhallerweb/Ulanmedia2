//@format
require('../../../config/config')
const mongoose = require("mongoose")
const User = require('../models/user')

// this script is used to create a new user. There is only one 
// user in the database (michael@hallerweb) so this script was only run once. 
function createNewUser(email, password){
    const user = new User( { email, password})
    //this function returns a token but there isn't 
    //a use for the token. The reason for for the return
    //is to ensure that the async par of generateAuthToken 
    //(the saving to the database part) completes before
    //createNewUser() is popped off the stack  
    return user.generateAuthToken()
}

mongoose.connect(process.env.MONGODB_URI)
	.then(() => createNewUser("michael@hallerweb.com", ""))
	.then(() => mongoose.disconnect()) 

