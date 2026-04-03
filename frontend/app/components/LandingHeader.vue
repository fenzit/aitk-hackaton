<template>
  <header ref="headerRef" class="border-b border-bunker-200 dark:border-black-800 bg-white dark:bg-black-950">
    <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
      <div class="flex items-center gap-2 header-anim">
        <div class="w-6 h-6 bg-primary-600 rounded-sm"></div>
        <span class="font-bold text-lg tracking-tight">Neutron AI</span>
      </div>
      <nav class="hidden md:flex gap-6 text-sm font-medium text-bunker-600 dark:text-black-300">
        <a href="#features" class="hover:text-bunker-900 dark:text-black-50 header-anim">{{ t('n_features') }}</a>
        <a href="#how-it-works" class="hover:text-bunker-900 dark:text-black-50 header-anim">{{ t('n_how') }}</a>
        <a href="#use-cases" class="hover:text-bunker-900 dark:text-black-50 header-anim">{{ t('n_use') }}</a>
      </nav>
      <div class="flex items-center gap-4">
        <!-- Theme Toggle -->
        <button @click="colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'" class="text-xs font-bold text-bunker-600 dark:text-black-300 hover:text-bunker-900 border border-bunker-200 dark:border-black-800 hover:bg-bunker-50 dark:bg-black-950 rounded px-2 py-1 transition-none header-anim flex items-center justify-center">
          <svg v-if="colorMode.value === 'dark'" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
        </button>
        <!-- Translation Toggle -->
        <button @click="toggleLocale" class="text-xs font-bold text-bunker-600 dark:text-black-300 hover:text-bunker-900 dark:text-black-50 border border-bunker-200 dark:border-black-800 hover:bg-bunker-50 dark:bg-black-950 rounded px-2 py-1 transition-none uppercase header-anim">
          {{ locale === 'en' ? 'RU' : 'EN' }}
        </button>
        <a href="#" class="text-sm font-medium text-bunker-600 dark:text-black-300 hover:text-bunker-900 dark:text-black-50 hidden sm:block header-anim">{{ t('n_signin') }}</a>
        <a href="#" class="bg-primary-600 text-white px-4 py-2 rounded-xl text-sm font-medium hover:bg-primary-700 transition-none header-anim">{{ t('n_get_started') }}</a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

const { t, locale, toggleLocale } = useTranslation();
const colorMode = useColorMode();
const headerRef = ref(null);
let ctx;

onMounted(() => {
  ctx = gsap.context(() => {
    gsap.from('.header-anim', {
      opacity: 0,
      duration: 0.8,
      stagger: 0.1,
      ease: 'power2.out'
    });
  }, headerRef.value);
});

onUnmounted(() => {
  if (ctx) ctx.revert();
});
</script>
