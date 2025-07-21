const list = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Convertimos a  json
  .then(data => {
    const films = data.results;

    films.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;

      list.appendChild(li);
    });
  })
  .catch(error => {
    console.error('Error al obtener las películas:', error);
  });