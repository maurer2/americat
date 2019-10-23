const autoPreprocess = require('svelte-preprocess');

module.exports = async ({ config }) => {
  const svelteLoader = config.module.rules.find(r => r.loader && r.loader.includes('svelte-loader'));

  svelteLoader.options = {
    ...svelteLoader.options,
    preprocess: autoPreprocess(),
  }

  return config;
};