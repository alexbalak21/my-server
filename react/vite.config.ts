import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  base: '/apps/react/',        // URL where Flask serves the app
  build: {
    outDir: resolve(__dirname, '../react_app/build'),  // absolute path to build folder
    emptyOutDir: true,          // clean the folder before building
    assetsDir: 'assets'         // keep assets inside /build/assets
  },
  plugins: [react()],
})
