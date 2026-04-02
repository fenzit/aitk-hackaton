<template>
  <section id="how-it-works" class="py-24 px-6 max-w-6xl mx-auto">
    <div class="mb-16">
      <h2 class="text-3xl font-bold tracking-tight text-slate-900 mb-4">How it works</h2>
      <p class="text-slate-600 text-lg max-w-2xl">Integrate AI into your application without learning prompt engineering, infrastructure scaling, or model management.</p>
    </div>

    <div class="grid md:grid-cols-3 gap-10">
      <div v-for="(step, index) in steps" :key="index" class="relative">
        <div class="text-6xl font-black text-slate-100 absolute -top-8 -left-4 z-0">{{ index + 1 }}</div>
        <div class="relative z-10">
          <h3 class="text-xl font-bold text-slate-900 mb-3">{{ step.title }}</h3>
          <p class="text-slate-600 mb-6 leading-relaxed">{{ step.description }}</p>
          <div class="bg-slate-900 rounded-xl p-6 text-sm text-slate-300 font-mono overflow-x-auto">
            <pre><code>{{ step.code }}</code></pre>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const steps = [
  {
    title: 'Initialize SDK',
    description: 'Install our lightweight client and initialize it with your project key. We handle the authentication safely.',
    code: 'npm install @neutron/ai\n\nimport Neutron from "@neutron/ai";\nconst ai = new Neutron("sk_test_...");'
  },
  {
    title: 'Call the API',
    description: 'Instead of complex prompts, just define what you want and your data schema. We return typed responses perfectly.',
    code: 'const result = await ai.generate({\n  task: "extract_features",\n  text: userInput,\n  schema: FeatureSchema\n});'
  },
  {
    title: 'Deploy to Edge',
    description: 'Everything runs on our globally distributed edge network, providing sub-second latency for your users everywhere.',
    code: '✓ Types matching schema\n✓ Tracing enabled\n✓ Deployed globally\n✓ Monitored 24/7'
  }
];
</script>
