const ul = document.querySelector('#my_list');
const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function() {
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  ul.appendChild(li);
});
