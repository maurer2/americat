import App from './components/App';

const dummyData = [
  {
    rank: '48',
    state: 'Utah',
  },
  {
    rank: '47',
    state: 'New Jersey',
  },
  {
    rank: '46',
    state: 'Louisiana',
  },
];

const currentApp = new App({
  target: document.body,
  props: {
    list: dummyData,
  },
});

export default currentApp;
