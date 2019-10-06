<script>
  import { createEventDispatcher } from 'svelte';

  // props
  export let keys;

  // local vars
  const dispatch = createEventDispatcher();

  // functions
  function handleButtonClick(key) {
    // svelte2
    // this.fire('sortBy', { key });

    // svelte 3
    dispatch('sortBy', key);
  }
</script>

<style lang="scss">
  .picker {
    margin-bottom: 1rem;
  }

  .title {
    font-size: 1rem;
  }
</style>

<template lang="html">
  <div class="picker">
    <h2 class="title">
      Sort by
    </h2>
    <div class="button-group">
      {#each keys as key}
        <button
          class="key"
          key={key}
          on:click|stopPropagation={() => handleButtonClick(key)}
        >
          {key}
        </button>
      {/each}
    </div>
  </div>
</template>