<template>
  <section id="use-cases" class="py-20 px-6 max-w-6xl mx-auto border-t border-bunker-200 dark:border-black-800">
    <div class="text-center max-w-2xl mx-auto mb-16">
      <h2 class="text-3xl font-bold tracking-tight text-bunker-900 dark:text-black-50 mb-4">{{ t('uc_title') }}</h2>
      <p class="text-bunker-600 dark:text-black-300 text-lg">{{ t('uc_desc') }}</p>
    </div>

    <div class="grid md:grid-cols-3 gap-6">
      <div class="border border-bunker-200 dark:border-black-800 rounded-xl p-8 hover:border-bunker-300 dark:hover:border-black-700 flex flex-col">
        <div class="inline-block w-fit bg-bunker-100 dark:bg-black-900 text-bunker-800 dark:text-black-100 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_1_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 dark:text-black-50 mb-3">{{ t('uc_1_t') }}</h3>
        <p class="text-bunker-600 dark:text-black-300 leading-relaxed mb-6 flex-grow">{{ t('uc_1_d') }}</p>
        <div class="mt-auto overflow-hidden rounded-xl h-48 border border-bunker-100 dark:border-black-800">
           <img src="https://images.unsplash.com/photo-1575806495204-c15555d496a7?auto=format&fit=crop&w=800&q=80" alt="Use case 1" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"/>
        </div>
      </div>
      <div class="border border-bunker-200 dark:border-black-800 rounded-xl p-8 hover:border-bunker-300 dark:hover:border-black-700 flex flex-col">
        <div class="inline-block w-fit bg-bunker-100 dark:bg-black-900 text-bunker-800 dark:text-black-100 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_2_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 dark:text-black-50 mb-3">{{ t('uc_2_t') }}</h3>
        <p class="text-bunker-600 dark:text-black-300 leading-relaxed mb-6 flex-grow">{{ t('uc_2_d') }}</p>
        <div class="mt-auto overflow-hidden rounded-xl h-48 border border-bunker-100 dark:border-black-800">
           <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80" alt="Use case 2" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"/>
        </div>
      </div>
      <div class="border border-bunker-200 dark:border-black-800 rounded-xl p-8 hover:border-bunker-300 dark:hover:border-black-700 flex flex-col">
        <div class="inline-block w-fit bg-bunker-100 dark:bg-black-900 text-bunker-800 dark:text-black-100 font-medium px-3 py-1 rounded mb-6 text-sm">{{ t('uc_3_badge') }}</div>
        <h3 class="text-xl font-bold text-bunker-900 dark:text-black-50 mb-3">{{ t('uc_3_t') }}</h3>
        <p class="text-bunker-600 dark:text-black-300 leading-relaxed mb-6 flex-grow">{{ t('uc_3_d') }}</p>
        <div class="mt-auto overflow-hidden rounded-xl h-48 border border-bunker-100 dark:border-black-800">
           <img src="https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80" alt="Use case 3" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500"/>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';

const { t } = useTranslation();
</script>
