//@format
const {PythonShell} = require('python-shell');

function createMonthsForOneAdForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.adImage, req.body.volID],
  };
  PythonShell.run(
    'create_months_for_one_ad_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createMonthsForOneAdForOneCampaignDataset;
