// https://github.com/UnwrittenFun/svelte-vscode/issues/1#issuecomment-495927947
const sass = require('node-sass');

module.exports = {
  preprocess: {
    style: async ({ content, attributes }) => {
      if (attributes.type !== 'text/scss' && attributes.lang !== 'scss') {
        return false;
      }

      return new Promise((resolve, reject) => {
        sass.render({
          data: content,
          sourceMap: true,
          outFile: 'x', // this is necessary, but is ignored
        }, (error, result) => {
          if (error) {
            return reject(error);
          }

          const { css: code, map: sourceMap } = result;

          return resolve({
            code: code.toString(),
            map: sourceMap.toString(),
          });
        });
      });
    },
  },
};
