# Svelte 3

---

## What is Svelte?

* Reactive frontend framework
* Component based
* Supports PostCSS & SCSS
* Can be used with Webpack, Rollup or Parcel
* No bundler-free version as of v3 (unlike Vue)
* no CLI like CRA or Vue CLI as of v3
* tagline "Cybernetically enhanced web apps" 🤔
* Supports SSR via additional framework Sapper (similar to VueJs and Nuxt)
* Out of the box scoped CSS (similar to Vue and styled-jsx in React)
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

## How does a Svelte component look like?

wfwefew

```javascript
<script>
  // props
  export let data;

  // functions
  function getValue(id) {
    const value = data.find((entry) => entry.id === id);

    return value;
  }

  // reactive var
  $: value = getValue('123');

  // non reactive var
  const value2 = 5

</script>

<style>
  .wrapper {
    margin: 0 auto;
    border: 1px solid var(--gray);
  }
</style>

<article class="wrapper">
    <ChildComponent players={ players } />
</article>
```

## Communication between Components

* Parent to child via props
* Child to parent via events

## Svelte template language

* Dummy
* Slots (similar to slots in Vue and props.children in React)

---

## Good parts

* Fast
* Scoped styling
* Easy to pick up when coming from Vue
* Reactivity quite easy

---

## Bad parts

* Getting it running is kinda tedious (no CLI)
* Small community
* A lot of outdated info due to fast evolving framework
* Bus factor (few active core members)
* Tooling is kind meh
* No support for CSS-in-JS frameworks like SC