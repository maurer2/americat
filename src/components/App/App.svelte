<script>
  // components
  import Picker from '../Picker';
  import Results from '../Results';

  // props
  export let list;

  // reactive vars
  $: keys = getKeys(list);
  $: listSorted = getSortedList(list);

  // functions
  function getSortedList(list) {
    console.log(list);
  }

  function getKeys(list) {
    const keyBag = list.flatMap((entry) => Object.keys(entry)); 
    const keySet = keyBag.filter((entry, index, entries) => entries.indexOf(entry) === index);

    return keySet;
  }

  function handleSortChange(event) {
    const key = event.detail;
    console.log('received sortBy event:', key);
  }
</script>

<style global lang="scss">
  $test: black;

  html {
    box-sizing: border-box;
    font-size: 16px;
  }

  *,
  *:before,
  *:after {
    box-sizing: inherit;
  }

  body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: $test;
  }
</style>

<template lang="html">
  <div class="wrapper">
    <header class="header">
      <h1 class="title">
        Americat
      </h1>
    </header>
    <main class="main">
      <Picker on:sortBy={(key) => handleSortChange(key)} keys={keys} />
      <Results list={list} />
    </main>
  </div>

</template>
