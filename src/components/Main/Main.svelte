<script>
  // props
  export let list;

</script>

<style lang="scss">
  .main {
    position: relative;
    grid-area: main;
  }

</style>

<template lang="html">
  <main class="main">
    <slot/>
  </main>
</template>
