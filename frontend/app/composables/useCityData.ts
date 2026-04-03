import { ref, onMounted, onUnmounted } from 'vue'

export interface CityMetrics {
  traffic_index: number
  air_quality_index: number
  noise_level: number
  pedestrian_flow: number
  active_incidents: number
}

export interface CityInsights {
  level: string
  level_ru: string
  city_health_score: number
  composite_score: number
  problems: string[]
  actions: string[]
  causal_link: string | null
  is_simulation: boolean
}

export interface CityHistoryPoint {
  timestamp: number
  traffic_index: number
  air_quality_index: number
  noise_level: number
}

export interface CityScenario {
  label: string
  prediction: string
}

export interface CitySnapshot {
  timestamp: number
  metrics: CityMetrics
  insights: CityInsights
  llm_recommendation: string
  history: CityHistoryPoint[]
}

export const useCityData = () => {
  const config = useRuntimeConfig()
  const data = ref<CitySnapshot | null>(null)
  const scenarios = ref<Record<string, CityScenario>>({})
  const isConnected = ref(false)
  const lastError = ref<string | null>(null)
  
  let ws: WebSocket | null = null

  const fetchData = async () => {
    try {
      const [dataRes, scenariosRes] = await Promise.all([
        fetch(`${config.public.apiUrl}/api/city-state`),
        fetch(`${config.public.apiUrl}/api/scenarios`)
      ])
      
      if (!dataRes.ok) throw new Error('Failed to fetch city state')
      data.value = await dataRes.json()
      
      if (scenariosRes.ok) {
        scenarios.value = await scenariosRes.json()
      }
    } catch (err: any) {
      lastError.value = err.message
      console.error('Error fetching city data:', err)
    }
  }

  const connectWs = () => {
    if (ws) ws.close()

    ws = new WebSocket(config.public.wsUrl)

    ws.onopen = () => {
      isConnected.value = true
      lastError.value = null
    }

    ws.onmessage = (event) => {
      try {
        const payload = JSON.parse(event.data)
        data.value = payload
      } catch (err) {
        console.error('Error parsing WS message:', err)
      }
    }

    ws.onerror = (err) => {
      console.error('WS Error:', err)
      isConnected.value = false
    }

    ws.onclose = () => {
      isConnected.value = false
      // Reconnect after 3 seconds
      setTimeout(connectWs, 3000)
    }
  }

  onMounted(() => {
    fetchData()
    connectWs()
  })

  onUnmounted(() => {
    if (ws) {
      ws.onclose = null // Prevent reconnect loop
      ws.close()
    }
  })

  return {
    data,
    scenarios,
    isConnected,
    lastError,
    refresh: fetchData
  }
}
