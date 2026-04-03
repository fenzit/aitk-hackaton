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
          <span class="ml-3 font-black text-slate-800 dark:text-black-100 tracking-tight text-xl">CityMind AI</span>
        </div>
        <button class="lg:hidden text-slate-400 dark:text-black-500 hover:bg-slate-100 dark:bg-black-900 p-1.5 rounded-lg -mr-2" @click="isMobileMenuOpen = false">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <nav class="flex-1 overflow-y-auto py-4 px-3 space-y-1">
        <a href="#" @click.prevent="currentTab = 'dashboard'" :class="['flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors', currentTab === 'dashboard' ? 'text-killarney-700 bg-killarney-50 dark:bg-killarney-950/30' : 'text-slate-600 dark:text-black-300 hover:bg-slate-50 dark:bg-black-950 hover:text-slate-900 dark:text-black-50']">
          <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" /></svg>
          <span class="block">Главная</span>
        </a>

        <a href="#" @click.prevent="currentTab = 'ecology'" :class="['flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors', currentTab === 'ecology' ? 'text-killarney-700 bg-killarney-50 dark:bg-killarney-950/30' : 'text-slate-600 dark:text-black-300 hover:bg-slate-50 dark:bg-black-950 hover:text-slate-900 dark:text-black-50']">
          <svg class="w-5 h-5 flex-shrink-0" :class="currentTab === 'ecology' ? 'text-killarney-500' : 'text-slate-400 dark:text-black-500'" fill="currentColor" viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66l.95-2.3c.48.17.98.3 1.34.3C12 20 20 16 20 8h-3zm-1 9.73C14 16.63 11.28 15.65 9 15.5c2.32-.4 6.52-1.04 8 2.23z"/></svg>
          <span class="block">Экология</span>
        </a>
        <a href="#" @click.prevent="currentTab = 'analytics'" :class="['flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors', currentTab === 'analytics' ? 'text-killarney-700 bg-killarney-50 dark:bg-killarney-950/30' : 'text-slate-600 dark:text-black-300 hover:bg-slate-50 dark:bg-black-950 hover:text-slate-900 dark:text-black-50']">
          <svg class="w-5 h-5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="currentTab === 'analytics' ? 'text-killarney-500' : 'text-slate-400 dark:text-black-500'">
            <rect x="4" y="14" width="4" height="6" rx="1.5"/>
            <rect x="10" y="8" width="4" height="12" rx="1.5"/>
            <rect x="16" y="4" width="4" height="16" rx="1.5"/>
          </svg>
          <span class="block">Аналитика</span>
        </a>
        
        <div class="pt-4 mt-4 border-t border-slate-100 dark:border-black-900"></div>
        
      </nav>
    </aside>

    <!-- Main Wrapper -->
    <div class="flex-1 flex flex-col min-w-0 overflow-hidden relative">
      <!-- Top Bar -->
      <header class="bg-white dark:bg-black-950 border-b border-slate-200 dark:border-black-800 h-16 shrink-0 px-4 md:px-6 flex items-center justify-between z-10 w-full">
        <div class="flex items-center gap-4 md:gap-6">
          <div class="flex items-center gap-2">
            <h1 class="text-xl font-black tracking-tight text-slate-800 dark:text-black-100 leading-none lg:hidden hidden sm:block">CityMind AI</h1>
          </div>
          
          <div class="h-6 w-px bg-slate-200 hidden md:block"></div>
          
          <div class="hidden md:flex items-center gap-2 bg-slate-50 dark:bg-black-950 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-black-800 hover:border-killarney-300 transition-colors cursor-pointer group relative">
            <svg class="w-5 h-5 text-slate-500 dark:text-black-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <select 
              v-if="cityData" 
              v-model="selectedCity"
              class="bg-transparent border-none text-sm font-black text-slate-700 dark:text-black-200 outline-none cursor-pointer group-hover:text-killarney-600 appearance-none pr-6 relative z-10 w-fit uppercase tracking-tighter"
            >
              <option value="Алматы">Алматы</option>
              <option value="Астана">Астана</option>
              <option value="Шымкент">Шымкент</option>
            </select>
            

            <!-- Removed old Online indicator, now combined with Switcher -->
            <div class="absolute inset-y-0 right-3 flex items-center pointer-events-none text-slate-400 dark:text-black-500 group-hover:text-killarney-500">
               <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
            </div>
          </div>
        </div>
        
        <div class="flex items-center gap-4 lg:gap-6">
          <div class="hidden sm:flex items-center gap-2 px-3 py-1.5 bg-slate-50 dark:bg-black-950 rounded-lg border border-slate-200 dark:border-black-800">
            <svg class="w-5 h-5 text-slate-500 dark:text-black-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span class="text-sm text-slate-700 dark:text-black-200 font-medium font-mono tracking-tight">{{ currentTime }}</span>
          </div>

          <!-- Theme Toggle -->
          <button @click="colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'" class="relative p-2 text-slate-400 dark:text-black-500 hover:text-killarney-600 transition-colors rounded-lg hover:bg-slate-100 dark:bg-black-900 flex items-center justify-center outline-none">
             <svg v-if="colorMode.value === 'dark'" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" /></svg>
             <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" /></svg>
          </button>
          
          <!-- Dropdown Info Menu -->
          <div class="relative">
            <button @click="isInfoMenuOpen = !isInfoMenuOpen" @blur="setTimeout(() => isInfoMenuOpen = false, 200)" class="relative p-2 text-slate-400 dark:text-black-500 hover:text-killarney-600 transition-colors rounded-lg hover:bg-slate-100 dark:bg-black-900 flex items-center justify-center outline-none">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
            </button>
            
            <!-- Dropdown content -->
            <div v-show="isInfoMenuOpen" class="absolute right-0 mt-2 w-48 bg-white dark:bg-black-950 border border-slate-200 dark:border-black-800 rounded-xl shadow-lg py-2 z-50">
              <a href="#" @click.prevent="showInformation('how_to_use')" class="block px-4 py-2 text-sm font-medium text-slate-700 dark:text-black-200 hover:bg-slate-50 dark:bg-black-950 hover:text-killarney-600 transition-colors">Как пользоваться</a>
              <a href="#" @click.prevent="showInformation('info')" class="block px-4 py-2 text-sm font-medium text-slate-700 dark:text-black-200 hover:bg-slate-50 dark:bg-black-950 hover:text-killarney-600 transition-colors">Информация</a>
            </div>
          </div>
          
          <button class="lg:hidden p-2 text-slate-500 dark:text-black-400 hover:bg-slate-100 dark:bg-black-900 rounded-lg flex-shrink-0 ml-1" @click="isMobileMenuOpen = true">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
          </button>
        </div>
      </header>

      <main class="flex-1 overflow-y-auto p-6 max-w-[1600px] w-full mx-auto">
        <!-- Dashboard Tab -->
        <div v-show="currentTab === 'dashboard'" class="space-y-6">

      <!-- Map Section (Full Width, Centered) -->
      <section 
        :class="[
          'w-full overflow-hidden relative shadow-md border border-slate-200 dark:border-black-800 group transition-all duration-300',
          isMapFullscreen ? 'fixed inset-0 z-50 rounded-none h-screen bg-slate-100 dark:bg-black-900' : 'rounded-2xl h-[500px] lg:h-[650px]'
        ]"
      >
        <!-- Leaflet Map Container -->
        <div id="map" class="absolute inset-0 h-full w-full z-0"></div>
        
        <!-- Map Overlay Gradients for soft blending -->
        <div class="absolute inset-x-0 top-0 h-32 bg-gradient-to-b from-slate-900/10 w-full opacity-60 pointer-events-none z-10"></div>
        
        <!-- Map Top Bar: Title -->
        <div class="absolute top-4 left-4 flex items-start gap-2 z-20 pointer-events-none">
          <div class="bg-white dark:bg-black-950/90 backdrop-blur-md px-5 py-3 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm pointer-events-auto flex items-center gap-3">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-killarney-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
            </svg>
            <h2 class="font-bold text-slate-800 dark:text-black-100 text-lg">Карта инфраструктуры</h2>
          </div>
          <button @click="toggleFullscreen" class="bg-white dark:bg-black-950/90 backdrop-blur-md p-3 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm pointer-events-auto hover:bg-white dark:bg-black-950 text-slate-600 dark:text-black-300 transition-colors flex items-center justify-center">
            <svg v-if="!isMapFullscreen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" /></svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>

        <!-- AI Panel Toggle Button (visible when panel is hidden) -->
        <button 
          @click="isAIPanelVisible = true"
          :class="['absolute top-16 right-4 z-40 bg-rose-600 hover:bg-rose-700 text-white px-4 py-3 rounded-xl shadow-xl transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] pointer-events-auto flex items-center gap-2 border border-rose-500/50', 
            isAIPanelVisible ? 'opacity-0 translate-x-12 scale-90 pointer-events-none' : 'opacity-100 translate-x-0 scale-100']"
        >
          <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          <span class="font-bold tracking-wide text-sm hidden sm:block">CITY INSIGHT</span>
        </button>


        <!-- AI Insight Panel: Floating HUD overlay on the right -->
        <div 
          :class="['absolute bottom-0 lg:bottom-auto lg:top-16 right-0 lg:right-4 w-full lg:w-96 bg-white dark:bg-black-950/95 backdrop-blur-lg lg:rounded-2xl border-t-4 lg:border-t-0 lg:border-l-[6px] border-rose-500 shadow-2xl flex flex-col h-[400px] lg:h-[calc(100%-5rem)] z-40 pointer-events-auto transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]', 
            isAIPanelVisible ? 'translate-y-0 lg:translate-x-0' : 'translate-y-[120%] lg:translate-y-0 lg:translate-x-[120%]']"
        >
          <div class="p-5 border-b border-slate-100 dark:border-black-900 flex items-center justify-between bg-rose-50 dark:bg-rose-950/30 shrink-0 cursor-pointer" @click="isAIPanelVisible = false">
            <h2 class="font-extrabold text-slate-900 dark:text-black-50 flex items-center gap-2 tracking-tight">
              <svg class="w-6 h-6 text-rose-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
              CITY INSIGHT
            </h2>
            <div class="flex items-center gap-4">
              <span class="animate-pulse flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-3 w-3 rounded-full bg-rose-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-rose-500 dark:bg-rose-500"></span>
              </span>
              <button class="text-slate-400 dark:text-black-500 hover:text-slate-700 dark:text-black-200 transition p-1.5 bg-white dark:bg-black-950/50 hover:bg-white dark:bg-black-950 rounded-lg border border-slate-200 dark:border-black-800">
                <svg class="w-5 h-5 hidden lg:block" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                <svg class="w-5 h-5 lg:hidden" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
              </button>
            </div>
          </div>
          
          <div class="flex-1 overflow-y-auto p-5 space-y-6 custom-scrollbar scroll-smooth overscroll-contain">
            <div>
               <h3 class="text-[10px] font-bold text-slate-400 dark:text-black-500 lowercase tracking-widest mb-1.5 opacity-80">что происходит:</h3>
               <p v-if="cityData" class="text-slate-800 dark:text-black-100 font-bold text-lg leading-tight tracking-tight">
                 {{ cityData.insights.problems[0] }}
               </p>
               <p v-else class="text-slate-400 font-bold text-lg">Загрузка данных...</p>
            </div>
            
            <div class="bg-rose-50 dark:bg-rose-950/30 p-4 rounded-2xl border border-rose-100 dark:border-rose-900/50 flex justify-between items-center shadow-sm">
               <h3 class="text-[10px] font-bold text-rose-500/70 lowercase tracking-widest">насколько критично:</h3>
               <p v-if="cityData" class="text-rose-600 dark:text-rose-400 font-black flex items-center gap-2">
                 {{ cityData.insights.level_ru.toUpperCase() }} 
                 <span :class="['w-3 h-3 rounded-full', cityData.insights.level === 'HIGH' ? 'bg-rose-600' : 'bg-amber-500']"></span>
               </p>
            </div>
            
            <div class="pt-1">
               <h3 class="text-[10px] font-bold text-slate-400 dark:text-black-500 lowercase tracking-widest mb-3 opacity-80">что делать (ai рекомендация):</h3>
               <ul v-if="cityData" class="space-y-2.5">
                 <li v-for="(action, idx) in cityData.insights.actions" :key="idx" class="flex items-center gap-3 p-3 bg-white dark:bg-black-950/50 border border-slate-200 dark:border-black-800 rounded-xl shadow-sm hover:border-killarney-400 hover:shadow-md transition-all cursor-pointer group">
                   <div class="w-8 h-8 rounded-full bg-killarney-50 dark:bg-killarney-950/30 text-killarney-600 flex items-center justify-center shrink-0 group-hover:bg-killarney-600 group-hover:text-white transition-colors">
                     <svg class="w-5 h-5 border-2 border-transparent rounded-full" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                   </div>
                   <span class="text-xs font-bold text-slate-700 dark:text-black-200 group-hover:text-killarney-700 leading-snug">{{ action }}</span>
                 </li>
                 <li class="mt-6 p-4 bg-indigo-50 dark:bg-indigo-950/30 rounded-2xl border border-indigo-100 dark:border-indigo-900/40 shadow-inner">
                    <p class="text-[10px] font-black text-indigo-500 lowercase tracking-widest mb-2 opacity-80 border-b border-indigo-100/50 dark:border-indigo-900/30 pb-1">llm предсказание:</p>
                    <p class="text-[11px] font-medium text-slate-700 dark:text-black-200 leading-relaxed italic">"{{ cityData.llm_recommendation }}"</p>
                 </li>
               </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Info Display (Triggered by Dropdown) -->
      <div id="infoBox" v-if="selectedInfo" class="mt-6 bg-white dark:bg-black-950 p-6 rounded-2xl border border-slate-200 dark:border-black-800 shadow-sm relative animate-in fade-in slide-in-from-top-4">
        <button @click="selectedInfo = null" class="absolute top-4 right-4 p-1.5 text-slate-400 dark:text-black-500 hover:bg-slate-100 dark:bg-black-900 rounded-lg hover:text-slate-700 dark:text-black-200 transition">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
        </button>
        <div v-if="selectedInfo === 'how_to_use'">
          <h2 class="text-xl font-bold text-slate-800 dark:text-black-100 mb-6 flex items-center gap-2 uppercase tracking-tight">
            <svg class="w-6 h-6 text-killarney-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            Как это работает: Три слоя интеллекта
          </h2>
          <div class="space-y-6 text-slate-600 dark:text-black-300 text-sm leading-relaxed max-w-3xl">
            <div class="space-y-2">
              <h3 class="font-bold text-slate-800 dark:text-black-100 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-killarney-100 dark:bg-killarney-900/30 text-killarney-600 flex items-center justify-center text-[10px]">1</span>
                Детекция проблем
              </h3>
              <p>Система непрерывно анализирует индекс трафика, качество воздуха, уровень шума и количество инцидентов. При превышении пороговых значений автоматически формируется список активных проблем.</p>
            </div>

            <div class="space-y-2">
              <h3 class="font-bold text-slate-800 dark:text-black-100 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-killarney-100 dark:bg-killarney-900/30 text-killarney-600 flex items-center justify-center text-[10px]">2</span>
                Оценка критичности
              </h3>
              <p>Каждая ситуация получает составной балл на основе взвешенной комбинации показателей. Результат — уровень тревоги: <span class="font-bold text-rose-500">LOW / MEDIUM / HIGH</span> — и единый City Health Score от 0 до 100.</p>
            </div>

            <div class="space-y-2">
              <h3 class="font-bold text-slate-800 dark:text-black-100 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-killarney-100 dark:bg-killarney-900/30 text-killarney-600 flex items-center justify-center text-[10px]">3</span>
                Причинно-следственный анализ
              </h3>
              <p>Система понимает связи между показателями. Например: высокий трафик → рост загрязнения воздуха. Это позволяет давать рекомендации, которые решают несколько проблем одним действием.</p>
            </div>

            <div class="pt-4 border-t border-slate-100 dark:border-black-900 space-y-3">
              <h3 class="font-black text-xs text-killarney-600 uppercase tracking-widest">Симуляция решений</h3>
              <p>Ключевая функция системы — режим <strong>"Simulate Decision"</strong>. Менеджер выбирает сценарий («закрыть центральную дорогу», «увеличить частоту автобусов», «ограничить дизельный транспорт», «включить зелёную волну») и мгновенно видит, как изменятся показатели города, включая нежелательные побочные эффекты.</p>
              <p class="italic text-slate-400 dark:text-black-500 text-xs">Это превращает систему из инструмента наблюдения в инструмент принятия решений.</p>
            </div>

            <div class="pt-4 border-t border-slate-100 dark:border-black-900 space-y-2">
              <h3 class="font-black text-xs text-indigo-500 uppercase tracking-widest">AI-рекомендации</h3>
              <p>Языковая модель получает текущий срез данных и формулирует управленческую рекомендацию на естественном языке — не шаблонный текст, а вывод, привязанный к конкретной ситуации в городе прямо сейчас.</p>
            </div>
          </div>
        </div>
        <div v-if="selectedInfo === 'info'">
          <h2 class="text-xl font-bold text-slate-800 dark:text-black-100 mb-6 flex items-center gap-2 uppercase tracking-tight">
            <svg class="w-6 h-6 text-killarney-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            Что это?
          </h2>
          <div class="space-y-5 text-slate-600 dark:text-black-300 text-sm leading-relaxed max-w-3xl">
            <p><strong>CityMind AI</strong> — не дашборд с графиками. Это цифровой мозг города: система, которая непрерывно наблюдает за двумя ключевыми направлениями — <span class="text-killarney-600 font-bold">транспортом и экологией</span> — и самостоятельно принимает решения о приоритетах и действиях.</p>
            
            <div class="pt-2">
              <p class="font-bold text-slate-800 dark:text-black-100 mb-3">Система отвечает на три вопроса, которые задаёт каждый городской менеджер:</p>
              <ul class="space-y-2 list-none">
                <li class="flex items-center gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-killarney-500"></div>
                  Что происходит прямо сейчас?
                </li>
                <li class="flex items-center gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-killarney-500"></div>
                  Насколько это критично?
                </li>
                <li class="flex items-center gap-3">
                  <div class="w-1.5 h-1.5 rounded-full bg-killarney-500"></div>
                  Что конкретно нужно сделать?
                </li>
              </ul>
            </div>
            
            <p class="mt-4 pt-4 border-t border-slate-100 dark:border-black-900 text-xs text-slate-400 dark:text-black-500">Версия системы: 1.0.4 (Сборка: Hackathon)</p>
          </div>
        </div>
      </div>
      </div> <!-- End Dashboard Tab -->



      <!-- Ecology Tab -->
      <div v-show="currentTab === 'ecology'" class="space-y-6">
        <div class="flex items-center justify-between mb-4 mt-2">
          <h2 class="text-2xl font-black text-slate-800 dark:text-black-100 tracking-tight flex items-center gap-3">
             <svg class="w-7 h-7 text-killarney-500" fill="currentColor" viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66l.95-2.3c.48.17.98.3 1.34.3C12 20 20 16 20 8h-3zm-1 9.73C14 16.63 11.28 15.65 9 15.5c2.32-.4 6.52-1.04 8 2.23z"/></svg>
             Экология
          </h2>
        </div>
        <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div v-for="(kpi, index) in kpis" :key="index" :class="`bg-white dark:bg-black-950 p-6 rounded-xl border-t-4 shadow-sm transition-shadow hover:shadow-md flex flex-col ${kpi.borderColor}`">
            <div class="flex items-start justify-between mb-4">
              <h3 class="text-sm font-bold text-slate-600 dark:text-black-300 uppercase tracking-wider">{{ kpi.title }}</h3>
            </div>
            <div class="flex items-baseline gap-2">
              <p :class="`text-3xl font-black ${kpi.textColor}`">{{ kpi.value }}</p>
            </div>
            <p class="text-xs font-semibold text-slate-500 dark:text-black-400 mt-2 mb-4">{{ kpi.subtitle }}</p>
            
            <div v-if="kpi.image" class="mt-auto pt-2 overflow-hidden rounded-lg">
              <img :src="kpi.image" alt="KPI visual" class="w-full h-56 object-cover rounded shadow-sm hover:scale-105 transition-transform duration-500" />
            </div>
          </div>
        </section>

        <!-- 20 Points Analytics History -->
        <div class="mt-8 bg-white dark:bg-black-950 p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-black-800 shadow-sm relative overflow-hidden transition-all hover:border-indigo-300 dark:hover:border-indigo-800/50">
          <div class="flex sm:flex-row flex-col items-start sm:items-center justify-between mb-8 gap-4">
            <div>
               <h3 class="text-xl font-black text-slate-800 dark:text-black-100 flex items-center gap-3">
                 <span class="p-2 bg-indigo-50 dark:bg-indigo-950/30 rounded-lg text-indigo-500"><svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z" /></svg></span>
                 История состояний (последние 20 точек)
               </h3>
               <p class="text-sm text-slate-500 dark:text-black-400 mt-2 font-medium">Динамика изменения уровня выбросов и загруженности во времени.</p>
            </div>
            <div class="bg-indigo-50 dark:bg-indigo-950/30 text-indigo-600 px-4 py-2 rounded-xl text-xs font-bold border border-indigo-200 dark:border-indigo-800/50 uppercase tracking-widest flex items-center gap-2">
               <span class="w-2 h-2 rounded-full bg-indigo-500 animate-pulse"></span>
               Аналитика активна
            </div>
          </div>
          
          <div class="h-64 w-full relative group">
             <!-- Background Grid Lines -->
             <div class="absolute inset-x-0 inset-y-6 flex flex-col justify-between opacity-30 pointer-events-none z-0">
               <div class="border-b border-slate-300 dark:border-black-700 w-full border-dashed"></div>
               <div class="border-b border-slate-300 dark:border-black-700 w-full border-dashed"></div>
               <div class="border-b border-slate-300 dark:border-black-700 w-full border-dashed"></div>
               <div class="border-b border-slate-300 dark:border-black-700 w-full border-dashed"></div>
             </div>
             
             <!-- Reactive Bars derived from chart1Data -->
             <div class="w-full h-full flex items-end justify-between px-1 pb-6 gap-1 sm:gap-2 relative z-10">
                <div v-for="(val, idx) in chart1Data.slice(-20)" :key="idx" class="w-full h-full relative group/bar flex items-end justify-center">
                   <!-- Tooltip -->
                   <div class="absolute bottom-full mb-2 opacity-0 group-hover/bar:opacity-100 transition-opacity bg-slate-800 text-white text-[11px] font-bold py-1.5 px-2.5 rounded-lg whitespace-nowrap shadow-xl pointer-events-none z-20">
                     Значение: {{ val }}
                     <svg class="absolute text-slate-800 h-2 w-full left-0 top-full" x="0px" y="0px" viewBox="0 0 255 255" xml:space="preserve"><polygon class="fill-current" points="0,0 127.5,127.5 255,0"/></svg>
                   </div>
                   <!-- Value Bar -->
                   <div class="w-full bg-gradient-to-t from-indigo-600 to-sky-400 rounded-md transition-all duration-700 ease-in-out group-hover/bar:from-sky-400 group-hover/bar:to-sky-300 group-hover/bar:-translate-y-1" :style="{height: `${val}%`}"></div>
                </div>
             </div>
             
             <!-- X-Axis Labels -->
             <div class="absolute bottom-0 left-0 right-0 flex justify-between text-[11px] font-bold text-slate-400 dark:text-black-500 uppercase tracking-widest px-2">
               <span>-20 циклов</span>
               <span class="hidden sm:inline">-15</span>
               <span>-10</span>
               <span class="hidden sm:inline">-5</span>
               <span class="text-indigo-500">Сейчас</span>
             </div>
          </div>
        </div>
      </div>

      <!-- Analytics Tab -->
      <div v-show="currentTab === 'analytics'" class="space-y-6">
        <div class="flex items-center justify-between mb-4 mt-2">
          <h2 class="text-2xl font-black text-slate-800 dark:text-black-100 tracking-tight flex items-center gap-3">
             <svg class="w-7 h-7 text-killarney-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
               <rect x="4" y="14" width="4" height="6" rx="1.5"/>
               <rect x="10" y="8" width="4" height="12" rx="1.5"/>
               <rect x="16" y="4" width="4" height="16" rx="1.5"/>
             </svg>
             Аналитика
          </h2>
          
          <div class="flex items-center gap-2 bg-indigo-50 dark:bg-indigo-950/30 px-4 py-2 rounded-xl border border-indigo-200 dark:border-indigo-800/50">
            <span class="relative flex h-2 w-2">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
            </span>
            <span class="text-[10px] font-black text-indigo-600 uppercase tracking-widest">Прогноз активен</span>
          </div>
        </div>

        <!-- Dynamic Simulation Scenarios moved to Analytics -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
           <div 
             v-for="(scenario, key) in scenarios" 
             :key="key"
             @mouseenter="hoveredScenario = key"
             @mouseleave="hoveredScenario = null"
             @click="triggerSim(key)"
             :class="[
               'p-5 rounded-2xl border transition-all cursor-pointer group relative overflow-hidden h-full flex flex-col',
               hoveredScenario === key 
                ? 'bg-white dark:bg-black-900 border-killarney-500 shadow-2xl shadow-killarney-500/10 -translate-y-1' 
                : 'bg-white dark:bg-black-950 border-slate-200 dark:border-black-800 hover:border-slate-400 shadow-sm'
             ]"
           >
              <div class="flex items-center justify-between mb-4 relative z-10">
                <div :class="[
                  'w-8 h-8 rounded-lg flex items-center justify-center transition-colors',
                  hoveredScenario === key ? 'bg-killarney-50 dark:bg-killarney-900/30' : 'bg-slate-100 dark:bg-black-900'
                ]">
                  <div v-if="key === 'close_road'" :class="['w-2.5 h-2.5 rounded-full', hoveredScenario === key ? 'bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.4)]' : 'bg-rose-500/60']"></div>
                  <div v-else-if="key === 'increase_buses'" :class="['w-2.5 h-2.5 rounded-sm', hoveredScenario === key ? 'bg-indigo-500 shadow-[0_0_8px_rgba(99,102,241,0.4)]' : 'bg-indigo-500/60']"></div>
                  <div v-else-if="key === 'restrict_diesel'" :class="['w-2.5 h-2.5 rotate-45 rounded-[1px]', hoveredScenario === key ? 'bg-amber-500 shadow-[0_0_8px_rgba(245,158,11,0.4)]' : 'bg-amber-500/60']"></div>
                  <div v-else-if="key === 'green_wave'" :class="['w-3 h-1 rounded-full', hoveredScenario === key ? 'bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.4)]' : 'bg-emerald-500/60']"></div>
                  <div v-else :class="['w-2.5 h-2.5 rounded-full bg-slate-400']"></div>
                </div>
                
                <div v-if="hoveredScenario === key" class="bg-killarney-50 dark:bg-killarney-900/40 px-2.5 py-1 rounded-md text-[7px] font-black text-killarney-600 dark:text-killarney-400 uppercase tracking-[0.1em] border border-killarney-100 dark:border-killarney-800">
                  Forecast
                </div>
              </div>
              
              <h3 :class="['font-black text-[10px] uppercase tracking-widest mb-2 relative z-10 transition-colors', hoveredScenario === key ? 'text-slate-900 dark:text-white' : 'text-slate-700 dark:text-black-200']">
                {{ scenario.label }}
              </h3>
              
              <p :class="['text-[9px] font-medium leading-relaxed relative z-10 transition-colors', hoveredScenario === key ? 'text-slate-600 dark:text-black-300' : 'text-slate-500 dark:text-black-400']">
                {{ scenario.prediction }}
              </p>
           </div>
        </div>

      <!-- Charts (2 graphs side by side) -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Chart 1: Traffic over time -->
        <div class="bg-white dark:bg-black-950 p-6 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm relative overflow-hidden">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-bold text-slate-800 dark:text-black-100">Трафик со временем</h3>
            <div class="flex items-center gap-3">
              <div v-if="hoveredScenario" class="flex items-center gap-2 text-[10px] font-black text-indigo-500 bg-indigo-50 dark:bg-indigo-950/30 px-2 py-1 rounded-lg border border-indigo-200 animate-pulse">
                <span>ПРЕДИКТИВНАЯ ГИПОТЕЗА</span>
              </div>
            </div>
          </div>
          
          <div class="h-64 relative overflow-hidden flex flex-col pb-2 mt-4">
             <div class="flex-1 w-full relative">
               <svg viewBox="0 0 400 150" class="w-full h-full preserve-3d absolute inset-0" preserveAspectRatio="none">
                 <defs>
                    <linearGradient id="trafficGradient" x1="0" y1="0" x2="0" y2="1">
                       <stop offset="0%" stop-color="#6366f1" stop-opacity="0.25"/>
                       <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
                    </linearGradient>
                    <linearGradient id="predictionGradient" x1="0" y1="0" x2="0" y2="1">
                       <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.2"/>
                       <stop offset="100%" stop-color="#f43f5e" stop-opacity="0"/>
                    </linearGradient>
                 </defs>
                 
                 <!-- Area Fill (Active) -->
                 <path :d="trafficPath" fill="url(#trafficGradient)" class="transition-all duration-700 ease-in-out" />
                 
                 <!-- Prediction Path (Visible on Hover) -->
                 <path 
                   v-if="hoveredScenario" 
                   :d="trafficPredictionPath" 
                   fill="url(#predictionGradient)" 
                   class="animate-pulse"
                 />
                 
                 <!-- Solid curve (Active) -->
                 <path :d="trafficPathMain" fill="none" class="stroke-indigo-500 transition-all duration-700 ease-in-out" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
                 
                 <!-- Solid prediction curve -->
                 <path 
                   v-if="hoveredScenario" 
                   :d="trafficPredictionPathMain" 
                   fill="none" 
                   class="stroke-rose-500 stroke-dasharray-4 transition-all duration-500" 
                   stroke-width="3" 
                   stroke-linecap="round" 
                   stroke-dasharray="8 4"
                 />
               </svg>
             </div>
             <!-- X-Axis Labels -->
             <div class="flex justify-between text-xs text-slate-400 dark:text-black-500 font-bold z-10 px-1 mt-2">
               <span>00:00</span>
               <span>06:00</span>
               <span>12:00</span>
               <span>18:00</span>
               <span>24:00</span>
             </div>
          </div>
        </div>

        <!-- Chart 2: AQI over time -->
        <div class="bg-white dark:bg-black-950 p-6 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm relative overflow-hidden">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-bold text-slate-800 dark:text-black-100">Качество воздуха (AQI)</h3>
            <div class="flex items-center gap-3">
              <div v-if="hoveredScenario" class="flex items-center gap-2 text-[10px] font-black text-emerald-500 bg-emerald-50 dark:bg-emerald-950/30 px-2 py-1 rounded-lg border border-emerald-200 animate-pulse">
                <span>ЭКО-ПРОГНОЗ</span>
              </div>
              <span class="flex items-center gap-1.5 text-xs font-bold text-amber-500 bg-amber-50 dark:bg-amber-950/30 px-2 py-1 rounded-md">
                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                PM 2.5
              </span>
            </div>
          </div>
          
          <div class="h-64 relative overflow-hidden flex flex-col pb-2 mt-4">
             <div class="flex-1 w-full relative">
               <svg viewBox="0 0 400 150" class="w-full h-full preserve-3d absolute inset-0" preserveAspectRatio="none">
                 <defs>
                    <linearGradient id="airGradient" x1="0" y1="0" x2="0" y2="1">
                       <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
                       <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
                    </linearGradient>
                 </defs>
                 
                 <!-- Area Fill (Active) -->
                 <path :d="airPath" fill="url(#airGradient)" class="transition-all duration-700 ease-in-out" />
                 
                 <!-- Prediction Path (Visible on Hover) -->
                 <path 
                   v-if="hoveredScenario" 
                   :d="airPredictionPath" 
                   fill="rgba(16, 185, 129, 0.1)" 
                   class="animate-pulse"
                 />
                 
                 <!-- Solid curve (Active) -->
                 <path :d="airPathMain" fill="none" class="stroke-emerald-500 transition-all duration-700 ease-in-out" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
                 
                 <!-- Solid prediction curve -->
                 <path 
                   v-if="hoveredScenario" 
                   :d="airPredictionPathMain" 
                   fill="none" 
                   class="stroke-emerald-400 stroke-dasharray-4 transition-all duration-500" 
                   stroke-width="3" 
                   stroke-linecap="round" 
                   stroke-dasharray="8 4"
                 />
               </svg>
             </div>
             <!-- X-Axis Labels (Days) -->
             <div class="flex justify-between text-xs text-slate-400 dark:text-black-500 font-bold z-10 px-1 mt-2">
               <span>Пн</span>
               <span>Вт</span>
               <span>Ср</span>
               <span>Чт</span>
               <span>Пт</span>
               <span>Сб</span>
               <span>Вс</span>
             </div>
          </div>
        </div>
      </section>
      </div> <!-- End Analytics Tab -->
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted, computed } from 'vue'
import { useCityData } from '../composables/useCityData'

