<script>
  // props
  export let list;
</script>

<style lang="scss">
  @import './src/variables.scss';

  $row-bp: 25rem;

  .footer {
    grid-area: footer;
    display: flex;
    padding: 1rem;
    flex-direction: column-reverse;
    text-align: center;
    background: $red;
    color: $white;

    @media only screen and (min-width: $row-bp) {
      flex-direction: row;
      flex-wrap: wrap-reverse;
      text-align: inherit;
    }
  }
  
  .quote {
    margin-left: auto;
    margin-right: auto;
    margin-top: 0.5rem;

    @media only screen and (min-width: $row-bp) {
      margin-top: 0;
      margin-left: 0;
    }
  }

  .status {
    margin: 0;
  }

</style>

<template lang="html">
  <footer class="footer">
    <quote class="quote">
      Semper felines
    </quote>
    <p class="status">
      {#await list}
        Data is being loaded
      {:then list}
        <strong>{list.length}</strong> results have been loaded
      {/await}
    </p>
  </footer>
</template>
