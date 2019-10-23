<style lang="scss">
  @import 'animatewithsass/_properties';
  @import 'animatewithsass/_attention-seekers/tada';

  .header {
    position: sticky;
    top: 0;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    grid-area: header;
    background: #3c3b6e;
    z-index: 1;
  }

  .title {
    margin: 1rem;
    align-items: flex-start;
    font-family: 'USA', Arial, sans-serif;
    font-weight: normal;
    font-size: 2.5rem;
    color: #ffffff;
    cursor: default;
  }

  title:hover {
    transform-origin: left center;
  }

</style>

<header class="header">
  <h1 class="title">
    Americat
  </h1>
  <slot/>
</header>

