import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

// Change this one variable when deploying different projects
const APP_FOLDER = 'react_app'   // or 'notes_app', 'dashboard_app', etc.

export default defineConfig({
  base: '/apps/react/',
  build: {
    outDir: resolve(__dirname, `../${APP_FOLDER}/build`),
    emptyOutDir: true,
    assetsDir: 'assets'
  },
  plugins: [react()],
})
