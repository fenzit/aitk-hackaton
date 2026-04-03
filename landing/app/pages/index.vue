<template>
  <div class="min-h-screen bg-slate-50 text-slate-900 font-sans">
    <!-- Header -->
    <header class="bg-white border-b border-slate-200 px-6 py-3 flex items-center justify-between sticky top-0 z-50">
      <div class="flex items-center gap-6">
        <!-- Logo / Name -->
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-indigo-600 text-white rounded-md flex items-center justify-center font-bold text-lg shadow-sm">
            C
          </div>
          <h1 class="text-lg font-bold tracking-tight text-slate-800 leading-none">CityMind AI</h1>
        </div>
        
        <!-- Status & Time indicator -->
        <div class="flex items-center gap-4 border-l border-slate-200 pl-6">
          <button @click="toggleStatus" class="flex items-center gap-2 group focus:outline-none">
            <span class="relative flex h-2.5 w-2.5">
              <span v-if="isLive" class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span :class="['relative inline-flex rounded-full h-2.5 w-2.5', isLive ? 'bg-emerald-500' : 'bg-rose-500']"></span>
            </span>
            <span class="text-sm font-medium text-slate-600 group-hover:text-slate-900 transition-colors">
              {{ isLive ? 'Live' : 'Critical' }}
            </span>
          </button>
          
          <span class="text-sm text-slate-400 font-medium font-mono">{{ currentTime }}</span>
        </div>
      </div>
      
      <!-- Buttons -->
      <div class="flex items-center gap-3">
        <button class="px-3 py-1.5 text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors flex items-center gap-2 border border-slate-200 shadow-sm bg-white">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh Data
        </button>
        <button @click="toggleSimulation" :class="['px-3 py-1.5 text-sm font-medium rounded-lg transition-colors flex items-center gap-2 border shadow-sm', isSimulation ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-600 hover:text-slate-900 hover:bg-slate-100']">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
          </svg>
          {{ isSimulation ? 'Simulation Mode ON' : 'Toggle Simulation' }}
        </button>
      </div>
    </header>

    <main class="p-6 max-w-[1600px] mx-auto space-y-6">
      <!-- KPI Cards (4 blocks in one row) -->
      <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="(kpi, index) in kpis" :key="index" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm transition-shadow hover:shadow-md">
          <div class="flex items-start justify-between mb-4">
            <h3 class="text-sm font-medium text-slate-500">{{ kpi.title }}</h3>
            <div :class="`p-2 rounded-lg ${kpi.colorClass}`">
              <component :is="kpi.icon" class="w-5 h-5" />
            </div>
          </div>
          <div class="flex items-baseline gap-2">
            <p class="text-2xl font-bold text-slate-800">{{ kpi.value }}</p>
            <span :class="`text-xs font-semibold ${kpi.trend > 0 ? 'text-emerald-500' : 'text-rose-500'}`">
              {{ kpi.trend > 0 ? '+' : '' }}{{ kpi.trend }}%
            </span>
          </div>
        </div>
      </section>

      <!-- Map (70%) and AI Insight Panel (30%) -->
      <section class="grid grid-cols-1 lg:grid-cols-12 gap-6 h-[500px]">
        <!-- Map Panel -->
        <div class="lg:col-span-8 bg-slate-100 rounded-xl border border-slate-200 overflow-hidden relative shadow-sm h-full group">
          <!-- Mock Map Background -->
          <div class="absolute inset-0 bg-[url('https://api.mapbox.com/styles/v1/mapbox/dark-v11/static/-74.006,40.7128,12,0,0/1200x800?access_token=pk.eyJ1IjoiZXhhbXBsZSIsImEiOiJjazAifQ.example')] bg-cover bg-center opacity-80 mix-blend-luminosity"></div>
          
          <!-- Map Overlay Gradients -->
          <div class="absolute inset-x-0 top-0 h-24 bg-gradient-to-b from-white w-full opacity-60"></div>
          
          <div class="absolute top-4 left-4 right-4 flex justify-between items-start z-10">
            <div class="bg-white/90 backdrop-blur-sm px-4 py-2 rounded-lg border border-slate-200 shadow-sm">
              <h2 class="font-semibold text-slate-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
                </svg>
                Live Traffic & Infrastructure Map
              </h2>
            </div>
            
            <div class="flex gap-2">
              <button class="bg-white/90 backdrop-blur-sm p-2 rounded-lg border border-slate-200 shadow-sm hover:bg-white text-slate-600 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h6a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" /></svg>
              </button>
            </div>
          </div>
          
          <!-- Map Interactivity Mock -->
          <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <div class="relative flex justify-center items-center">
              <div class="absolute w-24 h-24 bg-indigo-500/20 rounded-full animate-ping"></div>
              <div class="relative w-4 h-4 bg-indigo-600 rounded-full border-2 border-white shadow-lg"></div>
            </div>
          </div>
        </div>

        <!-- AI Insight Panel -->
        <div class="lg:col-span-4 bg-white rounded-xl border border-slate-200 shadow-sm flex flex-col h-full overflow-hidden">
          <div class="p-4 border-b border-slate-100 flex items-center justify-between bg-slate-50">
            <h2 class="font-semibold text-slate-800 flex items-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-indigo-500" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
              </svg>
              AI Insights
            </h2>
            <span class="text-xs font-medium px-2 py-1 bg-indigo-50 text-indigo-600 rounded text-center">Auto-updating</span>
          </div>
          
          <div class="flex-1 overflow-y-auto p-4 space-y-4">
            <div v-for="(insight, index) in insights" :key="index" class="p-4 rounded-lg border border-slate-100 hover:border-indigo-100 hover:bg-slate-50 transition-colors group">
              <div class="flex items-center gap-2 mb-2">
                <span :class="`w-2 h-2 rounded-full ${insight.urgency === 'high' ? 'bg-rose-500' : (insight.urgency === 'medium' ? 'bg-amber-500' : 'bg-blue-500')}`"></span>
                <span class="text-xs font-medium text-slate-500 uppercase tracking-wider">{{ insight.time }}</span>
              </div>
              <p class="text-sm text-slate-700 leading-relaxed font-medium">
                {{ insight.text }}
              </p>
              <div class="mt-3 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button class="text-xs text-indigo-600 font-medium hover:text-indigo-800">Resolve</button>
                <button class="text-xs text-slate-500 font-medium hover:text-slate-700">Dismiss</button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Charts (2 graphs side by side) -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Chart 1: Energy Usage -->
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-semibold text-slate-800">Energy Consumption Grid</h3>
            <select class="text-sm border border-slate-200 rounded-lg px-2 py-1 text-slate-600 bg-white">
              <option>Last 24 Hours</option>
              <option>Last 7 Days</option>
            </select>
          </div>
          <!-- Mock Chart Container -->
          <div class="h-64 flex items-end gap-2 px-2 relative">
            <!-- Grid lines -->
            <div class="absolute inset-0 flex flex-col justify-between pointer-events-none">
              <div v-for="i in 5" :key="i" class="w-full border-t border-slate-100 h-0"></div>
            </div>
            <!-- Bars -->
            <div v-for="(val, i) in chart1Data" :key="i" class="w-full relative group">
              <div 
                class="absolute bottom-0 w-[80%] mx-auto left-0 right-0 bg-indigo-500 rounded-t shadow-sm transition-all duration-500 group-hover:bg-indigo-600"
                :style="`height: ${val}%`"
              ></div>
            </div>
          </div>
          <div class="flex justify-between text-xs text-slate-400 mt-3 px-2">
            <span>00:00</span>
            <span>06:00</span>
            <span>12:00</span>
            <span>18:00</span>
            <span>24:00</span>
          </div>
        </div>

        <!-- Chart 2: Traffic Flow -->
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-semibold text-slate-800">Traffic Flow Efficiency</h3>
             <div class="flex gap-2">
                <span class="flex items-center gap-1 text-xs text-slate-500"><span class="w-3 h-3 rounded bg-emerald-400"></span> Current</span>
                <span class="flex items-center gap-1 text-xs text-slate-500"><span class="w-3 h-3 rounded bg-slate-200"></span> Expected</span>
             </div>
          </div>
          <!-- Mock Line Chart Container -->
          <div class="h-64 relative overflow-hidden flex items-center justify-center">
             <!-- Simulated Line Chart SVG -->
             <svg viewBox="0 0 400 150" class="w-full h-full preserve-3d" preserveAspectRatio="none">
               <path d="M0,130 C40,110 80,140 120,90 C160,40 200,80 240,60 C280,40 320,100 360,70 L400,60" fill="none" class="stroke-slate-200" stroke-width="2" stroke-dasharray="4 4" />
               <path d="M0,140 C40,120 80,120 120,70 C160,20 200,60 240,40 C280,20 320,80 360,50 L400,40" fill="none" class="stroke-emerald-500" stroke-width="3" />
               <path d="M0,150 L0,140 C40,120 80,120 120,70 C160,20 200,60 240,40 C280,20 320,80 360,50 L400,40 L400,150 Z" fill="url(#gradient)" opacity="0.2" />
               <defs>
                  <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#10b981" />
                    <stop offset="100%" stop-color="white" stop-opacity="0" />
                  </linearGradient>
               </defs>
             </svg>
          </div>
          <div class="flex justify-between text-xs text-slate-400 mt-3">
             <span>Mon</span>
             <span>Tue</span>
             <span>Wed</span>
             <span>Thu</span>
             <span>Fri</span>
             <span>Sat</span>
             <span>Sun</span>
          </div>
        </div>
      </section>

      <!-- Simulation Panel (full width) -->
      <section class="bg-indigo-900 border border-indigo-800 rounded-xl overflow-hidden shadow-lg relative text-white">
        <!-- Cool Background Effect -->
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"></div>
        <div class="absolute top-0 right-0 -mr-20 -mt-20 w-64 h-64 bg-indigo-500 rounded-full blur-3xl opacity-30"></div>
        
        <div class="relative z-10 p-6">
          <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-8 border-b border-indigo-800/50 pb-6">
            <div>
              <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                </svg>
                Traffic Routing Simulation Engine
              </h2>
              <p class="text-indigo-300 text-sm">Run 'what-if' scenarios to predict gridlock and redirect traffic patterns.</p>
            </div>
            <button class="bg-indigo-500 hover:bg-indigo-400 text-white px-6 py-2.5 rounded-lg font-medium transition-colors shadow-sm flex items-center gap-2 shadow-indigo-500/20">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
              </svg>
              Run Simulation
            </button>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Parameter 1 -->
            <div class="bg-indigo-950/50 p-5 rounded-xl border border-indigo-800/80">
              <label class="block text-sm font-medium text-indigo-300 mb-3">Weather Condition Impact</label>
              <div class="space-y-4">
                <input type="range" min="0" max="100" value="75" class="w-full accent-indigo-500">
                <div class="flex justify-between text-xs text-indigo-400">
                  <span>Clear</span>
                  <span>Heavy Storm</span>
                </div>
              </div>
            </div>
            
            <!-- Parameter 2 -->
            <div class="bg-indigo-950/50 p-5 rounded-xl border border-indigo-800/80">
              <label class="block text-sm font-medium text-indigo-300 mb-3">Major Event Density</label>
              <div class="space-y-4">
                <input type="range" min="0" max="100" value="40" class="w-full accent-emerald-500">
                <div class="flex justify-between text-xs text-indigo-400">
                  <span>Normal</span>
                  <span>Concert / Game Day</span>
                </div>
              </div>
            </div>

            <!-- Parameter 3 -->
            <div class="bg-indigo-950/50 p-5 rounded-xl border border-indigo-800/80">
              <label class="block text-sm font-medium text-indigo-300 mb-3">Emergency Response Priority</label>
              <div class="flex items-center gap-4">
                <label class="flex items-center gap-2 cursor-pointer">
                   <input type="radio" name="priority" class="text-indigo-500 focus:ring-indigo-500 bg-indigo-900 border-indigo-700">
                   <span class="text-sm text-indigo-200">Standard</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                   <input type="radio" name="priority" checked class="text-indigo-500 focus:ring-indigo-500 bg-indigo-900 border-indigo-700">
                   <span class="text-sm text-indigo-200">High Evacuation</span>
                </label>
              </div>
              <div class="mt-4 pt-4 border-t border-indigo-800/50">
                <p class="text-xs text-indigo-400">Estimated processing time: <span class="font-mono text-emerald-400">1.2s</span></p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isLive = ref(true)
