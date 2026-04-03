import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  devtools: { enabled: true },
  css: ['./app/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  modules: [
    '@nuxt/a11y',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/image',
    '@nuxtjs/color-mode',
    '@vercel/analytics'
  ],
  colorMode: {
    classSuffix: ''
  },
  runtimeConfig: {
    apiUrl: process.env.NUXT_API_URL || 'http://localhost:8000', // только SSR
    public: {
      wsUrl: process.env.NUXT_PUBLIC_WS_URL || 'ws://localhost:8000/ws/city',
      apiUrl: process.env.NUXT_PUBLIC_API_URL || 'http://localhost:8000',
    }
  }
});
