//@format

function checkForBadCountries(countries) {
  let badCountriesCount = 0;
  for (let country of countries) {
    if (country.classification === 'bad') {
      badCountriesCount += 1;
    }
  }
  return badCountriesCount;
}

export default checkForBadCountries;
