//@format

function checkForBadAds(ads) {
  let badAdsCount = 0;
  for (let ad of ads) {
    if (ad.classification === 'bad') {
      badAdsCount += 1;
    }
  }
  return badAdsCount;
}

export default checkForBadAds;
