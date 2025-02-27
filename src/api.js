import axios from 'axios';

// Django API 服务器地址（确保 Django 运行在这个端口）
// const API_URL = "http://127.0.0.1:8000";

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/readApi/api/', // Base URL for your Django API
  headers: {
    "Content-Type": "application/json",
  },
});

// 发送注册请求
export const registerUser = async (userData) => {
  return api.post("/register/", userData);
};

// 发送登录请求
export const loginUser = async (credentials) => {
  return api.post("/login/", credentials);
};

export default api;