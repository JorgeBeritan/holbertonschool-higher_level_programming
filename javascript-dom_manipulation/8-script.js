const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
const hello = document.getElementById('hello');

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
	}
    return response.json();
  })
  .then(data => {
    hello.textContent = data.hello;
  })
  .catch(error => {
    hello.innerHTML = 'Nop';
  });
