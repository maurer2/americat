<script>
  // props
  export let entry;
  export let activeKey;
</script>

<style lang="scss">
  @import './src/variables.scss';

  .entry {
    display: flex;
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

    &::after {
      content: ":";
    }
  }

  .value {
    display: flex;
    margin-left: auto;
  }
</style>

<template lang="html">
  <div class="entry">
    <abbr class="postal-code" title={entry.state}>
      {entry.postalCode}
    </abbr>
    <dl class="detail">
      <dt class="key">
        {entry.state}
      </dt>
      <dt class="value">
        <span class="number">
          {#if ['catsPerHouseholdAbsolute', 'householdsWithCats'].includes(activeKey)}
            {entry[activeKey].toFixed(1).toLocaleString('en')}
          {:else if activeKey === 'rank'}
            {entry[activeKey].toLocaleString('en').padStart(2, 0)}
          {:else}
            {entry[activeKey].toLocaleString('en')}
          {/if}
        </span>
        <span class="unit">
          {(activeKey === 'householdsWithCats') ? '%' : ''}
        </span>
      </dt>
    </dl>
  </div>
</template>
