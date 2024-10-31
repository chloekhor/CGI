<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-gray-100">
    <div class="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
      <h2 class="text-center text-2xl font-bold text-red-500">Reset Password</h2>

      <!-- Error Message -->
      <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
        {{ errorMessage }}
      </div>

      <form @submit.prevent="submitNewPassword" class="mt-8 space-y-6">
        <div class="rounded-md shadow-sm space-y-4">
          <!-- New Password Input -->
          <div>
            <label for="newPassword" class="block text-sm font-medium text-gray-700">New Password</label>
            <div class="relative">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="newPassword"
                id="newPassword"
                required
                class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
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

          <!-- Confirm New Password Input -->
          <div>
            <label for="confirmNewPassword" class="block text-sm font-medium text-gray-700">Confirm New Password</label>
            <input
              :type="showConfirmPassword ? 'text' : 'password'"
              v-model="confirmNewPassword"
              id="confirmNewPassword"
              required
              class="appearance-none rounded-lg relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm"
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
            Reset Password
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newPassword: '',
      confirmNewPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      passwordError: false, // 控制是否显示错误状态
      errorMessage: '', // 用于存储错误信息
    };
  },
  computed: {
    passwordLengthValid() {
      return this.newPassword.length >= 8;
    },
    hasUppercase() {
      return /[A-Z]/.test(this.newPassword);
    },
    hasLowercase() {
      return /[a-z]/.test(this.newPassword);
    },
    hasDigit() {
      return /\d/.test(this.newPassword);
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
    submitNewPassword() {
      // 检查密码是否符合要求
      if (!this.isPasswordValid) {
        this.passwordError = true;
        this.errorMessage = 'Password must meet the requirements.';
        return;
      }

      // 检查确认密码是否匹配
      if (this.newPassword !== this.confirmNewPassword) {
        this.errorMessage = 'Passwords do not match!';
        return;
      }

      // 模拟提交新密码的逻辑
      console.log({
        newPassword: this.newPassword,
      });

      // 重置错误标记和错误信息
      this.passwordError = false;
      this.errorMessage = '';

      // 模拟成功重置后重定向到首页
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
</style>
