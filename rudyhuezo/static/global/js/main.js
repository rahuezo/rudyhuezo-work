function displayAbility(element) {
  $(element).text(abilities[counter]);

  counter += 1;
  if (counter >= abilities.length) {
    counter = 0;
  }
}
