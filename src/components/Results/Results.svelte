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
    list-style: none;
    background: $red;
    color: $white;

    &:nth-child(even) {
      background: $white;
      color: $red;
    }
  }

  .postal-code {
    width: 4rem;
    padding: 1rem;
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
    padding: 1rem;
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
  <ul class="list">
    {#each list as entry, i (entry.state)}
      <li class="entry">
        <abbr class="postal-code" title={entry.state}>
          {entry.state.substring(0, 2)} <!-- placeholder -->
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
