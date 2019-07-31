//@format

function checkForBadAndIncludedCampaigns(campaigns) {
  let badAndIncludedCampaignsCount = 0;
  for (let campaign of campaigns) {
    if (campaign.classification === 'bad' && campaign.status == 'included') {
      badAndIncludedCampaignsCount += 1;
      campaign['badAndIncluded'] = true;
    }
  }
  return badAndIncludedCampaignsCount;
}

export default checkForBadAndIncludedCampaigns;
