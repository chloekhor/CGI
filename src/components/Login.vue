<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-[#FF7823]">Login</h2>
      
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
import api from '@/api/readApi';

export default {
  data() {
    return {
      email: '',
      password: '',
      showPassword: false, 
      errorMessage: '', 
    };
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    async login() {
      console.log(this.email);
      console.log(this.password);
      this.errorMessage = '';
      try {
        const response = await api.post('login/', {
          email: this.email,
          password: this.password
        }, { withCredentials: true }); // Ensures session cookies are sent

        if (response.data.user_id) {
          console.log("Login successful:", response.data);
          localStorage.setItem("user_id", response.data.user_id);
          this.$router.push('/home');
        }
      } catch (error) {
        if (error.response) {
      if (error.response.status === 401 || error.response.status === 403) {
        this.errorMessage = 'Invalid email or password.';
      } else {
        this.errorMessage = error.response.data?.error || 'Login failed, please try again.';
      }
    } else {
      this.errorMessage = 'Network error, please try again later.';
    }
      }
    }


  }
};
</script>
