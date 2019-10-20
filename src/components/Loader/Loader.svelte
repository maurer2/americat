<script>
  import { fade } from 'svelte/transition';
  import logo from './logo.svg';
  
  // props
  export let list;
</script>

<style lang="scss">
  .loader {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .logo {
    display: block;
    padding: 1rem;
    flex-basis: 10vw;
  }

</style>

<template lang="html">
  <div class="loader" out:fade="{{ duration: 250 }}">
    <img class="logo" src={ logo } alt="" />
  </div>
</template>
