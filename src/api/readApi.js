import axios from 'axios';

const api = axios.create({
    baseURL: 'https://127.0.0.1:8000/readApi/api/', // Base URL for your Django API
    withCredentials: true,
    headers: { 'Content-Type': 'application/json' },});

export default api;