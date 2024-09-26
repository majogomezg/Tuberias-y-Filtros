import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

export default defineConfig({
  integrations: [react()],
  vite: {
    resolve: {
      alias: {
        '@scripts': '/src/scripts',
        '@layouts': '/src/layouts'
      }
    }
  }
});
