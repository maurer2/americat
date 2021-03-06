const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const autoPreprocess = require('svelte-preprocess');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'public'),
  },
  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.svelte$/,
        use: {
          loader: 'svelte-loader',
          options: {
            emitCss: true,
            hotReload: true,
            preprocess: autoPreprocess(),
          },
        },
      },
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            babelrc: true,
          },
        },
      },
      {
        test: /\.(css)$/,
        use: [
          {
            loader: 'style-loader',
            options: {},
          },
          {
            loader: 'css-loader',
            options: {},
          },
        ],
      },
      {
        test: /\.(woff|woff2)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: '/',
            },
          },
        ],
      },
      {
        test: /\.(svg)$/,
        use: [
          {
            // loader: 'svg-inline-loader',
            loader: 'svg-url-loader',
            options: {},
          },
        ],
      },
    ],
  },
  plugins: [
    // new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.html',
      hash: true,
    }),
    new CopyPlugin([
      { from: 'api/results/data.json', to: 'json/states-ranking.json' },
      { from: 'api/results/postal-codes.json', to: 'json/postal-codes.json' },
    ]),
    new BundleAnalyzerPlugin({
      analyzerMode: 'disabled',
      generateStatsFile: false,
      statsOptions: {
        source: false,
      },
    }),
  ],
  devServer: {
    contentBase: path.join(__dirname, 'public'),
    compress: false,
    port: 9000,
    watchContentBase: true,
    hot: false,
    inline: true,
  },
};
