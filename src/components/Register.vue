<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-[#FF7823]">Register</h2>

      <!-- Error Message -->
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>
      <form @submit.prevent="registerUser" class="mt-8 space-y-6">
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
                class="absolute inset-y-0 right-0 px-4 py-2 text-sm font-medium text-[#FF7823] focus:outline-none"
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
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#FF7823] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Register
          </button>
        </div>
      </form>

      <!-- Log In Link -->
      <div class="text-center mt-4">
        <span class="text-gray-700">Already have an account?</span>
        <router-link to="/" class="text-[#FF7823] hover:text-orange-500 font-medium">Log In</router-link>
      </div>
    </div>
  </div>
  <TransitionRoot appear :show="isModalOpen" as="template">
  <Dialog as="div" static @close="closeModal" class="fixed inset-0 z-50 flex items-center justify-center">
    <div class="fixed inset-0 bg-black bg-opacity-30"></div>
    <div class="relative bg-white p-6 rounded-lg shadow-lg max-w-md w-full mx-auto">
      <div class="mt-4 text-center text-lg font-semibold text-gray-700">
        <p>Registration successful!</p>  
      </div>

      <div class="mt-4 flex justify-end">
      </div>
    </div>
  </Dialog>
</TransitionRoot>


</template>

<script>
import api from '@/api/createApi';
import { Dialog, TransitionRoot } from '@headlessui/vue';


export default {
  components: {
    Dialog,
    TransitionRoot
  },
  data() {
    return {
      name: '',
      email: '',
      password: '',
      confirmPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      passwordError: false,
      errorMessage: '',
      isModalOpen: false,  // Add isModalOpen to control modal visibility
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

    async registerUser() {
      this.errorMessage = '';
      this.passwordError = false; 

      if (this.password !== this.confirmPassword) {
        this.errorMessage = "Passwords do not match.";
        this.passwordError = true;
        return;
      }

      if (!this.isPasswordValid) {
        this.errorMessage = "Password must be at least 8 characters, with 1 uppercase letter, 1 lowercase letter, and 1 number.";
        this.passwordError = true;
        return;
      }

      try {
        const response = await api.post('/register/', {
          name: this.name,
          email: this.email,
          password: this.password
        });

        console.log("User registered:", response.data);
        this.isModalOpen = true;

        // Wait for 2 seconds before redirecting to login
        setTimeout(() => {
          this.goToLogin();
        }, 2000);

      } catch (error) {
        console.error("Registration error:", error.response?.data || error.message);
        this.errorMessage = error.response?.data?.error || "An error occurred";
      }

    },
    goToLogin() {
      this.closeModal(); 
      this.$router.push({ path: '/login' }); 

    },

    closeModal() {
      this.isModalOpen = false;
    },
  },
};
</script>

<style scoped>
</style>





