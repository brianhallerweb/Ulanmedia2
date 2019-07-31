//@format

function checkForBadLanguages(languages) {
  let badLanguagesCount = 0;
  for (let language of languages) {
    if (language.classification === 'bad') {
      badLanguagesCount += 1;
    }
  }
  return badLanguagesCount;
}

export default checkForBadLanguages;
