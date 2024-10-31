<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-red-500">Register</h2>

      <!-- Error Message -->
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="register" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm space-y-4">
          <!-- Name Input -->
          <div>
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input
              v-model="name"
              id="name"
              type="text"
              required
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
              placeholder="Your Name"
            />
          </div>

          <!-- Email Input -->
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

          <!-- Password Input -->
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
              <!-- Show Password Button -->
              <button
                type="button"
                @click="togglePasswordVisibility"
                class="absolute inset-y-0 right-0 px-4 py-2 text-sm font-medium text-red-500 focus:outline-none"
              >
                {{ showPassword ? 'Hide' : 'Show' }}
              </button>
            </div>

            <!-- Password Requirements -->
            <div :class="passwordError ? 'text-red-500' : 'text-gray-600'" class="text-sm mt-2">
              Min. 8 characters, 1 lowercase, 1 uppercase, and 1 number
            </div>
          </div>

          <!-- Confirm Password Input -->
          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-gray-700">Confirm Password</label>
            <input
              :type="showConfirmPassword ? 'text' : 'password'"
              v-model="confirmPassword"
              id="confirmPassword"
              required
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border"
              :class="passwordError ? 'border-red-500' : 'border-gray-300'"
              placeholder="••••••••"
            />
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Register
          </button>
        </div>
      </form>

      <!-- Log In Link -->
      <div class="text-center mt-4">
        <span class="text-gray-700">Already have an account?</span>
        <router-link to="/" class="text-red-600 hover:text-red-500 font-medium">Log In</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      passwordError: false, // 控制是否显示错误状态
      errorMessage: '', // 用于存储错误信息
    };
  },
  computed: {
    passwordLengthValid() {
      return this.password.length >= 8;
    },
    hasUppercase() {
      return /[A-Z]/.test(this.password);
    },
    hasLowercase() {
      return /[a-z]/.test(this.password);
    },
    hasDigit() {
      return /\d/.test(this.password);
    },
    isPasswordValid() {
      return (
        this.passwordLengthValid &&
        this.hasUppercase &&
        this.hasLowercase &&
        this.hasDigit
      );
    },
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    toggleConfirmPasswordVisibility() {
      this.showConfirmPassword = !this.showConfirmPassword;
    },
    register() {
      // 检查密码是否符合要求
      if (!this.isPasswordValid) {
        this.passwordError = true; // 设置密码错误标记
        this.errorMessage = 'Password must meet the requirements.';
        return;
      }

      // 检查确认密码是否匹配
      if (this.password !== this.confirmPassword) {
        this.errorMessage = 'Passwords do not match!';
        return;
      }

      // 处理注册逻辑
      console.log({
        name: this.name,
        email: this.email,
        password: this.password,
      });

      // 重置错误标记和错误信息
      this.passwordError = false;
      this.errorMessage = '';

      // 验证通过后，重定向到 /
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
</style>
