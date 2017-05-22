import React, { Component } from 'react';

class WeatherDisplay extends Component {
  constructor() {
      super();
      this.state = {
        weatherData: null
      };
  }

  componentDidMount() {
      const zip = this.props.zip;
      const URL = "http://api.openweathermap.org/data/2.5/weather?q=" +
        zip +
        "&appid=b1b35bba8b434a28a0be2a3e1071ae5b&units=imperial";
      fetch(URL).then(res => res.json()).then(json => {
        this.setState({ weatherData: json });
      });
  }

  render() {
    return (
      const weatherData = this.state.weatherData;
      if (!weatherData) return <div>Loading</div>;
        return <div>{JSON.stringify(weatherData)}</div>;
    );
  }
}
