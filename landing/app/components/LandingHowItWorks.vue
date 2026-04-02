<template>
  <section id="how-it-works" class="py-24 px-6 max-w-6xl mx-auto">
    <div class="mb-16">
      <h2 class="text-3xl font-bold tracking-tight text-bunker-900 mb-4">{{ t('hw_title') }}</h2>
      <p class="text-bunker-600 text-lg max-w-2xl">{{ t('hw_desc') }}</p>
    </div>

    <div class="grid md:grid-cols-3 gap-10">
      <div class="relative">
        <div class="text-6xl font-black text-bunker-100 absolute -top-8 -left-4 z-0">1</div>
        <div class="relative z-10">
          <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('hw_1_t') }}</h3>
          <p class="text-bunker-600 mb-6 leading-relaxed">{{ t('hw_1_d') }}</p>
          <div class="bg-bunker-900 rounded-xl p-6 text-sm text-bunker-300 font-mono overflow-x-auto">
            <pre><code>npm install @neutron/ai

import Neutron from "@neutron/ai";
const ai = new Neutron("sk_test_...");</code></pre>
          </div>
        </div>
      </div>
      
      <div class="relative">
        <div class="text-6xl font-black text-bunker-100 absolute -top-8 -left-4 z-0">2</div>
        <div class="relative z-10">
          <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('hw_2_t') }}</h3>
          <p class="text-bunker-600 mb-6 leading-relaxed">{{ t('hw_2_d') }}</p>
          <div class="bg-bunker-900 rounded-xl p-6 text-sm text-bunker-300 font-mono overflow-x-auto">
            <pre><code>const result = await ai.generate({
  task: "extract_features",
  text: userInput,
  schema: FeatureSchema
});</code></pre>
          </div>
        </div>
      </div>

      <div class="relative">
        <div class="text-6xl font-black text-bunker-100 absolute -top-8 -left-4 z-0">3</div>
        <div class="relative z-10">
          <h3 class="text-xl font-bold text-bunker-900 mb-3">{{ t('hw_3_t') }}</h3>
          <p class="text-bunker-600 mb-6 leading-relaxed">{{ t('hw_3_d') }}</p>
          <div class="bg-bunker-900 rounded-xl p-6 text-sm text-bunker-300 font-mono overflow-x-auto">
            <pre><code>✓ Types matching schema
✓ Tracing enabled
✓ Deployed globally
✓ Monitored 24/7</code></pre>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useTranslation } from '~/composables/useTranslation';

const { t } = useTranslation();
</script>
