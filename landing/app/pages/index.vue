<template>
  <div class="min-h-screen bg-white text-slate-900 font-sans selection:bg-primary-200 selection:text-primary-900">
    <LandingHeader />
    <main>
      <LandingHero />
      <LandingFeatures />
      <LandingHowItWorks />
      <LandingUseCases />
      <LandingCta />
    </main>
    <LandingFooter />
  </div>
</template>

<script setup>
useHead({
  title: 'Neutron AI - Ship AI features without the complexity',
  meta: [
    { name: 'description', content: 'The comprehensive API and toolkit to integrate, manage, and scale AI models in your applications.' }
  ]
})
</script>