const el = document.querySelector('header');
const redEl = document.querySelector('#red-header');

redEl.onclick = function() {
  el.style.color = '#FF0000';
}
