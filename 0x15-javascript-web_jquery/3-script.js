// Uses the jQuery API to add a red class to the header tag and turn it
// red when the divred_header tag is clicked

$('div#red_header').click(function () {
  $('header').addClass('red');
});
