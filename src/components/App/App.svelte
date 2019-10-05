<script>
  // components
  import Picker from '../Picker';
  import Results from '../Results';

  // props
  export let list;

  console.log(list);
</script>

<style lang="scss">
  $test: red;

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
    <main>
      <Picker />
      <Results list={ list } />
    </main>
  </div>

</template>