const selectedCity = ref('Алматы')
const { data: cityData, scenarios, isConnected } = useCityData(selectedCity)

const systemMode = ref('live')
const hoveredScenario = ref(null)
const currentTime = ref('')
const isMobileMenuOpen = ref(false)
const isInfoMenuOpen = ref(false)
const selectedInfo = ref(null)
const isMapFullscreen = ref(false)
const isAIPanelVisible = ref(true)
const currentTab = ref('dashboard')
const colorMode = useColorMode()
let mapInstance = null
let mapTileLayer = null

const showInformation = (infoType) => {
  selectedInfo.value = infoType
  isInfoMenuOpen.value = false
  currentTab.value = 'dashboard'
  setTimeout(() => {
    const el = document.getElementById('infoBox')
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'end' })
  }, 100)
}

watch(currentTab, (newTab) => {
  if (newTab === 'dashboard') {
    setTimeout(() => {
      if (mapInstance) mapInstance.invalidateSize()
    }, 100) // Delay to wait for UI rendering
  }
})

const toggleFullscreen = () => {
  isMapFullscreen.value = !isMapFullscreen.value
  setTimeout(() => {
    if (mapInstance) mapInstance.invalidateSize()
  }, 300)
}

const getCityCoords = (city) => {
  if (city === 'Астана') return [51.1694, 71.4491];
  if (city === 'Шымкент') return [42.3417, 69.5901];
  return [43.2389, 76.8897]; // Almaty
};

