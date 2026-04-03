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
        
        <NuxtLink to="/simulation" class="w-full flex items-center justify-start gap-3 px-3 py-2.5 rounded-xl text-sm font-bold transition-all shadow-sm bg-gradient-to-r from-killarney-500 to-killarney-600 text-white shadow-killarney-500/20 hover:from-killarney-600 hover:to-killarney-700 mt-2">
          <svg class="w-5 h-5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
          <span class="block">Режим симуляции</span>
        </NuxtLink>
      </nav>
    </aside>

    <!-- Main Wrapper -->
    <div class="flex-1 flex flex-col min-w-0 overflow-hidden relative">
      <!-- Top Bar -->
      <header class="bg-white dark:bg-black-950 border-b border-slate-200 dark:border-black-800 h-16 shrink-0 px-4 md:px-6 flex items-center justify-between z-10 w-full">
        <div class="flex items-center gap-4 md:gap-6">
          <div class="flex items-center gap-2">
            <h1 class="text-xl font-black tracking-tight text-slate-800 dark:text-black-100 leading-none lg:hidden hidden sm:block">CityMind</h1>
          </div>
          
          <div class="h-6 w-px bg-slate-200 hidden md:block"></div>
          
          <div class="hidden md:flex items-center gap-2 bg-slate-50 dark:bg-black-950 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-black-800 hover:border-killarney-300 transition-colors cursor-pointer group relative">
            <svg class="w-5 h-5 text-slate-500 dark:text-black-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            <select class="bg-transparent border-none text-sm font-medium text-slate-700 dark:text-black-200 outline-none cursor-pointer group-hover:text-killarney-600 appearance-none pr-6 relative z-10 w-fit">
              <option>Алматы</option>
            </select>
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
          
          <div class="flex-1 overflow-y-auto p-5 space-y-5">
            <div>
               <h3 class="text-[10px] font-bold text-slate-400 dark:text-black-500 uppercase tracking-widest mb-1.5">ЧТО ПРОИСХОДИТ:</h3>
               <p class="text-slate-800 dark:text-black-100 font-bold text-lg leading-tight">Тревога: критическая пробка <br><span class="text-sm text-slate-500 dark:text-black-400 font-medium">Обнаружен затор в центре</span></p>
            </div>
            
            <div class="bg-rose-50 dark:bg-rose-950/30 p-3.5 rounded-xl border border-rose-100 flex justify-between items-center">
               <h3 class="text-[10px] font-bold text-rose-500/70 uppercase tracking-widest">НАСКОЛЬКО КРИТИЧНО:</h3>
               <p class="text-rose-600 font-black flex items-center gap-2">ВЫСOКИЙ <span class="w-3 h-3 rounded-full bg-rose-600"></span></p>
            </div>
            
            <div class="pt-1">
               <h3 class="text-[10px] font-bold text-slate-400 dark:text-black-500 uppercase tracking-widest mb-2.5">ЧТО ДЕЛАТЬ (AI РЕКОМЕНДАЦИЯ):</h3>
               <ul class="space-y-2.5">
                 <li class="flex items-center gap-3 p-2.5 bg-white dark:bg-black-950 border border-slate-200 dark:border-black-800 rounded-lg shadow-sm hover:border-killarney-400 hover:shadow-md transition-all cursor-pointer group">
                   <div class="w-7 h-7 rounded-full bg-killarney-50 dark:bg-killarney-950/30 text-killarney-600 flex items-center justify-center shrink-0 group-hover:bg-killarney-600 group-hover:text-white transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h8M8 11h8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div>
                   <span class="text-xs font-bold text-slate-700 dark:text-black-200 group-hover:text-killarney-700">Увеличить автобусы</span>
                 </li>
                 <li class="flex items-center gap-3 p-2.5 bg-white dark:bg-black-950 border border-slate-200 dark:border-black-800 rounded-lg shadow-sm hover:border-killarney-400 hover:shadow-md transition-all cursor-pointer group">
                   <div class="w-7 h-7 rounded-full bg-rose-50 dark:bg-rose-950/30 text-rose-600 flex items-center justify-center shrink-0 group-hover:bg-rose-600 group-hover:text-white transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg></div>
                   <span class="text-xs font-bold text-slate-700 dark:text-black-200 group-hover:text-rose-700">Ограничить въезд</span>
                 </li>
                 <li class="flex items-center gap-3 p-2.5 bg-white dark:bg-black-950 border border-slate-200 dark:border-black-800 rounded-lg shadow-sm hover:border-emerald-400 hover:shadow-md transition-all cursor-pointer group">
                   <div class="w-7 h-7 rounded-full bg-emerald-50 dark:bg-emerald-950/30 text-emerald-600 flex items-center justify-center shrink-0 group-hover:bg-emerald-600 group-hover:text-white transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg></div>
                   <span class="text-xs font-bold text-slate-700 dark:text-black-200 group-hover:text-emerald-700">Оповестить жителей</span>
                 </li>
               </ul>
            </div>
            
            <div class="mt-auto pt-2">
              <button class="w-full py-3.5 bg-killarney-600 hover:bg-killarney-700 text-white text-sm font-bold rounded-xl shadow-lg shadow-killarney-600/20 transition-transform active:scale-[0.98]">
                Применить стратегии
              </button>
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
          <h2 class="text-xl font-bold text-slate-800 dark:text-black-100 mb-4 flex items-center gap-2">
            <svg class="w-6 h-6 text-killarney-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            Как пользоваться системой?
          </h2>
          <div class="space-y-3 text-slate-600 dark:text-black-300 text-sm leading-relaxed">
            <p>1. Изучайте интерактивную карту для мониторинга инфраструктуры города.</p>
            <p>2. Используйте <strong>CITY INSIGHT</strong> для получения AI-рекомендаций и запуска симуляций.</p>
            <p>3. Переключайтесь между вкладками Экология и Аналитика для детального просмотра.</p>
            <p>4. Применяйте стратегии, предложенные AI, для улучшения городских показателей.</p>
          </div>
        </div>
        <div v-if="selectedInfo === 'info'">
          <h2 class="text-xl font-bold text-slate-800 dark:text-black-100 mb-4 flex items-center gap-2">
            <svg class="w-6 h-6 text-killarney-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            Информация
          </h2>
          <div class="space-y-3 text-slate-600 dark:text-black-300 text-sm leading-relaxed">
            <p><strong>CityMind AI</strong> — это интеллектуальная панель управления городскими смарт-системами, созданная для оптимизации городской среды.</p>
            <p>Система объединяет алгоритмы ИИ с данными в реальном времени для симуляции и принятия решений.</p>
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
      </div>

      <!-- Analytics Tab -->
      <div v-show="currentTab === 'analytics'" class="space-y-6">
        <!-- Analytics Section -->
        <div class="flex items-center justify-between mb-4 mt-2">
          <h2 class="text-2xl font-black text-slate-800 dark:text-black-100 tracking-tight flex items-center gap-3">
             <svg class="w-7 h-7 text-killarney-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
               <rect x="4" y="14" width="4" height="6" rx="1.5"/>
               <rect x="10" y="8" width="4" height="12" rx="1.5"/>
               <rect x="16" y="4" width="4" height="16" rx="1.5"/>
             </svg>
             Аналитика
          </h2>
        </div>

      <!-- Charts (2 graphs side by side) -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Chart 1: Traffic over time -->
        <div class="bg-white dark:bg-black-950 p-6 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-bold text-slate-800 dark:text-black-100">Трафик со временем</h3>
            <select class="text-sm border border-slate-200 dark:border-black-800 rounded-lg px-2 py-1 text-slate-600 dark:text-black-300 bg-white dark:bg-black-950 outline-none focus:ring-1 focus:ring-killarney-500 font-medium">
              <option>За 24 часа</option>
              <option>За 7 дней</option>
            </select>
          </div>
          <!-- Curved Area Chart Container -->
          <div class="h-64 relative overflow-hidden flex flex-col pb-2 mt-4">
             <div class="flex-1 w-full relative">
               <svg viewBox="0 0 400 150" class="w-full h-full preserve-3d absolute inset-0" preserveAspectRatio="none">
                 <defs>
                    <linearGradient id="trafficGradient" x1="0" y1="0" x2="0" y2="1">
                       <stop offset="0%" stop-color="#6366f1" stop-opacity="0.25"/>
                       <stop offset="100%" stop-color="#6366f1" stop-opacity="0"/>
                    </linearGradient>
                 </defs>
                 <!-- Dotted lighter line -->
                 <path d="M0,80 C40,70 80,40 120,50 C160,60 200,90 240,80 C280,70 320,30 360,40 C380,45 390,60 400,70" fill="none" class="stroke-slate-200" stroke-width="2.5" stroke-dasharray="4 4" />
                 
                 <!-- Area Fill -->
                 <path d="M0,60 C40,50 80,20 120,30 C160,40 200,70 240,60 C280,50 320,10 360,20 C380,25 390,40 400,50 L400,150 L0,150 Z" fill="url(#trafficGradient)" />
                 
                 <!-- Solid curve -->
                 <path d="M0,60 C40,50 80,20 120,30 C160,40 200,70 240,60 C280,50 320,10 360,20 C380,25 390,40 400,50" fill="none" class="stroke-indigo-500" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
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

        <!-- Chart 2: Air quality over time -->
        <div class="bg-white dark:bg-black-950 p-6 rounded-xl border border-slate-200 dark:border-black-800 shadow-sm">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-bold text-slate-800 dark:text-black-100">Качество воздуха (AQI)</h3>
             <div class="flex gap-2">
                <span class="flex items-center gap-1 text-xs text-slate-500 dark:text-black-400 font-medium"><span class="w-3 h-3 rounded bg-amber-400"></span> PM 2.5</span>
             </div>
          </div>
          <!-- Curved Area Chart Container -->
          <div class="h-64 relative overflow-hidden flex flex-col pb-2 mt-4">
             <div class="flex-1 w-full relative">
               <svg viewBox="0 0 400 150" class="w-full h-full preserve-3d absolute inset-0" preserveAspectRatio="none">
                 <defs>
                    <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
                       <stop offset="0%" stop-color="#4d9a5c" stop-opacity="0.25"/>
                       <stop offset="100%" stop-color="#4d9a5c" stop-opacity="0"/>
                    </linearGradient>
                 </defs>
                 <!-- Dotted lighter line -->
                 <path d="M0,120 C40,105 80,100 120,65 C160,30 200,35 240,25 C280,15 320,70 360,50 C380,40 390,35 400,30" fill="none" class="stroke-slate-200" stroke-width="2.5" stroke-dasharray="4 4" />
                 
                 <!-- Area Fill -->
                 <path d="M0,105 C40,85 80,90 120,45 C160,0 200,10 240,0 C280,-10 320,50 360,30 C380,20 390,15 400,10 L400,150 L0,150 Z" fill="url(#chartGradient)" />
                 
                 <!-- Solid green curve -->
                 <path d="M0,105 C40,85 80,90 120,45 C160,0 200,10 240,0 C280,-10 320,50 360,30 C380,20 390,15 400,10" fill="none" class="stroke-killarney-500" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
               </svg>
             </div>
             <!-- X-Axis Labels -->
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
import { ref, watch, onMounted, onUnmounted } from 'vue'

