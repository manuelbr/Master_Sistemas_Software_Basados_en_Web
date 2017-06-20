import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.css";
import { Navbar, Nav, Button} from "react-bootstrap";

class App extends Component {
  constructor() {
    super();
    this.state = {
      busqueda: 0,
      texto: " ",
    };
  }

  updateInputValue(event) {
    this.setState({
      texto: event.target.value
    });
  }

  render() {
    let principal;
    let buscar;
    let resultados;
    let inicial;

    principal = (
      <Navbar>
        <Navbar.Brand bsStyle="tabs" onClick={() => {
                      this.setState({
                        busqueda: 0
                      });
                    }}
        >
          Inicio
        </Navbar.Brand>
        <Navbar.Header>
        <Navbar.Brand bsStyle="tabs" onClick={() => {
                          this.setState({
                            busqueda: 1
                          });
                        }}
        >
          Búsqueda
        </Navbar.Brand>
        </Navbar.Header>
      </Navbar>
    )

    inicial = (
      <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Buscador de Películas</h2>
      </div>
    )

    buscar = (
      <Navbar.Form>
        <h2>Búsqueda de película</h2>
        <div class="form-group">
          <input type="text" name="term" onChange={ this.updateInputValue.bind(this)} id="term" placeholder="Busqueda" class="form-control"/>
        </div>
        <br></br>
        <Button bsStyle="primary" onClick={() => { this.setState({ busqueda: 2}); }}>Buscar</Button>
      </Navbar.Form>
    )

    resultados = (
      <MovieDisplay movie={this.state.texto} />
    )

    if(this.state.busqueda === 0){
        return (
          <div className="App">
          { principal }
          { inicial }
          </div>
        )
    }else
        if(this.state.busqueda === 1){
          return (
            <div className="App">
            { principal }
            { buscar }
            </div>
          )
        }else
          if(this.state.busqueda === 2){
            return (
              <div className="App">
              { principal }
              { resultados }
              </div>
            )
          }
  }
}

class MovieDisplay extends Component {

  constructor(){
    super();
    this.state = {
      movieData: null
    };
  }

  componentDidMount() {
    var movie = this.props.movie;
    movie = movie.split(' ').join('+');
    const URL = "https://api.themoviedb.org/3/search/movie?api_key=13126f034aad28bc9e7ca1d5c3973e44&query=" + movie;
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ movieData: json });
    });
  }

  render() {
    const movieData = this.state.movieData;
    if (!movieData) return <div>{this.state.movieData}</div>;
    const pelicula = movieData.results[0];
    const caratula = "http://image.tmdb.org/t/p/w185/" + pelicula.poster_path;
    return (
      <div>
        <h1>
          <img src={caratula} alt="caratula"/>
        </h1>
        <p>{pelicula.title}</p>
        <p>Nota media: {pelicula.vote_average}</p>
        <p>Fecha de estreno: {pelicula.release_date}</p>
        <div id="sinopsis">
          <p>Sinopsis: {pelicula.overview}</p>
        </div>
      </div>
    );
  }
}

export default App;
