<script>
  // props
  export let list;
</script>

<style lang="scss">
  @import './src/variables.scss';

  .list {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .entry {
    display: flex;
    padding: 1rem;
    flex-direction: column;
    list-style: none;
    background: $red;
    color: $white;

    &:nth-child(even) {
      background: $white;
      color: $red;
    }
  }

  .detail {
    display: flex;
    margin: 0;
  }

  .key {
    font-weight: bold;

    &::after {
      content: ":";
      color: bold;
    }
  }
  
  .value {
    margin-left: 0.25rem;
  }
</style>

<template lang="html">
  <ul class="list">
    {#each list as entry, i}
      <li class="entry" key="{i}">
        <dl class="detail">
          <dt class="key">State</dt>
          <dt class="value">{entry.state}</dt>
        </dl>
      </li>
    {/each}
  </ul>
</template>
