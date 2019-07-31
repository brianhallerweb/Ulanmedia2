//@format
const {PythonShell} = require('python-shell');

function createMonthsForOneCWidgetForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.cWidgetID, req.body.volID],
  };
  PythonShell.run(
    'create_months_for_one_c_widget_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createMonthsForOneCWidgetForOneCampaignDataset;
