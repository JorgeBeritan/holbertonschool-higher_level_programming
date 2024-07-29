const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const charElement = document.getElementById('character');

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
	}
    return response.json();
  })
  .then(data => {
    const name = data.name;
    charElement.textContent = name;
  })
  .catch(error => {
    charElement.textContent = 'Error al cargar el nombre';
  });