let timer
onMounted(() => {
  const updateTime = () => {
    currentTime.value = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }
  updateTime()
  timer = setInterval(updateTime, 1000)

  // Initialize Leaflet Map
  const initLeafletMap = () => {
    if (!window.L) {
      setTimeout(initLeafletMap, 100);
      return;
    }
    
    // Clear the map container first if it already has a map (fixes hot-reload issues)
    const mapContainer = document.getElementById('map');
    if (mapContainer && mapContainer._leaflet_id) {
       mapContainer._leaflet_id = null;
       mapContainer.innerHTML = '';
    }

    mapInstance = L.map('map', { 
      zoomControl: false,
      attributionControl: false
    }).setView(getCityCoords(selectedCity.value), 12);
    
    const tileUrl = colorMode.value === 'dark' 
      ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
      : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
      
      mapTileLayer = L.tileLayer(tileUrl, {
      subdomains: 'abcd',
      maxZoom: 20
    }).addTo(mapInstance);

    // No static dots logic here anymore, moved to renderMarkers
  }
  
  initLeafletMap();

  const renderMarkers = (city) => {
    if (!mapInstance || !window.L) return;

    // Clear old markers
    mapInstance.eachLayer((layer) => {
      if (layer instanceof L.CircleMarker) {
        mapInstance.removeLayer(layer);
      }
    });

    const coords = getCityCoords(city);
    const count = Math.floor(Math.random() * (35 - 20 + 1)) + 20;
    const incidentTypes = [
      '<b>Крупное ДТП</b><br>Заблокировано 2 полосы',
      '<b>Затор (Traffic Jam)</b><br>Скорость потока < 10 км/ч',
      '<b>Дорожные работы</b><br>Ремонт инфраструктуры',
      '<b>Остановка движения</b><br>Сбой умного светофора',
      '<b>Повышенный выброс AQI</b><br>Локальное загрязнение в 2 раза',
      '<b>Авария с общественным транспортом</b><br>Требуется перенаправление',
      '<b>Сложные метеоусловия</b><br>Затопление / гололед'
    ];

    for (let i = 0; i < count; i++) {
      const lat = coords[0] - 0.06 + Math.random() * 0.12;
      const lon = coords[1] - 0.08 + Math.random() * 0.16;
      const incident = incidentTypes[(i * 3 + 1) % incidentTypes.length];
      
      L.circleMarker([lat, lon], {
        radius: 8,
        fillColor: "#ef4444",
        color: "#ffffff",
        weight: 3,
        opacity: 1,
        fillOpacity: 0.9
      }).addTo(mapInstance).bindPopup(incident);
    }
  };

  // Initial markers
  setTimeout(() => renderMarkers(selectedCity.value), 500);

  watch(() => colorMode.value, (newMode) => {
    if (mapTileLayer) {
      const tileUrl = newMode === 'dark' 
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
      mapTileLayer.setUrl(tileUrl);
    }
  });

  // Reactive City Switching
  watch(selectedCity, (newCity) => {
    if (!mapInstance) return;
    const coords = getCityCoords(newCity);
    mapInstance.flyTo(coords, 12, { duration: 1.5 });
    renderMarkers(newCity);
  });
})

