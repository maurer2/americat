<script>
  // components
  import Picker from '../Picker';
  import Results from '../Results';

  // props
  export let list;

  console.log(list);
</script>

<style global lang="scss">
  $test: red;

  html {
    box-sizing: border-box;
    font-size: 16px;
  }

  *,
  *:before,
  *:after {
    box-sizing: inherit;
  }

  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .title {
    color: $test;
  }
</style>

<template lang="html">
  <div class="wrapper">
    <header class="header">
      <h1 class="title">
        Americat
      </h1>
    </header>
    <main class="main">
      <Picker />
      <Results list={ list } />
    </main>
  </div>

</template>
