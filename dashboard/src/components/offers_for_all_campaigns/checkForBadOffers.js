//@format

function checkForBadOffers(offers) {
  let badOffersCount = 0;
  for (let offer of offers) {
    if (offer.classification === 'bad') {
      badOffersCount += 1;
    }
  }
  return badOffersCount;
}

export default checkForBadOffers;
