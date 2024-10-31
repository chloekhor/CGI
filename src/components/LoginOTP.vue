<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-red-500">Login</h2>
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
                class="px-4 py-2 text-sm font-medium text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 rounded-r-lg border border-red-500"
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
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
          >
            Verify OTP
          </button>
        </div>
      </form>

      <!-- Login with another account -->
      <div class="text-center mt-4">
        <router-link to="/login" class="text-red-600 hover:text-red-500 font-medium">
          Login with another account
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      otp: '',
      generatedOTP: '', // 保存生成的 OTP
      errorMessage: '', // 用于存储错误信息
    };
  },
  methods: {
    sendOTPEmail() {
      // 生成随机的6位数OTP并展示给用户（模拟通过电子邮件发送）
      this.generatedOTP = Math.floor(100000 + Math.random() * 900000).toString();
      alert('OTP sent to your email: ' + this.generatedOTP); // 模拟显示发送的OTP
    },
    submitOTP() {
      // 验证用户输入的OTP是否与发送的OTP匹配
      if (this.otp === this.generatedOTP) {
        this.errorMessage = ''; // 验证通过，清除错误信息
        alert('OTP Verified. Login successful!');
        this.$router.push('/home'); // 跳转到首页
      } else {
        this.errorMessage = 'Invalid OTP. Please try again.'; // OTP 错误，设置错误信息
      }
    },
  },
  mounted() {
    // 在页面加载时发送OTP
    this.sendOTPEmail();
  },
};
</script>

<style scoped>
</style>
