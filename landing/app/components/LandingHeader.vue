<template>
  <header class="border-b border-bunker-200 bg-white">
    <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <div class="w-6 h-6 bg-primary-600 rounded-sm"></div>
        <span class="font-bold text-lg tracking-tight">Neutron AI</span>
      </div>
      <nav class="hidden md:flex gap-6 text-sm font-medium text-bunker-600">
        <a href="#features" class="hover:text-bunker-900">{{ t('n_features') }}</a>
        <a href="#how-it-works" class="hover:text-bunker-900">{{ t('n_how') }}</a>
        <a href="#use-cases" class="hover:text-bunker-900">{{ t('n_use') }}</a>
      </nav>
      <div class="flex items-center gap-4">
        <!-- Translation Toggle -->
        <button @click="toggleLocale" class="text-xs font-bold text-bunker-600 hover:text-bunker-900 border border-bunker-200 hover:bg-bunker-50 rounded px-2 py-1 transition-none uppercase">
          {{ locale === 'en' ? 'RU' : 'EN' }}
        </button>
        <a href="#" class="text-sm font-medium text-bunker-600 hover:text-bunker-900 hidden sm:block">{{ t('n_signin') }}</a>
        <a href="#" class="bg-primary-600 text-white px-4 py-2 rounded-xl text-sm font-medium hover:bg-primary-700 transition-none">{{ t('n_get_started') }}</a>
      </div>
    </div>
  </header>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';

const { t, locale, toggleLocale } = useTranslation();
</script>
