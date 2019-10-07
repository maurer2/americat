<script>
  import { createEventDispatcher } from 'svelte';

  // props
  export let keys;
  export let activeKey;

  let buttonLabels = {
    rank: 'Rank',
    state: 'State',
    householdsWithCats: 'Households with cats',
    catPopulationAbsolute: 'Cat population',
    catPopulationRelative: 'Cat population (relative)',
    catsPerHouseholdAbsolute: 'Cats per household',
    catsPerHouseholdRelative: 'Cats per household (relative)',
  }

  // local vars
  const dispatch = createEventDispatcher();

  // functions
  function handleButtonClick(key) {
    // svelte2
    // this.fire('sortBy', { key });

    // svelte 3
    dispatch('sortBy', key);
  }

  function getButtonLabel(activeKey) {
    if (!(activeKey in buttonLabels)) {
      return '';
    }

    return buttonLabels[activeKey];
  }
</script>

<style lang="scss">
  .picker {
    margin-bottom: 0;
  }

  .button-group {
    display: flex;
    flex-wrap: wrap;
  }

  .button {
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 0;
    background: white;

    &--is-active {
      color: red;
    }
  }

</style>

<template lang="html">
  <div class="picker">
    <div class="button-group">
      {#each keys as key}
        <button
          class="button {key === activeKey ? 'button--is-active' : ''}"
          key={key}
          on:click|stopPropagation={() => handleButtonClick(key)}
        >
          {getButtonLabel(key)}
        </button>
      {/each}
    </div>
  </div>
</template>