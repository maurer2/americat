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
  @import './src/variables.scss';

  .picker {
    position: relative; // osx focus ring above fade-line
    display: flex;
    margin-bottom: 0;
    flex-wrap: wrap;
    z-index: 1;
  }

  .button {
    display: flex;
    padding: 0.5rem;
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: 33%;
    justify-content: center;
    align-items: center;
    appearance: none;
    border: 1px solid $blue;
    color: $blue;

    @media only screen and (min-width: 35rem) {
      flex-basis: 0;
    }

    &--is-active {
      position: relative; // new stacking context to have osx focus ring on top of other buttons
      background: $red;
      color: $white;
    }

    .icon {
      width: 1rem;
      height: 1rem;
      flex-shrink: 0;
      fill: currentColor;
      visibility: hidden;

      &--is-active {
        visibility: visible;
      }
    }

    .text {
      padding: 0 0.5rem;
      flex-grow: 1; // force stars to edges
    }
  }

</style>

<template lang="html">
  <div class="picker">
    {#each keys as key}
      <button
        class="button {key === activeKey ? 'button--is-active' : ''}"
        key={key}
        on:click|stopPropagation={() => handleButtonClick(key)}
      >
        <svg class="icon {key === activeKey ? 'icon--is-active' : ''} " viewbox="0 0 260 245">
          <path d="m55,237 74-228 74,228L9,96h240"/>
        </svg>
        <span class="text">
          {getButtonLabel(key)}
        </span>
        <svg class="icon {key === activeKey ? 'icon--is-active' : ''} " viewbox="0 0 260 245">
          <path d="m55,237 74-228 74,228L9,96h240"/>
        </svg>
      </button>
    {/each}
  </div>
</template>