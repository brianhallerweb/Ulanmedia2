//@format

function checkForBadAndIncludedCampaigns(campaigns) {
  let badAndIncludedCampaignsCount = 0;
  for (let campaign of campaigns) {
    if (campaign.is_bad_and_included === true) {
      badAndIncludedCampaignsCount += 1;
    }
  }
  return badAndIncludedCampaignsCount;
}

export default checkForBadAndIncludedCampaigns;
