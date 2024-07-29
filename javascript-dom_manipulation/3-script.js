const header = document.querySelector('header');
const tHeader = document.querySelector('#toggle_header');

tHeader.addEventListener('click', function() {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  }
  else if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  }
});
