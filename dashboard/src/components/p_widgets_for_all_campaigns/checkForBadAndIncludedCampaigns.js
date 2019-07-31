//@format

function checkForBadAndIncludedCampaigns(widgets) {
  let hasBadAndIncludedCampaignsCount = 0;
  for (let widget of widgets) {
    if (widget.has_bad_and_included_campaigns === true) {
      hasBadAndIncludedCampaignsCount += 1;
    }
  }
  return hasBadAndIncludedCampaignsCount;
}

export default checkForBadAndIncludedCampaigns;
