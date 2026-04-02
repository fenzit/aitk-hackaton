export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  // Это отключит проблемный движок
  css: [],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  modules: [
    '@nuxt/image',
    '@nuxt/fonts',
    '@nuxt/eslint',
    '@nuxt/a11y'
  ]
})