const isLive = ref(true)
const isSimulation = ref(false)
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
    }).setView([43.2389, 76.8897], 13);
    
    const tileUrl = colorMode.value === 'dark' 
      ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
      : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
      
    mapTileLayer = L.tileLayer(tileUrl, {
      subdomains: 'abcd',
      maxZoom: 20
    }).addTo(mapInstance);
  }
  
  initLeafletMap();

  watch(() => colorMode.value, (newMode) => {
    if (mapTileLayer) {
      const tileUrl = newMode === 'dark' 
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
      mapTileLayer.setUrl(tileUrl);
    }
  });
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

const kpis = ref([
  { title: 'УРОВЕНЬ ТРАФИКА', value: 'КРИТИЧНО', subtitle: '88% загруженности', borderColor: 'border-t-rose-500', textColor: 'text-rose-600', image: 'https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?auto=format&fit=crop&w=800&q=80' },
  { title: 'КАЧЕСТВО ВОЗДУХА', value: '142 AQI', subtitle: 'Нездоровый', borderColor: 'border-t-amber-400', textColor: 'text-amber-500', image: 'https://picsum.photos/seed/factory/800/600' },
  { title: 'ИНДЕКС ЗДОРОВЬЯ', value: '92/100', subtitle: 'Стабильно', borderColor: 'border-t-emerald-500', textColor: 'text-emerald-600', image: 'https://picsum.photos/seed/health/800/600' },
  { title: 'АКТИВНЫЕ АЛЕРТЫ', value: '3', subtitle: 'Требуют внимания', borderColor: 'border-t-orange-500', textColor: 'text-orange-600' },
])

const chart1Data = ref([45, 60, 30, 85, 90, 70, 50, 65, 80, 40, 55, 75, 45, 60, 30, 85, 90, 70, 50, 65, 80, 40, 55, 75])
</script>

<style scoped>
/* Optional grid background or subtle styling */
</style>