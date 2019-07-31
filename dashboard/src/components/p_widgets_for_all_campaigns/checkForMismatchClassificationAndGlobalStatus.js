//@format

function checkForMismatchClassificationAndGlobalStatus(widgets) {
  let mismatchWidgetsCount = 0;
  for (let widget of widgets) {
    if (widget.has_mismatch_classification_and_global_status) {
      mismatchWidgetsCount += 1;
    }
  }
  return mismatchWidgetsCount;
}

export default checkForMismatchClassificationAndGlobalStatus;
