<script>
  // modules
  import { onMount } from "svelte";

  // components
  import Header from '../Header';
  import Navigation from '../Navigation';
  import Results from '../Results';

  // props
  // export let list;

  // reactive vars
  $: list = [];
  $: listUnsorted = list.slice();
  $: sortBy = 'rank';
  $: keys = getKeys(listUnsorted);
  $: listSorted = getSortedList(listUnsorted, sortBy);

  // vars
  const url = 'data.json';
  const visibleFields = [
    'rank',
    'state',
    'householdsWithCats',
    'catPopulationAbsolute',
    'catsPerHouseholdAbsolute'
  ];

  // life cycle hooks
  onMount(() => {
    fetchData(url).then((data) => {
        const transformedData = transformData(data);
        
        list = transformedData;
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

  function fetchData(url) {
    const newList = fetch(url)
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

  function transformData(rawData) {
    const transformedData = rawData.map((entry) => {
      const entryWithSelectedKeys = Object.keys(entry).reduce((total, current) => {
        const isVisible = visibleFields.includes(current);
        let newTotal = total;
        
        if (isVisible) {
          newTotal[current] = entry[current];
        }

        return newTotal
      }, {});

      return entryWithSelectedKeys;
    });

    return transformedData;
  }

</script>

<style lang="scss">
  @import './src/variables.scss';

  .wrapper {
    display: grid;
    position: relative;
    margin: 0 auto;
    grid-template-areas:
      "header"
      "main"
      "footer"
    ;
    color: $test;
  }

  .main {
    grid-area: main;
  }

</style>

<template lang="html">
  <div class="wrapper">
    <Header>
      {#if list.length > 0}
        <Navigation
          on:sortBy={(key) => handleSortChange(key)}
          keys={keys}
          activeKey={sortBy}
        />
      {/if}
    </Header>
    {#if list.length > 0}
      <main class="main">
        <Results list={listSorted} />
      </main>
    {/if}
  </div>

</template>
