//@format
const {PythonShell} = require('python-shell');

function createGprsForEachPOfferDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.dateRange],
  };
  PythonShell.run(
    'create_gprs_for_each_p_offer_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createGprsForEachPOfferDataset;
