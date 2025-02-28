<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-[#FF7823]">Login</h2>
      
      <!-- Error Message -->
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="login" class="mt-8 space-y-6">
        <div class="rounded-md space-y-4">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
            <input
              v-model="email"
              id="email"
              type="email"
              required
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
              placeholder="you@example.com"
            />
          </div>

          <!-- Password Input with Show/Hide -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <div class="relative">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="password"
                id="password"
                required
                class="appearance-none rounded-lg relative block w-full px-3 py-2 border"
                :class="passwordError ? 'border-red-500' : 'border-gray-300'"
                placeholder="••••••••"
              />
              <!-- Show/Hide Password Button -->
              <button
                type="button"
                @click="togglePasswordVisibility"
                class="absolute inset-y-0 right-0 px-4 py-2 text-sm font-medium text-[#FF7823] focus:outline-none"
              >
                {{ showPassword ? 'Hide' : 'Show' }}
              </button>
            </div>
          </div>

          <!-- Forgot Password Link -->
          <div class="text-right">
            <router-link to="/forgot-password" class="text-[#FF7823] hover:text-red-500 text-sm font-medium">
              Forgot your password?
            </router-link>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#FF7823] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Log In
          </button>
        </div>
      </form>

      <!-- Sign Up Link -->
      <div class="text-center mt-4">
        <span class="text-gray-700">Don’t have an account? </span>
        <router-link to="/register" class="text-[#FF7823] hover:text-red-500 font-medium">Sign Up</router-link>
      </div>
    </div>
  </div>
</template>






<script>
import { loginUser } from '@/api.js';



export default {
  data() {
    return {
      email: '',
      password: '',
      showPassword: false, // 控制密码是否显示
      errorMessage: '', // 用于存储错误信息
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword; // 切换密码显示状态
    },
    async login() {
      if (!this.email || !this.password) {
        this.errorMessage = 'Please fill in all the fields.';
        return;
      }

      try {  //这边下面都是新增的
      // 新增：调用API函数loginUser，将用户输入的数据传递给后端
      const response = await loginUser({
        email: this.email,
        password: this.password
      });
      console.log ('Login response:', response.data);  // 新增：打印后端返回的数据，方便调试
      // 新增：登录成功后重定向到OTP验证页面
      this.$router.push('/login-otp');
    } catch (error) {
      // 新增：捕获错误并显示错误信息
      this.errorMessage = error.response?.data?.error || 'Login failed. Please try again.';
    }
  },
},
};
</script>

<style scoped>
</style>


//Timz, these is previous version before connect with backend, Just put here to refer, can delete if u think no need these anymore
// 模拟登录逻辑
      //console.log({  //这里说这个.有问题
        //email: this.email,
        //password: this.password,
      });  //这里说这个;有问题

      // 重置错误信息
      //this.errorMessage = '';  //这里说这个.和;有问题
      
      // 成功后重定向
      //this.$router.push('/login-otp');  //这里说这个.和;有问题
    //},  //这里说这个,有问题
  //},  //这里说这个}和,有问题
//};//这里说这个}有问题
