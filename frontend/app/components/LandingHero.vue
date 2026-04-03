<template>
  <section ref="heroRef" class="py-20 md:py-32 px-6 max-w-6xl mx-auto text-center">
    <div class="max-w-3xl mx-auto">
      <h1 class="hero-anim text-5xl md:text-6xl font-extrabold tracking-tight text-bunker-900 leading-[1.1] mb-6" v-html="t('h_title')">
      </h1>
      <p class="hero-anim text-lg md:text-xl text-bunker-600 mb-10 max-w-2xl mx-auto leading-relaxed">
        {{ t('h_desc') }}
      </p>
      <div class="hero-anim flex flex-col sm:flex-row justify-center items-center gap-4">
        <a href="#" class="w-full sm:w-auto bg-primary-600 text-white px-8 py-3.5 rounded-xl font-medium hover:bg-primary-700 text-lg transition-none">
          {{ t('h_start') }}
        </a>
        <a href="#" class="w-full sm:w-auto bg-bunker-50 border border-bunker-200 text-bunker-900 px-8 py-3.5 rounded-xl font-medium hover:bg-slate-100 text-lg transition-none">
          {{ t('h_docs') }}
        </a>
      </div>
      <div class="hero-anim mt-12 text-sm text-bunker-500 font-medium">
        {{ t('h_sub') }}
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

const { t } = useTranslation();
const heroRef = ref(null);
let ctx;

onMounted(() => {
  ctx = gsap.context(() => {
    // Top-to-bottom simple fade-in (opacity 0 -> 1 without translation)
    gsap.from('.hero-anim', {
      opacity: 0,
      duration: 1,
      stagger: 0.2, // Small delay sequentially starting from top to bottom
      delay: 0.3, // Slightly delayed so header has time to animate
      ease: 'power1.out'
    });
  }, heroRef.value);
});

onUnmounted(() => {
  if (ctx) ctx.revert();
});
</script>
