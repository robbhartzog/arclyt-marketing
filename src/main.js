import { createApp } from 'vue'
import { createGtag } from 'vue-gtag'
import App from './App.vue'
import './styles/main.css'

createApp(App)
  .use(createGtag({ tagId: 'G-0QDJTQPRZK' }))
  .mount('#app')
