const webpack = require('webpack');
const path = require('path');

const PATHS = {
  app: './src/index.js',
  html: './src/index.html',
  dist: path.join(__dirname, 'dist')
};

module.exports = {
  entry: {
    html: PATHS.html,
    javascript: PATHS.app
  },
  output: {
    path: PATHS.dist,
    publicPath: '/',
    filename: '[name].js'
  },
  devServer: {
    contentBase: PATHS.dist
  },
  module: {
    loaders: [
      {
        test: /\.html$/,
        loader: "file-loader?name=[name].[ext]"
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        query:
        {
          presets:['react']
        }
      }
    ]
  }
};
