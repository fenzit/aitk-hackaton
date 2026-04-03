<template>
  <section id="features" class="py-24 px-6 bg-bunker-50 dark:bg-black-950 border-y border-bunker-200 dark:border-black-800">
    <div class="max-w-6xl mx-auto">
      <div class="text-center max-w-2xl mx-auto mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-bunker-900 dark:text-black-50 mb-4">{{ t('f_title') }}</h2>
        <p class="text-bunker-600 dark:text-black-300 text-lg">{{ t('f_desc') }}</p>
      </div>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="feature in features" :key="feature.title" class="bg-white dark:bg-black-950 border border-bunker-200 dark:border-black-800 p-8 rounded-xl flex flex-col">
          <div class="w-12 h-12 bg-primary-50 dark:bg-primary-950/30 rounded-lg flex items-center justify-center mb-6">
            <component :is="feature.icon" class="w-6 h-6 text-primary-600 dark:text-primary-400" />
          </div>
          <h3 class="text-xl font-bold text-bunker-900 dark:text-black-50 mb-3">{{ feature.title }}</h3>
          <p class="text-bunker-600 dark:text-black-300 leading-relaxed mb-6 flex-grow">{{ feature.description }}</p>
          <div class="mt-auto overflow-hidden rounded-xl bg-bunker-50 dark:bg-black-900 border border-bunker-100 dark:border-black-800 h-40">
            <img :src="feature.image" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500" alt="Feature Image" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, defineComponent, h } from 'vue';
import { useTranslation } from '~/composables/useTranslation';

const { t } = useTranslation();

const SparklesIcon = defineComponent({
  render() {
    return h('svg', { fill: 'none', viewBox: '0 0 24 24', strokeWidth: 2, stroke: 'currentColor' }, [
      h('path', { strokeLinecap: 'round', strokeLinejoin: 'round', d: 'M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456ZM16.894 20.567 16.5 21.75l-.394-1.183a2.25 2.25 0 0 0-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 0 0 1.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 0 0 1.423 1.423l1.183.394-1.183.394a2.25 2.25 0 0 0-1.423 1.423Z' })
    ]);
  }
});

const CodeIcon = defineComponent({
  render() {
    return h('svg', { fill: 'none', viewBox: '0 0 24 24', strokeWidth: 2, stroke: 'currentColor' }, [
      h('path', { strokeLinecap: 'round', strokeLinejoin: 'round', d: 'M17.25 6.75 22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3-4.5 16.5' })
    ]);
  }
});

const GlobeIcon = defineComponent({
  render() {
    return h('svg', { fill: 'none', viewBox: '0 0 24 24', strokeWidth: 2, stroke: 'currentColor' }, [
      h('path', { strokeLinecap: 'round', strokeLinejoin: 'round', d: 'M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418' })
    ]);
  }
});

const PuzzleIcon = defineComponent({
  render() {
    return h('svg', { fill: 'none', viewBox: '0 0 24 24', strokeWidth: 2, stroke: 'currentColor' }, [
      h('path', { strokeLinecap: 'round', strokeLinejoin: 'round', d: 'M14.25 6.087c0-.355.186-.676.401-.959.221-.29.349-.634.349-1.003 0-1.036-.86-1.875-1.915-1.875s-1.915.839-1.915 1.875c0 .369.128.713.349 1.003.215.283.401.604.401.959v0a1.5 1.5 0 0 1-1.5 1.5H6a1.5 1.5 0 0 0-1.5 1.5v2.625c0 .241.05.474.141.688.197.464.309.972.309 1.5 0 .528-.112 1.036-.309 1.5-.091.214-.141.447-.141.688v2.625A1.5 1.5 0 0 0 6 18.75h2.625c.241 0 .474-.05.688-.141.464-.197.972-.309 1.5-.309.528 0 1.036.112 1.5.309.214.091.447.141.688.141H15.75c1.036 0 1.875-.84 1.875-1.875v-3.75c0-.828.672-1.5 1.5-1.5h1.5a1.5 1.5 0 0 0 1.5-1.5v-3.75a1.5 1.5 0 0 0-1.5-1.5h-1.5c-.828 0-1.5-.672-1.5-1.5V6.087Z' })
    ]);
  }
});

const features = computed(() => [
  {
    title: t('f_1_t'),
    description: t('f_1_d'),
    icon: SparklesIcon,
    image: 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=800&q=80'
  },
  {
    title: t('f_2_t'),
    description: t('f_2_d'),
    icon: CodeIcon,
    image: 'https://images.unsplash.com/photo-1541888087525-0746830cb1ea?auto=format&fit=crop&w=800&q=80'
  },
  {
    title: t('f_3_t'),
    description: t('f_3_d'),
    icon: GlobeIcon,
    image: 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80'
  },
  {
    title: t('f_4_t'),
    description: t('f_4_d'),
    icon: PuzzleIcon,
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80'
  }
]);
</script>
