import Test from './components/Test.svelte';

const test = new Test({
  target: document.body,
  props: {
    title: 'Americat',
  },
});

export default test;