onUnmounted(() => {
  clearInterval(timer)
})

const toggleStatus = () => {
  systemMode.value = systemMode.value === 'live' ? 'simulation' : 'live'
}

useHead({
  title: 'CityMind AI - Intelligent City Control Dashboard',
  meta: [
    { name: 'description', content: 'CityMind AI operations and simulation control panel.' }
  ],
  link: [
    { rel: 'stylesheet', href: 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css' }
  ],
  script: [
    {
      src: 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
      defer: true
    }
  ],
  bodyAttrs: {
    class: 'bg-slate-50 dark:bg-black-950'
  }
})

// Mock icons mapped to heroicons or similar intuitive SVG structures
const ActivityIcon = { template: `<svg fill="none"></svg>` }

// Dynamic Chart Helper Paths (Truly Data Driven)
const generatePath = (dataArr, useArea = false, modifier = 0) => {
  if (!dataArr || dataArr.length === 0) return '';
  const width = 400;
  const height = 150;
  const points = dataArr.map((v, i) => {
    const x = (i / (dataArr.length - 1)) * width;
    // Apply modifier then scale to 0-100 range and map to 0-height
    const valWithMod = Math.min(100, Math.max(0, v + modifier));
    const y = height - (valWithMod * 1.2) - 20; // 1.2 scale to leave room at top
    return `${x},${y}`;
  });
  
  if (points.length < 2) return '';
  
  // Create a smooth curve using cubic splines or simple lines for now (L)
  // Actually, let's use a simple polyline or Q/C for smoothness. 
  // For a hackathon, a polyline is safe, but let's try a simplified curve.
  let path = `M${points[0]}`;
  for (let i = 1; i < points.length; i++) {
    path += ` L${points[i]}`;
  }
  
  if (useArea) {
    path += ` L${width},${height} L0,${height} Z`;
  }
  return path;
}

const trafficPath = computed(() => {
  const data = chart1Data.value.length > 0 ? chart1Data.value : [40, 50, 45, 60, 55, 70, 65];
  return generatePath(data, true);
})

const trafficPathMain = computed(() => {
  const data = chart1Data.value.length > 0 ? chart1Data.value : [40, 50, 45, 60, 55, 70, 65];
  return generatePath(data, false);
})

const trafficPredictionPath = computed(() => {
  if (!hoveredScenario.value) return '';
  let mod = 0;
  if (hoveredScenario.value === 'close_road') mod = 25;
  if (hoveredScenario.value === 'increase_buses') mod = -20;
  if (hoveredScenario.value === 'green_wave') mod = -15;
  if (hoveredScenario.value === 'restrict_diesel') mod = -5;

  const data = chart1Data.value.length > 0 ? chart1Data.value : [40, 50, 45, 60, 55, 70, 65];
  return generatePath(data, true, mod);
})

const trafficPredictionPathMain = computed(() => {
  if (!hoveredScenario.value) return '';
  let mod = 0;
  if (hoveredScenario.value === 'close_road') mod = 25;
  if (hoveredScenario.value === 'increase_buses') mod = -20;
  if (hoveredScenario.value === 'green_wave') mod = -15;
  if (hoveredScenario.value === 'restrict_diesel') mod = -5;

  const data = chart1Data.value.length > 0 ? chart1Data.value : [40, 50, 45, 60, 55, 70, 65];
  return generatePath(data, false, mod);
})

const airPath = computed(() => {
  const data = chart2Data.value.length > 0 ? chart2Data.value : [30, 35, 45, 55, 65, 60, 70];
  return generatePath(data, true);
})

const airPathMain = computed(() => {
  const data = chart2Data.value.length > 0 ? chart2Data.value : [30, 35, 45, 55, 65, 60, 70];
  return generatePath(data, false);
})

const airPredictionPath = computed(() => {
  if (!hoveredScenario.value) return '';
  let mod = 0;
  if (hoveredScenario.value === 'restrict_diesel') mod = -30;
  if (hoveredScenario.value === 'increase_buses') mod = -15;
  if (hoveredScenario.value === 'close_road') mod = -10; // assuming less cars in center = better air

  const data = chart2Data.value.length > 0 ? chart2Data.value : [30, 35, 45, 55, 65, 60, 70];
  return generatePath(data, true, mod);
})

const airPredictionPathMain = computed(() => {
  if (!hoveredScenario.value) return '';
  let mod = 0;
  if (hoveredScenario.value === 'restrict_diesel') mod = -30;
  if (hoveredScenario.value === 'increase_buses') mod = -15;
  if (hoveredScenario.value === 'close_road') mod = -10;

  const data = chart2Data.value.length > 0 ? chart2Data.value : [30, 35, 45, 55, 65, 60, 70];
  return generatePath(data, false, mod);
})

const kpis = computed(() => {
  if (!cityData.value) {
    return [
      { title: 'УРОВЕНЬ ТРАФИКА', value: 'Загрузка...', subtitle: '...', borderColor: 'border-t-slate-300', textColor: 'text-slate-400' },
      { title: 'КАЧЕСТВО ВОЗДУХА', value: 'Загрузка...', subtitle: '...', borderColor: 'border-t-slate-300', textColor: 'text-slate-400' },
      { title: 'ИНДЕКС ЗДОРОВЬЯ', value: 'Загрузка...', subtitle: '...', borderColor: 'border-t-slate-300', textColor: 'text-slate-400' },
      { title: 'АКТИВНЫЕ АЛЕРТЫ', value: 'Загрузка...', subtitle: '...', borderColor: 'border-t-slate-300', textColor: 'text-slate-400' },
    ]
  }

  const { metrics, insights } = cityData.value
  
  // Mapping color/severity based on backend insights
  const trafficColor = insights.level === 'HIGH' ? 'text-rose-600' : (insights.level === 'MEDIUM' ? 'text-amber-500' : 'text-emerald-600')
  const trafficBorder = insights.level === 'HIGH' ? 'border-t-rose-500' : (insights.level === 'MEDIUM' ? 'border-t-amber-400' : 'border-t-emerald-500')

  const airSeverity = metrics.air_quality_index > 200 ? 'Очень плохо' : (metrics.air_quality_index > 100 ? 'Нездоровый' : 'Хороший')
  const airColor = metrics.air_quality_index > 200 ? 'text-rose-600' : (metrics.air_quality_index > 100 ? 'text-amber-500' : 'text-emerald-600')
  const airBorder = metrics.air_quality_index > 200 ? 'border-t-rose-500' : (metrics.air_quality_index > 100 ? 'border-t-amber-400' : 'border-t-emerald-500')

  return [
    { 
      title: 'УРОВЕНЬ ТРАФИКА', 
      value: insights.level_ru, 
      subtitle: `${metrics.traffic_index}% загруженности`, 
      borderColor: trafficBorder, 
      textColor: trafficColor, 
      image: '/traffic_new.png' 
    },
    { 
      title: 'КАЧЕСТВО ВОЗДУХА', 
      value: `${metrics.air_quality_index} AQI`, 
      subtitle: airSeverity, 
      borderColor: airBorder, 
      textColor: airColor, 
      image: '/smoke.png' 
    },
    { 
      title: 'ИНДЕКС ЗДОРОВЬЯ', 
      value: `${insights.city_health_score}/100`, 
      subtitle: 'Статистика', 
      borderColor: 'border-t-emerald-500', 
      textColor: 'text-emerald-600', 
      image: '/health_index.png' 
    },
    { 
      title: 'ОПОВЕЩЕНИЯ', 
      value: metrics.active_incidents.toString(), 
      subtitle: 'Требуют внимания', 
      borderColor: 'border-t-orange-500', 
      textColor: 'text-orange-600',
      image: '/alerts.png'
    },
  ]
})

const chart1Data = computed(() => cityData.value?.history.map(h => h.traffic_index) || [])
const chart2Data = computed(() => cityData.value?.history.map(h => h.air_quality_index) || [])

const isSimulating = computed(() => cityData.value?.insights.is_simulation || false)

const triggerSim = async (key) => {
  if (isSimulating.value) return;
  
  const config = useRuntimeConfig()

  try {
    const response = await fetch(`${config.public.apiUrl}/api/simulate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
        scenario: key,
        city: selectedCity.value
      })
    })
    
    if (!response.ok) throw new Error('Simulation trigger failed')
  } catch (err) {
    console.error('Error triggering simulation:', err)
  }
}
</script>

<style scoped>
/* Optional grid background or subtle styling */
</style>