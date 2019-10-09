# Svelte 3

---

## What is Svelte?

* Reactive frontend framework
* Component based
* Supports PostCSS & SCSS
* Out of the box scoped CSS (similar to Vue and styled-jsx in React)
* Can be used with Webpack, Rollup or Parcel
* No bundler-free version as of v3 (unlike Vue)
* no CLI like CRA or Vue CLI as of v3
* tagline "Cybernetically enhanced web apps" 🤔
* Supports SSR via additional framework Sapper (similar to VueJs and Nuxt)
* Supports Pug (kinda)

---

## What is different about Svelte compared to React or Vue?

* No virtual DOM
* Precompiled components
* Uses JS labels for reactivity (supported since ES1)
* No support for JSX or TSX

---

## How does reactivity work in Svelte?

* Dummy

---

## Svelte components

<!-- .slide: style="text-align: left;"> -->
Each Svelte component consists of a javascript-, style- and one or more template-parts

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
  // non reactive var
  const salutation = 'Howdy';
</script>

---

```css
<style>
  <!-- gets compiled to .wrapper.svelte-<randomHash> -->
  .wrapper {
    margin: 0 auto;
    border: 1px solid var(--gray);
  }
</style>
```

---

```html
<div class="parent">
  <ChildComponent value={ value } />

  <ChildComponent value={ value } />
    <h2>{salutation}</h2>
  </ChildComponent>
</div>

<div class="child">
  <h1>Title</h1>
  <slot />
</div>
```

---

## Communication between Components

* Parent to child via props
* Child to parent via events
* Child to parent via bind
* Event emitter
* Context-API
* Store

---

## Compose templates
* Slots (similar to slots in Vue and props.children in React)

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
  <p>Tset</p>
{/if}
<{#if id === 25}
  <p>Test</p>
:else if id === 52}
  <p>Tset</p>
{/if}
```

---

## List rendering

```
<ul>
  {#each list as listItem, i}
    <li>{i} {listItem}</li>
  {/each}
</ul>

<ul>
  {#each list as listItem, i}
    <li>{i} {listItem}</li>
  {:else}
    <p>Empty</p>
  {/each}
</ul>
```

---

## Events

```
<a href="/" on:click={func}>
	Text
</a>

<a
  href="/"
  on:click|once|preventDefault|stopPropagation={func}
>
	Text
</a>
```

---

```
<div class="parent">
  <!-- Handle child event in parent -->
  <ChildComponent on:eventname="funcInParent" />

  <!-- Relay child event to grandparent -->
  <ChildComponent on:eventname />
</div>

<div class="child">
  <h1>Title</h1>
</div>
```

---

## Other stuff
* Life cycle methods
* Store

---

## Good parts

* Fast
* Scoped styling
* Easy to pick up when coming from Vue
* Reactivity quite easy
* Declarative event modifier

---

## Bad parts

* Getting it running is kinda tedious (no CLI)
* Small community
* A lot of outdated info due to fast evolving framework
* Bus factor (few active core members)
* Tooling is kind meh
* No support for CSS-in-JS frameworks like SC
