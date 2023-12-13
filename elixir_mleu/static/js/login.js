/* Simple VanillaJS to toggle class */

document.getElementById('toggleProfile').addEventListener('click', function () {
  [].map.call(document.querySelectorAll('.profile'), function(el) {
    el.classList.toggle('profile--open');
  });
});

document.getElementById("login_button").addEventListener('click', function()
                                                        {
    location.href = "index.html";    
});