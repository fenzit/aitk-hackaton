<template>
  <div class="flex h-screen bg-slate-50 dark:bg-black-950 text-slate-900 dark:text-black-50 font-sans overflow-hidden">
    <!-- Mobile Sidebar Backdrop -->
    <div v-if="isMobileMenuOpen" class="fixed inset-0 bg-slate-900/50 z-40 lg:hidden backdrop-blur-sm transition-opacity" @click="isMobileMenuOpen = false"></div>

    <!-- Sidebar -->
    <aside :class="['fixed inset-y-0 left-0 bg-white dark:bg-black-950 border-r border-slate-200 dark:border-black-800 flex-col z-50 w-64 lg:static lg:w-64 transition-transform duration-300 transform flex-shrink-0', isMobileMenuOpen ? 'translate-x-0 flex' : '-translate-x-full lg:translate-x-0 hidden lg:flex']">
      <div class="h-20 flex items-center justify-between px-6 border-b border-slate-200 dark:border-black-800 shrink-0">
        <div class="flex items-center">
          <div class="h-12 w-12 rounded-full bg-white dark:bg-black-950 shadow-sm border border-slate-200 dark:border-black-800 overflow-hidden shrink-0 flex items-center justify-center p-0.5">
            <img src="/logo.png" alt="CityMind Logo" class="h-full w-full object-cover rounded-full" />
          </div>
          <span class="ml-3 font-black text-slate-800 dark:text-black-100 tracking-tight text-xl">CityMind</span>
        </div>
        <button class="lg:hidden text-slate-400 dark:text-black-500 hover:bg-slate-100 dark:bg-black-900 p-1.5 rounded-lg -mr-2" @click="isMobileMenuOpen = false">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <nav class="flex-1 overflow-y-auto py-4 px-3 space-y-1">
        <NuxtLink to="/" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-slate-600 dark:text-black-300 hover:bg-slate-50 dark:bg-black-950 hover:text-slate-900 dark:text-black-50 transition-colors">
          <svg class="w-5 h-5 text-slate-400 dark:text-black-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" /></svg>
          <span class="block">Дашборд</span>
        </NuxtLink>
        <div class="pt-4 mt-4 border-t border-slate-100 dark:border-black-900"></div>
        <a href="#" class="w-full flex items-center justify-start gap-3 px-3 py-2.5 rounded-xl text-sm font-bold transition-all shadow-sm bg-gradient-to-r from-killarney-500 to-killarney-600 text-white shadow-killarney-500/20">
          <span class="text-lg">✨</span>
          <span class="block">Режим симуляции</span>
        </a>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 overflow-y-auto p-5 sm:p-8 lg:p-12 max-w-5xl mx-auto w-full relative flex flex-col">
      <!-- Mobile View Burger -->
      <div class="lg:hidden flex items-center gap-3 mb-6 bg-white dark:bg-black-950 p-3 rounded-xl shadow-sm border border-slate-200 dark:border-black-800">
        <button class="p-2 -ml-1 text-slate-500 dark:text-black-400 hover:bg-slate-100 dark:bg-black-900 rounded-lg" @click="isMobileMenuOpen = true">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
        </button>
        <span class="font-black text-slate-800 dark:text-black-100">Меню</span>
      </div>
      
      <div class="mb-10">
        <h1 class="text-4xl font-black text-slate-900 dark:text-black-50 flex items-center gap-4 tracking-tight">
          <span class="text-5xl text-killarney-500">✨</span>
          Система Моделирования Города
        </h1>
        <p class="text-slate-500 dark:text-black-400 mt-2 font-medium text-lg">Тестируйте сценарии "что-если" для оценки влияния на трафик и экологию.</p>
      </div>

      <!-- Scenarios Selector -->
      <div class="bg-white dark:bg-black-950 p-8 rounded-2xl border-l-[6px] border-l-killarney-500 shadow-xl shadow-slate-200/50">
        <h2 class="text-2xl font-bold text-slate-800 dark:text-black-100 mb-6 flex items-center justify-between">
          <span>Выберите сценарий</span>
          <span class="text-sm font-semibold bg-killarney-100 text-killarney-700 px-3 py-1 rounded-full">AI Анализ</span>
        </h2>
        
        <div class="space-y-4 mb-8">
          <label class="flex items-center gap-4 p-4 border border-slate-200 dark:border-black-800 rounded-xl cursor-pointer hover:bg-slate-50 dark:bg-black-950 transition-colors" :class="{'bg-slate-50 dark:bg-black-950 border-killarney-300 shadow-sm': scenarioOptions.closeRoad}">
            <input type="checkbox" v-model="scenarioOptions.closeRoad" class="w-5 h-5 accent-killarney-600 text-killarney-600 rounded bg-slate-100 dark:bg-black-900 border-slate-300 focus:ring-killarney-500">
            <div>
              <span class="block font-bold text-slate-800 dark:text-black-100 text-lg">Перекрыть дорогу (Абая пр-т)</span>
              <span class="block text-slate-500 dark:text-black-400 text-sm font-medium">Симуляция перекрытия главной артерии для проверки альтернативных маршрутов.</span>
            </div>
          </label>
          
          <label class="flex items-center gap-4 p-4 border border-slate-200 dark:border-black-800 rounded-xl cursor-pointer hover:bg-slate-50 dark:bg-black-950 transition-colors" :class="{'bg-slate-50 dark:bg-black-950 border-killarney-300 shadow-sm': scenarioOptions.increaseTransport}">
            <input type="checkbox" v-model="scenarioOptions.increaseTransport" class="w-5 h-5 accent-killarney-600 text-killarney-600 rounded bg-slate-100 dark:bg-black-900 border-slate-300 focus:ring-killarney-500">
            <div>
              <span class="block font-bold text-slate-800 dark:text-black-100 text-lg">Увеличить общественный транспорт</span>
              <span class="block text-slate-500 dark:text-black-400 text-sm font-medium">Добавить 50+ электробусов на ключевые маршруты.</span>
            </div>
          </label>
          
          <label class="flex items-center gap-4 p-4 border border-slate-200 dark:border-black-800 rounded-xl cursor-pointer hover:bg-slate-50 dark:bg-black-950 transition-colors" :class="{'bg-slate-50 dark:bg-black-950 border-killarney-300 shadow-sm': scenarioOptions.restrictCars}">
            <input type="checkbox" v-model="scenarioOptions.restrictCars" class="w-5 h-5 accent-killarney-600 text-killarney-600 rounded bg-slate-100 dark:bg-black-900 border-slate-300 focus:ring-killarney-500">
            <div>
              <span class="block font-bold text-slate-800 dark:text-black-100 text-lg">Ограничить машины в Центре</span>
              <span class="block text-slate-500 dark:text-black-400 text-sm font-medium">Ввести зону с низким уровнем выбросов.</span>
            </div>
          </label>
        </div>

        <button @click="runSimulation" :disabled="isRunning" class="w-full relative overflow-hidden group py-4 px-6 bg-killarney-600 hover:bg-killarney-700 text-white text-lg font-black rounded-xl shadow-2xl transition-all disabled:opacity-70">
          <span class="relative z-10 flex items-center justify-center gap-2">
            <svg v-if="isRunning" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span v-else>▶</span>
            {{ isRunning ? 'Вычисление влияния...' : 'Запустить Симуляцию' }}
          </span>
          <div class="absolute inset-0 bg-gradient-to-r from-killarney-500 to-killarney-700 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
        </button>
      </div>

      <!-- Results Simulation -->
      <transition name="fade">
        <div v-if="hasRun" class="mt-8 space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-killarney-50 dark:bg-killarney-950/30 p-6 rounded-2xl border-2 border-killarney-100 flex flex-col items-center justify-center py-10 shadow-sm transition-all transform hover:-translate-y-1">
              <span class="text-killarney-400 font-bold uppercase tracking-widest text-sm mb-2">Ожидаемый трафик</span>
              <div class="text-5xl font-black text-killarney-700 flex items-center gap-2">
                <span>↓ 25%</span>
              </div>
            </div>
            
            <div class="bg-emerald-50 dark:bg-emerald-950/30 p-6 rounded-2xl border-2 border-emerald-100 flex flex-col items-center justify-center py-10 shadow-sm transition-all transform hover:-translate-y-1">
              <span class="text-emerald-500 font-bold uppercase tracking-widest text-sm mb-2">Снижение загрязнения</span>
              <div class="text-5xl font-black text-emerald-600 flex items-center gap-2">
                <span>↓ 18%</span>
              </div>
            </div>
          </div>

          <div class="bg-amber-50 p-8 rounded-2xl border-2 border-amber-200 relative overflow-hidden shadow-sm">
            <div class="absolute -right-10 -top-10 text-9xl opacity-10">🤖</div>
            <h3 class="text-amber-800 font-bold text-lg mb-2 flex items-center gap-2">
              <span class="text-2xl">💡</span> ИИ Рекомендация
            </h3>
            <p class="text-2xl font-black text-amber-900 leading-tight">
              Лучшее действие → <span class="bg-amber-200 px-3 py-1 rounded inline-block mt-2 sm:mt-0 shadow-sm text-amber-950">Увеличить общ. транспорт</span>
            </p>
            <p class="text-amber-700 mt-4 font-medium max-w-2xl">
              Этот подход обеспечивает наиболее сбалансированное влияние на движение в городе, избегая недовольства от закрытия дорог.
            </p>
          </div>
        </div>
      </transition>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)

const scenarioOptions = ref({
  closeRoad: false,
  increaseTransport: true,
  restrictCars: false
})

const isRunning = ref(false)
const hasRun = ref(false)

const runSimulation = () => {
  if (isRunning.value) return
  
  hasRun.value = false
  isRunning.value = true
  
  setTimeout(() => {
    isRunning.value = false
    hasRun.value = true
  }, 1800)
}

useHead({
  title: 'Simulation | CityMind AI'
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
