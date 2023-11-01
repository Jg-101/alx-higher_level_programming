// Adds an LI elem to the list when the div#add_item tag is clicked
// The new elem must be <li>Item</li> and must be added to UL.my_list

$('div#add_item').click(function () {
  let element = '<li>Item</li>';
  $('ul.my_list').append(element);
});
