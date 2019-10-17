# Svelte 3

---

## What is Svelte?

* Reactive frontend framework
* Component based
* Doesn't use a VDOM implementation
* Heavily influenced by VueJS
* Last major release in April 2019

---

## Features

* Uses single file components
* Components provide style encapsulation by default
* Support for PostCSS & SCSS
* Can be used with Webpack, Rollup or Parcel
* No runtime-environment necessary
* Fast and low bundle size
* Partial support for Pug
* SSR via additional framework Sapper
* Quite fast

---

## Disadvantages

* Developer tools are quite barebones
* Typescript support poor
* No support for JSX or TSX
* Only partial support for Pug
* No bundler-free version as of v3
* no CLI like CRA or Vue CLI as of v3
* Lack of ports of popular third party libraries
* A lot of outdated tutorials
* No support for CSS-in-JS frameworks like SC

---

## Ideal use cases

* Low powered devices
* Low bandwidth connections

---

## Anatomy of a Svelte component

```
<script>
  js-stuff
</script>

<style>
  css-stuff
</style>

<div>
  html-stuff
</div>
```

---

## Javascript

```javascript
<script>
  // imports
  import ChildComponent from './ChildComponent.svelte';
  // props
  export let data;
  // function
  function getValue(id) {
    return data.find((entry) => entry.id === id);
  }
  // reactive var
  $: value = getValue('123');
  $: value2 = data.every((entry) => entry.id !== '123');
  // non reactive var
  const salutation = 'Howdy';
</script>

---

## CSS

```css
<style>
  .wrapper {
    margin: 0 auto;
    border: 1px solid var(--gray);
  }
</style>
```

```css
<style>
  .wrapper.svelte-123456 {
    margin: 0 auto;
    border: 1px solid var(--gray);
  }
</style>
```

---

## HTML

```html
<div class="parent">
  <ChildComponent value={ value } text="text" />
  <ChildComponent value={ x === 25 } />
  
  <h1 class="className">
    Title
  </h1>
  <label for="field">Label</label>
</div>
```

```html
<template lang="html">
  <div class="parent">
    .....
  </div>
</div>
```

---

## Svelte template language

---

## Control structures

```
<{#if id === 25}
  <p>Test</p>
{/if}

<{#if id === 25}
  <p>Test</p>
{:else}
  <p>Test 2</p>
{/if}

<{#if id === 25}
  <p>Test</p>
{:else if id === 52}
  <p>Test 2</p>
{:else}
  <p>Test 3</p>
{/if}
```

---

## List rendering

```
<ul>
  {#each list as listItem, i (listItem.id)}
    <li>{i} {listItem}</li>
  {/each}
</ul>

<ul>
  {#each list as listItem, i (listItem.id)}
    <li>{i} {listItem}</li>
  {:else}
    No entries
  {/each}
</ul>
```

---

## Slots for reusability

```html
<div class="v-card">
  <slot name="title">>
    <h1>Default title</h1>
  </slot>
  <slot name="hobby">>
    Musicals
  </slot>
</div>
```

```html
<script>
  import VCard from './VCard.svelte';
</script>

<VCard>
  <div slot="title">
    <h2>Real title</h2>
  <div>
<VCard>
```

---

## Slots for composition

```html
<div class="parent">
  <ChildComponent value={ value } />

  <ChildComponent value={ value } />
    <h2>{salutation}</h2>
  </ChildComponent>
</div>
```

```html
<div class="child">
  <h1>Title {value}</h1>
  <slot>
    Optional default content
  </slot>
</div>
```

---

## Events

```
<a href="/" on:click={doSomething}>
  Text
</a>

<a
  href="/"
  on:click|once|preventDefault|stopPropagation={doSomething}
>
	Text
</a>
```


---

## Event handling between components

```html
<div class="parent">
  <!-- Handle child event in parent -->
  <ChildComponent on:childeventname="funcInParent" />

  <!-- Relay child event to grandparent -->
  <ChildComponent on:childeventname />
</div>
```

```html
<script>
  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch('childeventname');
  }
</script>
<div class="child">
  <a href="" on:click|preventDefault={handleButtonClick}>Test</a>
</div>
```

---

## Communication between Components

* Props
* Events
* Two way data binding 
* Context-API
* Store

---

## Declarative promise handling

```html
<script>
  let someAsyncOperation = new Promise((resolve, reject) => {
    .....
  });
</script>
<div class="component">
  {#await someAsyncOperation}
    <Spinner />
  {:then someAsyncOperationReturnValue}
    <MainComponent data={ someAsyncOperationReturnValue } />
  {:catch error}
    <span class="error">dang it - { error }</span>
  {/await}
</div>
```

---

## Declarative transitions and animations

```html
<div class="component">
  <h1 transition:fade="{{ duration: 1000 }}">Titel</h1>
  <h1 in:fade="{{ duration: 500 }}" out:fade="{{ duration: 500 }}">
    Titel
  </h1>
  <h1
    transition:fade
    on:introstart="{() => function() }"
    on:outrostart="{() => function() }"
    on:introend="{() => function() }"
    on:outroend="{() => function() }"
    >
      Titel
  </h1>
</div>
```

---

## Other features
* Life cycle methods (onMount, beforeUpdate, afterUpdate, onDestroy etc.)
* Store

---
