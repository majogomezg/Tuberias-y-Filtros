import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

import node from '@astrojs/node';

export default defineConfig({
  integrations: [react()],

  vite: {
    resolve: {
      alias: {
        '@scripts': '/src/scripts',
        '@layouts': '/src/layouts'
      }
    }
  },

  output: 'server',

  adapter: node({
    mode: 'standalone'
  })
});