const isSimulation = ref(false)
const currentTime = ref('')

let timer
onMounted(() => {
  const updateTime = () => {
    currentTime.value = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }
  updateTime()
  timer = setInterval(updateTime, 1000)
})

onUnmounted(() => {
  clearInterval(timer)
})

const toggleStatus = () => {
  isLive.value = !isLive.value
}

const toggleSimulation = () => {
  isSimulation.value = !isSimulation.value
}

useHead({
  title: 'CityMind AI - Intelligent City Control Dashboard',
  meta: [
    { name: 'description', content: 'CityMind AI operations and simulation control panel.' }
  ],
  bodyAttrs: {
    class: 'bg-slate-50'
  }
})

// Mock icons mapped to heroicons or similar intuitive SVG structures
const ActivityIcon = {
  template: `<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>`
}
const UsersIcon = {
  template: `<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" /></svg>`
}
const ChartIcon = {
  template: `<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M8 13v-1m4 1v-3m4 3V8M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" /></svg>`
}
const ServerIcon = {
  template: `<svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" /></svg>`
}

const kpis = ref([
  { title: 'Total Active Sensors', value: '42,891', trend: 2.4, icon: ActivityIcon, colorClass: 'bg-indigo-100 text-indigo-600' },
  { title: 'Traffic Flow Rate', value: '840 v/h', trend: -1.2, icon: UsersIcon, colorClass: 'bg-emerald-100 text-emerald-600' },
  { title: 'Grid Efficiency', value: '98.5%', trend: 0.5, icon: ChartIcon, colorClass: 'bg-blue-100 text-blue-600' },
  { title: 'Server Load', value: '42%', trend: 4.1, icon: ServerIcon, colorClass: 'bg-purple-100 text-purple-600' },
])

const insights = ref([
  { time: '2 mins ago', text: 'Congestion detected on I-95 Northbound. Adjusting traffic light patterns.', urgency: 'medium' },
  { time: '14 mins ago', text: 'Power grid spike predicted in Downtown sector due to incoming storm front.', urgency: 'high' },
  { time: '1 hr ago', text: 'Subway line A operating at 110% capacity. Deployment recommended.', urgency: 'medium' },
  { time: '2 hrs ago', text: 'Daily synchronization with state municipal database complete.', urgency: 'low' },
  { time: '3 hrs ago', text: 'Water pressure anomaly detected in Sector 4. Maintenance crew dispatched.', urgency: 'low' },
])

const chart1Data = ref([45, 60, 30, 85, 90, 70, 50, 65, 80, 40, 55, 75, 45, 60, 30, 85, 90, 70, 50, 65, 80, 40, 55, 75])
</script>

<style scoped>
/* Optional grid background or subtle styling */
</style>