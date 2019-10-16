<script>
  // props
  export let list;
  export let activeKey;

  console.log(list);
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
  <ul class="list">
    {#each list as entry, i (entry.state)}
      <li class="entry">
        <dl class="detail">
          <dt class="key">
            {entry.state.trim()}
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
