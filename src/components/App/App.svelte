<script>
  // imports
  import { onMount } from 'svelte';

  // components
  import Header from '../Header';
  import Main from '../Main';
  import Footer from '../Footer';
  
  import Navigation from '../Navigation';
  import Results from '../Results';
  import Loader from '../Loader';
  
  // vars
  const urlStateRanking = 'json/states-ranking.json';
  const urlPostalCodes = 'json/postal-codes.json';
  const visibleFields = [
    'rank',
    'state',
    'householdsWithCats',
    'catPopulationAbsolute',
    'catsPerHouseholdAbsolute',
  ];

  const dataFetching = new Promise((resolve) => {
    const dataSources = Promise.all([
      fetchData(urlStateRanking),
      fetchData(urlPostalCodes),
    ]);

    setTimeout(() => {
      resolve(dataSources);
    }, 2500);

    return dataSources;
  });

  let [sortBy] = visibleFields;
  let stateRankingList = [];
  let keys = [];

  // reactive vars
  $: {
    stateRankingList = dataFetching
      .then(([stateRankingFetched, postalCodesFetched]) => {
        const transformedList = getTransformedData(stateRankingFetched);
        const mergedList = getStateRankingWithPostalCodes(transformedList, postalCodesFetched);
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

        return new Error();
      })
      .catch((error) => error);

    return newList;
  }

  function getStateRankingWithPostalCodes(stateRankingList, postalCodesList) {
    const mergedList = stateRankingList.map((entry) => {
      const { state } = entry;
      const postalCodes = Object.keys(postalCodesList);
      const postalCode = postalCodes.find((codeEntry) => postalCodesList[codeEntry] === state);
      const mergedEntry = { ...entry, postalCode };

      return mergedEntry;
    });

    return mergedList;
  }

  function getSortedList(list, sortByKey) {
    const sortByIsInList = list.some((listEntry) => Object.keys(listEntry).includes(sortByKey));

    if (!sortByIsInList) {
      return list;
    }

    const listSorted = list.slice().sort((elementFirst, elementSecond) => {
      const sortElementFirst = elementFirst[sortByKey].toString();
      const sortElementSecond = elementSecond[sortByKey].toString();

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
      const newTotal = total;
  
      if (isVisible) {
        newTotal[current] = entry[current];
      }

      return newTotal;
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
    min-height: 100%;
    grid-template-rows: auto 1fr auto; 
    grid-template-areas:
      "header"
      "main"
      "footer"
    ;
  }
</style>

<template lang="html">
  <article class="wrapper">
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
    <Main>
      {#await stateRankingList}
        <Loader />
      {:then stateRankingList}
        <Results list={stateRankingList} activeKey={sortBy} />
      {:catch error}
        An error has occured
      {/await}
    </Main>
    <Footer class="test" list={stateRankingList} />
  </article>
</template>
