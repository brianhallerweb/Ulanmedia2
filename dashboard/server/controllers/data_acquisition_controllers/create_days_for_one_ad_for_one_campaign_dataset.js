//@format
const {PythonShell} = require('python-shell');

function createDaysForOneAdForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.adImage, req.body.volID],
  };
  PythonShell.run(
    'create_days_for_one_ad_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOneAdForOneCampaignDataset;
