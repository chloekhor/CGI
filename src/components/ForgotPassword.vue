<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <!-- 【新增】成功提示消息 -->
      <div v-if="message" class="text-center py-2 px-4 text-sm font-medium bg-green-100 text-green-600 rounded-md">
        {{ message }}
      </div>
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>
      <h2 class="text-center text-2xl font-bold text-[#FF7823]">Forgot Password</h2>
      <p class="text-center text-gray-600">Enter your email address to receive a password reset link.</p>

      <form @submit.prevent="submitEmail" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input
              v-model="email"
              id="email"
              type="email"
              required
              @input="validateEmail" 
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:z-10 sm:text-sm"
              :class="passwordError ? 'border-red-500' : 'border-gray-300'"
              placeholder="you@example.com"
            />
            <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ errorMessage }}</p>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#FF7823] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Send Reset Link
          </button>
        </div>
      </form>

      <div class="text-center mt-4">
        <router-link to="/login" class="text-[#FF7823] hover:text-orange-500 font-medium">Back to Login</router-link>
      </div>
    </div>
  </div>
</template>

<script>

// 【新增】：导入 axios，用于发送 HTTP 请求
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      passwordError: false, // Controls if error is displayed
      errorMessage: '', // Stores error message
      message: '' // 【新增】：存储成功提示信息
    };
  },
  methods: {
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.email)) {
        this.errorMessage = 'Invalid email format.';
        this.passwordError = true;
      } else {
        this.passwordError = false;
        this.errorMessage = '';
      }
    },
    
    submitEmail() {
      this.validateEmail(); 
      
      if (this.passwordError) {
        return; 
      }

    // 【新增】：使用 axios 发送 POST 请求到后端 forgot_password API
    axios.post('https://localhost:8000/api/forgot-password/', { email: this.email })
        .then(response => {
          // 【修改】：显示后端返回的成功消息
          this.message = response.data.message || "Reset email sent. Please check your inbox.";
          this.errorMessage = '';
        })
        .catch(error => {
          // 【修改】：处理并显示错误信息
          if (error.response && error.response.data && error.response.data.error) {
            this.errorMessage = error.response.data.error;
          } else {
            this.errorMessage = "An error occurred while sending the reset link.";
          }
          this.message = '';
        });



      console.log('Password reset link sent to:', this.email);
    },
  },
};
</script>


