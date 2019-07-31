//@format
const {PythonShell} = require('python-shell');

function createDaysForOneCWidgetForOneCampaignReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.cWidgetID, req.body.volID],
  };
  PythonShell.run(
    'create_days_for_one_c_widget_for_one_campaign_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOneCWidgetForOneCampaignReport;
