//@format

function checkForBadAndIncludedPWidgets(pWidgets) {
  let badAndIncludedPWidgetsCount = 0;
  for (let pWidget of pWidgets) {
    if (pWidget.is_bad_and_included === true) {
      badAndIncludedPWidgetsCount += 1;
    }
  }
  return badAndIncludedPWidgetsCount;
}

export default checkForBadAndIncludedPWidgets;
