<script>
  // imports
  import { onMount } from "svelte";

  // components
  import Header from '../Header';
  import Navigation from '../Navigation';
  import Results from '../Results';
  import Loader from '../Loader';
  
  // vars
  let listFetched = fetchData(url);
  let sortBy = 'rank';
  let listSorted = [];
  let keys = [];

  const url = 'data.json';
  const visibleFields = [
    'rank',
    'state',
    // 'householdsWithCats',
    'catPopulationAbsolute',
    'catsPerHouseholdAbsolute'
  ];

  // reactive vars
  $: {
    listSorted = listFetched
      .then((listUnfiltered) => {
        const transformedList = transformData(listUnfiltered);
        const sortedList = getSortedList(transformedList, sortBy);

        return sortedList;
      })
      .catch((error) => {
        return error;
      });

    keys = listSorted
      .then((list) => {
        const extractedKeys = getKeys(list);

        return extractedKeys;
      })
      .catch((error) => {
        return error;
      });
  };

  // life cycle hooks
  onMount(() => {});

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
        return error;
      });

    return newList;
  }

  function transformData(rawData) {
    const transformedData = rawData.map((entry) => getEntryWithVisibleKeys(entry));

    return transformedData;
  }

  function getEntryWithVisibleKeys(entry) {
    const entryWithSelectedKeys = Object.keys(entry).reduce((total, current) => {
        const isVisible = visibleFields.includes(current);
        
        if (isVisible) {
          total[current] = entry[current];
        }

        return total
      }, {});

    return entryWithSelectedKeys
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
  }

  .main {
    grid-area: main;
  }
</style>

<template lang="html">
  <div class="wrapper">
    <Header>
      {#await keys then keys}
        {#if keys.length > 0}
          <Navigation
            on:sortBy={(key) => handleSortChange(key)}
            keys={keys}
            activeKey={sortBy}
          />
        {/if}
      {/await}
    </Header>
    {#await listSorted}
      <Loader />
    {:then listSorted}
      <main class="main">
        <Results list={listSorted} />
      </main>
    {:catch error}
      Error has occured
    {/await}
  </div>
</template>
