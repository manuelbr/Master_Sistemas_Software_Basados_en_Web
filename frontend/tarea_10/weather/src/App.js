import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


class App extends Component {
  constructor() {
    super();
    this.state = {
      busqueda: 0
    };
  }
  render() {
    const activePlace = this.state.activePlace;
    return (
      <div className="App">
        <div class="container">
          <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
            <a class="navbar-brand" id="busqueda"
              onClick={() => {
                  if(this.state.busqueda == 0){
                      this.state.busqueda = 1;
                  }
              }}>
              Búsqueda</a>

            <a class="navbar-brand" id="inicio"
                onClick={() => {
                    if(this.state.busqueda == 1){
                        this.state.busqueda = 0;
                    }
                }}>
                Inicio</a>
            </div>
          </div>
          </nav>
          /*
            AQUI VA LA BARRA DE BÚsqueda
            incluir BOOTSTRAp.
          */

        <MovieDisplay movie={/*Nombre cogido del buscador*/} />
      </div>
    );
  }
}

class MovieDisplay extends Component {
  constructor() {
    super();
    this.state = {
      movieData: null
    };
  }

  componentDidMount() {
    var movie = this.props.movie;
    movie = movie.replace(" ","+");
    const URL = "https://api.themoviedb.org/3/search/movie?api_key=13126f034aad28bc9e7ca1d5c3973e44&query=" + movie;
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ movieData: json });
    });
  }

  render() {
    const movieData = this.state.movieData;
    if (!movieData) return <div>Cargando...</div>;
    const pelicula = movieData.results[0];
    const caratula = "http://image.tmdb.org/t/p/w185/" + pelicula.poster_path;
    return (
      <div>
        <h1>
          <img src={caratula}/>
        </h1>
        <p>{pelicula.title}</p>
        <p>Nota media: {pelicula.popularity}</p>
        <p>Fecha de estreno: {pelicula.release_date}</p>
        <p>Sinopsis: {pelicula.overview}</p>
      </div>
    );
  }

}

export default App;
