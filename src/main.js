import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css';
import router from './router'; 

import axios from "axios";

axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app');


const formData = new FormData();
formData.append('file', selectedFile);

axios.post('https://localhost:8000/api/upload/', formData, {
    headers: {
        'Content-Type': 'multipart/form-data',
    },
    withCredentials: true  // 确保 cookies/session 可以传输
}).then(response => {
    console.log(response.data);
}).catch(error => {
    console.error(error.response?.data || error.message);
});

