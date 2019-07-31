//@format

function checkForMismatchVolWeightAndRecWeight(offers) {
  let mismatchOffersCount = 0;
  for (let offer of offers) {
    if (offer.has_mismatch_vol_weight_and_rec_weight) {
      mismatchOffersCount += 1;
    }
  }
  return mismatchOffersCount;
}

export default checkForMismatchVolWeightAndRecWeight;
