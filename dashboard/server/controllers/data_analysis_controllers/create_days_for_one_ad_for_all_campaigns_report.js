//@format
const {PythonShell} = require('python-shell');

function createDaysForOneAdForAllCampaignsReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.adImage],
  };
  PythonShell.run(
    'create_days_for_one_ad_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOneAdForAllCampaignsReport;
