<script>
  import { fly } from 'svelte/transition';

  // props
  export let list;
  export let activeKey;
</script>

<style lang="scss">
  @import './src/variables.scss';

  .list {
    margin: 0;
    padding: 0;
    list-style: none;

    @supports (scroll-snap-type: y) and (scroll-snap-align: start) {
      height: 100vh;
      overflow-y: scroll;
      scroll-snap-type: y;
    }
  }

  .entry {
    display: flex;
    list-style: none;
    background: $red;
    color: $white;

    @supports (scroll-snap-type: y) and (scroll-snap-align: start) {
      scroll-snap-align: start;
    }

    &:nth-child(even) {
      background: $white;
      color: $red;
    }
  }

  .postal-code {
    flex-basis : 4rem;
    padding: 0.75rem 1rem;
    text-decoration: none;
    text-align: center;
    background: $blue;
    color: $white;
    font-weight: bold;
    text-transform: uppercase;
  }

  .detail {
    display: flex;
    margin: 0;
    padding: 0.75rem 1rem;
    flex-grow: 1;
  }

  .key {
    display: flex; // workaround whitespaces
    font-weight: bold;

    &::after {
      content: ":";
      color: bold;
    }
  }

  .value {
    display: flex; // workaround whitespaces
    margin-left: 0.25rem;
  }
</style>

<template lang="html">
  <ul class="list" in:fly="{{x: 5000, duration: 250, delay: 250}}">
    {#each list as entry, i (entry.state)}
      <li class="entry">
        <abbr class="postal-code" title={entry.state}>
          {entry.postalCode}
        </abbr>
        <dl class="detail">
          <dt class="key">
            {entry.state}
          </dt>
          <dt class="value">
            <span class="number">{entry[activeKey]}</span>
            <span class="unit">{(activeKey === 'householdsWithCats') ? '%' : ''}</span>
          </dt>
        </dl>
      </li>
    {/each}
  </ul>
</template>
