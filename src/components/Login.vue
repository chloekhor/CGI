<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-red-500">Login</h2>
      
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
                class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
                placeholder="••••••••"
              />
              <!-- Show/Hide Password Button -->
              <button
                type="button"
                @click="togglePasswordVisibility"
                class="absolute inset-y-0 right-0 px-4 py-2 text-sm font-medium text-red-500 focus:outline-none"
              >
                {{ showPassword ? 'Hide' : 'Show' }}
              </button>
            </div>
          </div>

          <!-- Forgot Password Link -->
          <div class="text-right">
            <router-link to="/forgot-password" class="text-red-600 hover:text-red-500 text-sm font-medium">
              Forgot your password?
            </router-link>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Log In
          </button>
        </div>
      </form>

      <!-- Sign Up Link -->
      <div class="text-center mt-4">
        <span class="text-gray-700">Don’t have an account?</span>
        <router-link to="/register" class="text-red-600 hover:text-red-500 font-medium">Sign Up</router-link>
      </div>
    </div>
  </div>
</template>

<script>
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
    login() {
      if (!this.email || !this.password) {
        this.errorMessage = 'Please fill in all the fields.';
        return;
      }

      // 模拟登录逻辑
      console.log({
        email: this.email,
        password: this.password,
      });

      // 重置错误信息
      this.errorMessage = '';
      
      // 成功后重定向
      this.$router.push('/login-otp');
    },
  },
};
</script>

<style scoped>
</style>
