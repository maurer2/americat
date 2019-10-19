<script>
  // imports
  import { onMount } from 'svelte';

  // components
  import Header from '../Header';
  import Navigation from '../Navigation';
  import Results from '../Results';
  import Loader from '../Loader';
  
  // vars
  let sortBy = 'rank';
  let stateRankingList = [];
  let keys = [];

  const urlStateRanking = 'json/states-ranking.json';
  const urlPostalCodes = 'json/postal-codes.json';
  const visibleFields = [
    'rank',
    'state',
    'householdsWithCats',
    'catPopulationAbsolute',
    'catsPerHouseholdAbsolute',
  ];
  const dataFetching = Promise.all([
    fetchData(urlStateRanking),
    fetchData(urlPostalCodes),
  ]);

  // reactive vars
  $: {
    stateRankingList = dataFetching
      .then(([stateRankingFetched, postalCodesFetched]) => {
        const transformedStateRankingList = getTransformedData(stateRankingFetched);
        const mergedList = getStateRankingWithPostalCodes(transformedStateRankingList, postalCodesFetched);
        const sortedList = getSortedList(mergedList, sortBy);

        return sortedList;
      })
      .catch((error) => error);

    keys = stateRankingList
      .then((list) => getKeys(list))
      .catch((error) => error);
  }

  // life cycle hooks
  onMount(() => {});

  // functions
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

  function getStateRankingWithPostalCodes(stateRankingList, postalCodesList) {
    const mergedList = stateRankingList.map((entry) => {
      const { state } = entry;
      const postalCode = Object.keys(postalCodesList).find(postalCode => postalCodesList[postalCode] === state);
      const mergedEntry = Object.assign({}, entry, { postalCode });

      return mergedEntry;
    });

    return mergedList;
  }

  function getSortedList(list, sortBy) {
    const listSorted = list.slice().sort((elementFirst, elementSecond) => {
      const sortElementFirst = elementFirst[sortBy];
      const sortElementSecond = elementSecond[sortBy];

      return sortElementFirst.localeCompare(sortElementSecond, undefined, { numeric: true });
    });

    return listSorted;
  }

  function getKeys(list) {
    const keyBag = list.flatMap((entry) => Object.keys(entry));
    const keySet = keyBag.filter((entry, index, entries) => entries.indexOf(entry) === index);

    return keySet;
  }

  function getTransformedData(rawData) {
    const transformedData = rawData.map((entry) => getEntryWithVisibleKeys(entry));

    return transformedData;
  }

  function getEntryWithVisibleKeys(entry) {
    const entryWithSelectedKeys = Object.keys(entry).reduce((total, current) => {
      const isVisible = visibleFields.includes(current);
  
      if (isVisible) {
        total[current] = entry[current];
      }

      return total;
    }, {});

    return entryWithSelectedKeys;
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
    {#await stateRankingList}
      <Loader />
    {:then stateRankingList}
      <main class="main">
        <Results list={stateRankingList} activeKey={sortBy} />
      </main>
    {:catch error}
      An error has occured
    {/await}
  </div>
</template>
