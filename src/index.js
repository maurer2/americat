import 'core-js/es';
import 'normalize.css';

import './font.woff';
import './font.woff2';
import './global.css';

import App from './components/App';

const currentApp = new App({
  target: document.body,
  props: {},
});

export default currentApp;
