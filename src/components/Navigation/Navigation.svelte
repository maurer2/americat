<script>
  import { createEventDispatcher } from 'svelte';

  // props
  export let keys;
  export let activeKey;

  // local vars
  const dispatch = createEventDispatcher();
  const buttonLabels = {
    rank: 'Overall rank',
    state: 'State',
    householdsWithCats: 'Households with cats',
    catPopulationAbsolute: 'Cat population',
    catPopulationRelative: 'Cat population (relative)',
    catsPerHouseholdAbsolute: 'Cats per household',
    catsPerHouseholdRelative: 'Cats per household (relative)',
    postalCode: 'Postal code',
  }

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

  .navigation {
    display: flex;
    width: 100%;
    flex-wrap: wrap;
  }

  .button {
    display: flex;
    padding: 0.5rem;
    flex-grow: 1;
    flex-shrink: 0;
    flex-basis: 50%;
    justify-content: center;
    align-items: center;
    background: $white;
    border: 0;
    appearance: none;
    color: $blue;
    outline: 0;
    cursor: pointer;

    @media only screen and (min-width: 30rem) {
      flex-basis: auto;
    }

    &--is-active {
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
  <div class="navigation">
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