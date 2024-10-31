import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/components/Home.vue'; 
import Login from '@/components/Login.vue'; 
import Register from '@/components/Register.vue'; 
import ForgotPassword from '@/components/ForgotPassword.vue'; 
import ResetPassword from '@/components/ResetPassword.vue'; 
import LoginOTP from '@/components/LoginOTP.vue'; 

const routes = [
  {
    path: '/',
    redirect: '/login', // 默认重定向到登录页面
  },
  {
    path: '/login',
    name: 'Login',
    component: Login, // 默认页面
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword, // 默认页面
  },
  {
    path: '/register',
    name: 'Register',
    component: Register, // 默认页面
  },
  {
    path: '/home',
    name: 'Home',
    component: Home, // 默认页面
  },
  {
    path: '/login-otp',
    name: 'LoginOTP',
    component: LoginOTP, // 默认页面
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: ResetPassword, // 默认页面
  },


];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
