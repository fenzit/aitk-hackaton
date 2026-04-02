<template>
  <section id="use-cases" class="py-20 px-6 max-w-6xl mx-auto border-t border-bunker-200">
    <div class="text-center max-w-2xl mx-auto mb-16">
      <h2 class="text-3xl font-bold tracking-tight text-bunker-900 mb-4">{{ t('uc_title') }}</h2>
      <p class="text-bunker-600 text-lg">{{ t('uc_desc') }}</p>
    </div>

    <div class="grid md:grid-cols-3 gap-6">
      <div class="border border-bunker-200 rounded-xl p-8 hover:border-bunker-300">
        <div class="inline-block bg-bunker-100 text-bunker-800 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_1_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('uc_1_t') }}</h3>
        <p class="text-bunker-600 leading-relaxed">{{ t('uc_1_d') }}</p>
      </div>
      <div class="border border-bunker-200 rounded-xl p-8 hover:border-bunker-300">
        <div class="inline-block bg-bunker-100 text-bunker-800 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_2_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('uc_2_t') }}</h3>
        <p class="text-bunker-600 leading-relaxed">{{ t('uc_2_d') }}</p>
      </div>
      <div class="border border-bunker-200 rounded-xl p-8 hover:border-bunker-300">
        <div class="inline-block bg-bunker-100 text-bunker-800 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_3_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('uc_3_t') }}</h3>
        <p class="text-bunker-600 leading-relaxed">{{ t('uc_3_d') }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';

const { t } = useTranslation();
</script>
