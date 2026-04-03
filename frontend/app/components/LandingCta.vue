<template>
  <section class="py-24 px-6 max-w-6xl mx-auto">
    <div class="bg-bunker-950 rounded-3xl p-10 md:p-20 text-center">
      <h2 class="text-4xl md:text-5xl font-extrabold tracking-tight text-white mb-6">
        {{ t('c_title') }}
      </h2>
      <p class="text-xl text-bunker-300 mb-10 max-w-2xl mx-auto">
        {{ t('c_desc') }}
      </p>
      <div class="flex flex-col sm:flex-row justify-center gap-4">
        <a href="#" class="bg-primary-600 text-white px-8 py-4 rounded-xl font-medium hover:bg-primary-500 text-lg transition-none">
          {{ t('c_start') }}
        </a>
        <a href="#" class="bg-white/10 text-white px-8 py-4 rounded-xl font-medium hover:bg-white/20 text-lg transition-none border border-white/20">
          {{ t('c_demo') }}
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';

const { t } = useTranslation();
</script>
