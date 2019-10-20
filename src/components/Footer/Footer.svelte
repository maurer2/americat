<script>
  import iconList from './icon-list.svg';

  // props
  export let list;
</script>

<style lang="scss">
  @import './src/variables.scss';
  @import 'animatewithsass/_properties';
  @import "animatewithsass/_attention-seekers/flash";

  $bp-row: 26rem;

  .footer {
    grid-area: footer;
    display: flex;
    padding: 1rem;
    flex-direction: column-reverse;
    text-align: center;
    background: $red;
    color: $white;

    @media only screen and (min-width: $bp-row) {
      flex-direction: row;
      flex-wrap: wrap-reverse;
      text-align: inherit;
    }

    .message {
      &--is-flashing {
        display: block;

        @include flash(
          $duration: 2.5s,
          $count: infinite,
          $delay: 0s,
          $function: ease, 
        );
      }
    }
  }
  
  .quote {
    margin-left: auto;
    margin-right: auto;
    margin-top: 0.5rem;
    font-style: italic;
    text-transform: capitalize;

    @media only screen and (min-width: $bp-row) {
      margin-top: 0;
      margin-left: 0;
    }

    &:before {
      content: open-quote;
    }

    &:after {
      content: close-quote;
    }
  }

  .status {
    margin: 0;
  }

  .icon {
    vertical-align: baseline;
  }

</style>

<template lang="html">
  <footer class="footer">
    <quote class="quote">
      Semper feline
    </quote>
    <p class="status">
      {#await list}
        <span class="message message--is-flashing">
          Data is being loaded
        </span>
      {:then list}
        <span class="message">
          <img class="icon icon--list" src={iconList} alt="" />
          {list.length} entries have been loaded
        </span>
      {/await}
    </p>
  </footer>
</template>
