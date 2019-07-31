//@format
const {PythonShell} = require('python-shell');

function createMonthsForOneAdForAllCampaignsDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.adImage],
  };
  PythonShell.run(
    'create_months_for_one_ad_for_all_campaigns_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createMonthsForOneAdForAllCampaignsDataset;
