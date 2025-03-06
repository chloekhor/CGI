<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
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
              :class="emailError ? 'border-red-500' : 'border-gray-300'"
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
              placeholder="you@example.com"
              @input="validateEmail"
            />
            <p v-if="emailError" class="text-red-500 text-sm mt-1">Invalid email format</p>
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
export default {
  data() {
    return {
      email: "",
      emailError: false
    };
  },
  methods: {
    submitEmail() {
      // 处理提交逻辑，发送电子邮件
      console.log('Password reset link sent to:', this.email);
      // 可以在这里加入请求，发送到API处理找回密码
    },
    validateEmail() {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      this.emailError = !emailPattern.test(this.email);
    }
  },
};
</script>

<style scoped>
</style>
