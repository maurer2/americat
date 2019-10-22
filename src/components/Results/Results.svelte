<script>
  import { fly } from 'svelte/transition';
  import Entry from '../Entry';

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

  .list-entry {
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
</style>

<template lang="html">
  <ul class="list" in:fly="{{x: 5000, duration: 250, delay: 250}}">
    {#each list as entry, i (entry.state)}
      <li class="list-entry">
        <Entry entry={entry} activeKey={activeKey} />
      </li>
    {/each}
  </ul>
</template>
