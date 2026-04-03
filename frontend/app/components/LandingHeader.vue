<template>
  <header ref="headerRef" class="border-b border-bunker-200 bg-white">
    <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
      <div class="flex items-center gap-2 header-anim">
        <div class="w-6 h-6 bg-primary-600 rounded-sm"></div>
        <span class="font-bold text-lg tracking-tight">Neutron AI</span>
      </div>
      <nav class="hidden md:flex gap-6 text-sm font-medium text-bunker-600">
        <a href="#features" class="hover:text-bunker-900 header-anim">{{ t('n_features') }}</a>
        <a href="#how-it-works" class="hover:text-bunker-900 header-anim">{{ t('n_how') }}</a>
        <a href="#use-cases" class="hover:text-bunker-900 header-anim">{{ t('n_use') }}</a>
      </nav>
      <div class="flex items-center gap-4">
        <!-- Translation Toggle -->
        <button @click="toggleLocale" class="text-xs font-bold text-bunker-600 hover:text-bunker-900 border border-bunker-200 hover:bg-bunker-50 rounded px-2 py-1 transition-none uppercase header-anim">
          {{ locale === 'en' ? 'RU' : 'EN' }}
        </button>
        <a href="#" class="text-sm font-medium text-bunker-600 hover:text-bunker-900 hidden sm:block header-anim">{{ t('n_signin') }}</a>
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
