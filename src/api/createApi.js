import axios from 'axios';

//const api = axios.create({
  //  baseURL: 'http://127.0.0.1:8000/createApi/api/', // Base URL for your Django API
//});

const api = axios.create({
    baseURL: 'https://127.0.0.1:8000/createApi/api/',
});

export default api;