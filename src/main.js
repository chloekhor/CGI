import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css';
import router from './router'; 



createApp(App).use(router).mount('#app');


// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router'
// import './assets/tailwind.css'

// // Import necessary BootstrapVue components
// import { BButton, BSidebar, BImg } from 'bootstrap-vue-3'

// // Import Bootstrap's CSS
// import 'bootstrap/dist/css/bootstrap.min.css'

// // Create the Vue app
// const app = createApp(App)

// // Use the required components
// app.component('BButton', BButton)
// app.component('BSidebar', BSidebar)
// app.component('BImg', BImg)

// // Use the router and mount the app
// app.use(router).mount('#app')
