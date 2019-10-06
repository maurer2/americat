const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const sveltePreprocess = require('svelte-preprocess');
const scss = require('svelte-preprocess');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

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
            preprocess: [
              sveltePreprocess({}),
              scss([]),
            ],
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
    ],
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'src/index.html',
      hash: true,
    }),
    new BundleAnalyzerPlugin({
      analyzerMode: 'disabled',
      generateStatsFile: true,
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
