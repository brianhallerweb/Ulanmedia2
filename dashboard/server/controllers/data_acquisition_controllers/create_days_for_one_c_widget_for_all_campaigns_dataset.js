//@format
const {PythonShell} = require('python-shell');

function createDaysForOneCWidgetForAllCampaignsDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.cWidgetID],
  };
  PythonShell.run(
    'create_days_for_one_c_widget_for_all_campaigns_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOneCWidgetForAllCampaignsDataset;
