//@format
require('../../config/config');
require('./db/mongoose');

const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

const fs = require('fs');
const addToList = require('./addToList');

const login = require('./controllers/user_controllers/login');
const logout = require('./controllers/user_controllers/logout');

const authenticate = require('./middleware/authenticate');
const User = require('./models/user');

///////////// Middleware /////////////////
app.use(bodyParser.json());

//---------------------------------------
//////// User routes //////////////
app.post('/api/users/login', login);

app.delete('/api/users/logout', authenticate, logout);
//---------------------------------------

//////// Campaign sets route //////////////
app.get('/api/readcampaignsets', (req, res) => {
  fs.readFile('../../campaign_sets/campaign_sets.json', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    res.send(data);
  });
});
//---------------------------------------

//////// exclude routes //////////////

app.post('/api/excludecampaignforoneporcwidget', authenticate, (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/misc/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'exclude_campaign_for_one_p_or_c_widget.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

//---------------------------------------

//////// widget list routes //////////////
app.get('/api/readwhitelist', (req, res) => {
  fs.readFile('../../widget_lists/whitelist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.get('/api/readgreylist', (req, res) => {
  fs.readFile('../../widget_lists/greylist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.get('/api/readblacklist', (req, res) => {
  fs.readFile('../../widget_lists/blacklist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.post('/api/addtolist', authenticate, (req, res) => {
  res.json(addToList(req.body.widgetID, req.body.listType));
});

//---------------------------------------

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen(process.env.PORT, () => {
  console.log(`dashboard server running on port ${process.env.PORT}`);
});
