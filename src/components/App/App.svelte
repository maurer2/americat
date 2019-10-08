<script>
  // modules
  import { onMount } from "svelte";

  // components
  import Header from '../Header';
  import Picker from '../Picker';
  import Results from '../Results';

  // props
  // export let list;

  // reactive vars
  $: list = [];
  $: listUnsorted = list.slice();
  $: sortBy = 'rank';
  $: keys = getKeys(listUnsorted);
  $: listSorted = getSortedList(listUnsorted, sortBy);

  // life cycle hooks
  onMount(() => {
    fetchData().then((data) => {
        list = data;
      });
  });

  // functions
  function getSortedList(list, sortBy) {
    const listSorted = list.sort((elementFirst, elementSecond) => {
      const sortElementFirst = elementFirst[sortBy];
      const sortElementSecond = elementSecond[sortBy];

      return sortElementFirst.localeCompare(sortElementSecond, undefined, {numeric: true});
    });

    return listSorted;
  }

  function getKeys(list) {
    const keyBag = list.flatMap((entry) => Object.keys(entry)); 
    const keySet = keyBag.filter((entry, index, entries) => entries.indexOf(entry) === index);

    return keySet;
  }

  function handleSortChange(event) {
    const key = event.detail;

    console.log('received sortBy event:', key);
    sortBy = key;
  }

  function fetchData() {
    const newList = fetch('data.json')
      .then((response) => {
        if (response.ok) {
          let jsonData;

          try {
            jsonData = response.json();
          } catch (error) {
            return new Error(error);
          }

          return jsonData;
        }
      })
      .catch((error) => {
        console.log(error);
      });

    return newList;
  }

  function transformData() {

  }

</script>

<style lang="scss">
  $test: black;

  // usa colors
  $blue: #3C3B6E;
  $white: #FFFFFF;
  $red: #B22234;

  .wrapper {
    display: grid;
    position: relative;
    margin: 0 auto;
    grid-template-areas:
      "header"
      "main"
    ;
    overflow: visible;
    color: $test;
  }

  .main {
    grid-area: main;
    padding: 1rem;
  }

</style>

<template lang="html">
  <div class="wrapper">
    <Header>
      <slot>
        {#if list.length > 0}
          <Picker
            on:sortBy={(key) => handleSortChange(key)}
            keys={keys}
            activeKey={sortBy}
          />
        {/if}
      </slot>
    </Header>
    {#if list.length > 0}
      <main class="main">
        <Results list={listSorted} />
      </main>
    {/if}
  </div>

</template>
