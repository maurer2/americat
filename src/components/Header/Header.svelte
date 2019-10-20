<style lang="scss">
  @import './src/variables.scss';
  @import 'animatewithsass/_properties';
  @import "animatewithsass/_attention-seekers/tada";

  .header {
    position: sticky;
    top: 0;
    grid-area: header;
    background: $blue;
    z-index: 1;
  }

  .title {
    display: inline-block;
    margin: 1rem;
    font-family: 'USA', Arial, sans-serif;
    font-weight: normal;
    font-size: 2.5rem;
    color: $white;
    cursor: default;

    &:hover {
      transform-origin: left center;

      @include tada(
        $duration: 0.75s,
        $count: 1,
        $delay: 0.25s,
        $function: ease, 
      );
    }
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
