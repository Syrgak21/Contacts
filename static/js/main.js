(function() {
  var searchField = document.getElementById('search-area');

  var handler = function() {
    var text = searchField.value,
        names = document.getElementsByClassName('contact_info'),
        regexp = RegExp(text, 'i');

    for (var i = 0; i < names.length; i++) {
      var name = names[i];
      contact = document.getElementsByClassName('contact')
      name.innerText.search(regexp) < 0 ?
        contact[i].style.display = 'none' :
        contact[i].style.display = 'flex';
    }
  };

  searchField.addEventListener('input', handler);
})();
