<script>
  // props
  export let list;
</script>

<style lang="scss">
  .list {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .entry {
    display: flex;
    padding: 0;
    flex-direction: column;
    list-style: none;

    & + & {
      margin-top: 1rem;
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
          <dt class="key">Rank</dt>
          <dt class="value">{entry.rank}</dt>
        </dl>
        <dl class="detail">
          <dt class="key">State</dt>
          <dt class="value">{entry.state}</dt>
        </dl>
      </li>
    {/each}
  </ul>
</template>
