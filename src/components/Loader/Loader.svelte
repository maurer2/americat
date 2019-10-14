<script>
  import logo from './logo.svg';
  // props
  export let list;
</script>

<style lang="scss">
  .loader {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: grayscale(85%);
  }

  .logo {
    display: block;
    padding: 1rem;
  }
</style>

<template lang="html">
  <div class="loader">
    <img class="logo" src={ logo } alt="" />
  </div>
</template>
