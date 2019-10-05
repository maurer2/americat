<script>
  // props
  export let list;
</script>

<style lang="scss">
</style>

<template lang="html">
  Results { list.length }

  <code>
    <pre>
      { JSON.stringify(list, null, 2) }
    </pre>
  </code>
</template>