import 'normalize.css';
import App from './components/App';

const list = [
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
    list,
  },
});

export default currentApp;
