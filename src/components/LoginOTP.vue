<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-[#FF7823]">Login</h2>
      <p class="text-center text-gray-600">We have sent an OTP to your email address. Please enter it below to verify your login.</p>

      <!-- Error Message -->
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="submitOTP" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm space-y-4">
          <div>
            <label for="otp" class="block text-sm font-medium text-gray-700">OTP</label>
            <!-- Flex container to position the input and the button side by side -->
            <div class="flex items-center">
              <input
                v-model="otp"
                id="otp"
                type="text"
                required
                maxlength="6"
                class="appearance-none rounded-l-lg block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
                placeholder="Enter 6-digit OTP"
              />
              <!-- Resend OTP Button next to the input field -->
              <button
                type="button"
                @click="sendOTPEmail"
                class="px-4 py-2 text-sm font-medium text-white bg-[#FF7823] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 rounded-r-lg border border-red-500"
              >
                Resend
              </button>
            </div>
          </div>
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#FF7823] hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Verify OTP
          </button>
        </div>
      </form>

      <!-- Login with another account -->
      <div class="text-center mt-4">
        <router-link to="/login" class="text-orange-600 hover:text-orange-500 font-medium">
          Login with another account
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api/readApi'; // ✅ 确保引入 API 交互模块
export default {
  data() {
    return {
      otp: '',
      errorMessage: '',
      isResendDisabled: false, // ✅ 1分钟内不能点击
      email: ''
    };
  },
  created() {
    this.email = this.$route.query.email || ''; // ✅ 确保 email 存在
  },
  methods: {
    async sendOTPEmail() {
      if (this.isResendDisabled) return;

      this.isResendDisabled = true; // ✅ 防止用户短时间内重复点击
      setTimeout(() => {
        this.isResendDisabled = false;
      }, 60000); // 60秒后解除按钮限制

      try {
          const response = await axios.post('https://localhost:8000/api/resend-otp/', {
            email: this.email
      });
        console.log("OTP resent successfully:", response.data);
      } catch (error) {
        console.error("Error resending OTP:", error);
        this.errorMessage = "Failed to resend OTP. Try again later.";
      }
    },
    async submitOTP() {
      try {
        const response = await api.post('verify-otp/', {
          email: this.email,
          otp: this.otp
        });

        console.log("OTP verified, access granted:", response.data);
        // ✅ 这里假设服务器返回一个 access_token，存入 localStorage
        localStorage.setItem("access_token", response.data.access_token);
        // ✅ OTP 正确，跳转到首页
        this.$router.push('/home');

} catch (error) {
console.error("OTP verification failed:", error);
this.errorMessage = "Invalid OTP or too many attempts.";
}
}
}
};
</script>
