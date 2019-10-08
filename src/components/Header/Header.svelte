<script>

</script>

<style lang="scss">
  @import './src/variables.scss';

  .header {
    position: sticky;
    top: 0;
    grid-area: header;
    background: $blue;

    &:after {
      content: '';
      position: absolute;
      left: 0;
      top: 100%;
      right: 0;
      height: 1rem;
      background: linear-gradient(to bottom, rgba(white, 1) 0%, rgba(white, 0) 100%);
    }
  }

  .title {
    margin: 1rem;
    font-family: 'USA', Arial, sans-serif;
    font-weight: normal;
    font-size: 2.5rem;
    color: $white;
  }

</style>

<template lang="html">
  <header class="header">
    <h1 class="title">
      Americat
    </h1>
    <slot/>
  </header>
</template>
