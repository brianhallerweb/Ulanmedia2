//@format
const path = require('path');

module.exports = {
  entry: './src/app.js',
  output: {
    path: path.join(__dirname, 'public'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        loader: 'babel-loader',
        test: /\.js$/,
        exclude: /node_modules/,
      },
      {
        test: /\.s?css$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
    ],
  },
  devtool: 'cheap-module-eval-source-map',
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    proxy: [
      {
        context: ['/api/'],
        target: 'http://localhost:3000',
      },
      {
        context: ['/jsonapi/'],
        target: 'http://localhost:5000',
      },
    ],
    historyApiFallback: true,
  },
};
