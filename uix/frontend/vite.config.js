import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({ mode }) => {
  // Load env with a prefix; only variables starting with VITE_ will be loaded
  const env = loadEnv(mode, process.cwd(), 'VITE_')
  console.log('Loaded env variables:', env)
  const target = `${env.VITE_API_HOST}:${env.VITE_BACKEND_PORT}`
  console.log('Proxy target is:', target)

  const port = Number(env.VITE_FRONTEND_PORT) || 7173

  return {
    plugins: [react()],
    server: {
      port: port,
      proxy: {
        '/api': {
          target,
          changeOrigin: true,
          secure: false,
        },
      },
    },
  }
})
