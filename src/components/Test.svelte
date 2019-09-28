<script>
  export let title;
</script>

<style lang="scss">
  $test: red;

  .title {
    color: $test;
  }
</style>

<h1 class="title">
  {title} HTML plain
</h1>

<template lang="pug">
  h1.title
    | {title} pug
</template>
