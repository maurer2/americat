module.exports = {
  extends: [
    'airbnb-base',
  ],
  env: {
    "browser": true,
    "node": true,
  },
  plugins: [
    'svelte3',
  ],
  overrides: [
    {
      files: ['**/*.svelte'],
      processor: 'svelte3/svelte3'
    }
  ],
  rules: {
    'import/first': 'off',
    'import/no-mutable-exports': 'off',
    'no-labels': 'off',
    'no-restricted-syntax': ['error', 'ForInStatement', 'ForOfStatement', 'WithStatement'],
    // 'import/prefer-default-export': 'off',
  },
  settings: {
    'svelte3/ignore-styles': false,
  },
};
