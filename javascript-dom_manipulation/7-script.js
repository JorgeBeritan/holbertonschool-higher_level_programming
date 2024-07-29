const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.getElementById('list_movies');

fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
	}
    return response.json();
  })
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const li = document.createElement('li');
	  li.textContent = movie.title;
      listMovies.appendChild(li);
	});
  })
  .catch(error => {
    listMovies.innerHTML == '<li>Error to download the movies</li>';
  });
