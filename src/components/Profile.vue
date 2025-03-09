<template>
    <div class="p-6">
        <Navbar :logo="logo" />

        <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
            {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="text-center py-2 px-4 text-sm font-medium bg-green-100 text-white-600 rounded-md">
            {{ successMessage }}
        </div>

        <div v-if="!isEditing" class="w-full border rounded-lg p-4 bg-gray-100 text-gray-700 shadow-md">
            <div class="text-center">
                <p class="text-sm text-gray-500">Logged in as</p>
                <div v-for="item in profile" :key="item.id" class="text-lg font-semibold text-gray-900">
                    {{ item.username }}
                </div>
            </div>
        </div>



        <!-- Show Current Data -->
        <form v-for="item in profile" :key="item.id">
            <div v-if="!isEditing" class="border border-black p-4 mt-4 rounded-md w-100">
                <label for="uname" class="block font-semibold">Username:</label>
                <div id="uname" name="uname" class="w-full border rounded-md p-2 mb-2 bg-gray-100 text-gray-700">
                    {{ item.username }}
                </div>

                <label for="email" class="block font-semibold">Email:</label>
                <div id="email" name="email" class="w-full border rounded-md p-2 mb-2 bg-gray-100 text-gray-700">
                    {{ item.email }}
                </div>

                <label for="password" class="block font-semibold">Password:</label>
                <div id="password" name="password" class="w-full border rounded-md p-2 mb-2 bg-gray-100 text-gray-700">
                    ••••••••
                </div>

                <div class="flex justify-center">
                    <button @click="toggleEdit" type="button" class="bg-orange-500 text-white font-bold py-2 px-4 rounded-xl hover:bg-orange-600 w-full max-w-[600px] text-center">
                        Edit
                    </button>
                </div>
            </div>
        </form>

        <!-- Edit Profile -->
        <form v-if="isEditing" @submit.prevent="saveChanges" class="border border-black p-4 mt-4 rounded-md w-100">
            <label for="uname" class="block font-semibold">Username:</label>
            <input v-model="username" type="text" id="uname" name="uname" class="w-full border rounded-md p-2 mt-1 mb-3" :class="passwordError ? 'border-red-500' : 'border-gray-300'">

            <label for="email" class="block font-semibold">Email:</label>
            <input v-model="email" type="text" id="email" name="email" class="w-full border rounded-md p-2 mt-1 mb-3" :class="passwordError ? 'border-red-500' : 'border-gray-300'">

            <!-- Password -->
            <div>
                <label for="password" class="block font-semibold">Password</label>
                <div class="relative">
                    <input
                        :type="showPassword ? 'text' : 'password'"
                        v-model="password"
                        id="password"
                        class="appearance-none rounded-lg relative block w-full px-3 py-2 border"
                        :class="passwordError ? 'border-red-500' : 'border-gray-300'"
                        placeholder="leave it blank if no change"
                    />
                    <button
                        type="button"
                        @click="togglePasswordVisibility"
                        class="absolute inset-y-0 right-0 px-4 py-2 text-sm font-medium text-red-500 focus:outline-none"
                    >
                        {{ showPassword ? 'Hide' : 'Show' }}
                    </button>
                </div>
                <div :class="passwordError ? 'text-red-500' : 'text-gray-600'" class="text-sm mt-2">
                    Min. 8 characters, 1 lowercase, 1 uppercase, and 1 number
                </div>
            </div>

            <br>

            <!-- Confirm Password -->
            <div>
                <label for="confirmPassword" class="block font-semibold">Confirm Password</label>
                <input
                    :type="showConfirmPassword ? 'text' : 'password'"
                    v-model="confirmPassword"
                    id="confirmPassword"
                    class="appearance-none rounded-lg relative block w-full px-3 py-2 border"
                    :class="passwordError ? 'border-red-500' : 'border-gray-300'"
                    placeholder="leave it blank if no password change"
                />
            </div>
            

            <div class="flex justify-center mt-4">
                <button type="submit" class="bg-orange-500 text-white font-bold py-2 px-4 rounded-xl hover:bg-green-600 w-full max-w-[600px] text-center">
                    Save
                </button>
                <button @click="toggleEdit" type="button" class="ml-4 bg-gray-400 text-white font-bold py-2 px-4 rounded-xl hover:bg-gray-500 w-full max-w-[600px] text-center">
                    Cancel
                </button>
            </div>
        </form>
        <Loader :isLoading="isLoading" />
    </div>
</template>

<script>
import Navbar from '../fragments/Navbar.vue';
import Loader from '../fragments/loader.vue';
import api from '@/api/readApi';


export default {
    name: 'Result',
    components: {
        Navbar,
        Loader,
    },
    data() {
        return {
            profile: [],
            isEditing: false,
            isLoading: false,
            showPassword: false,
            showConfirmPassword: false,
            errorMessage: '',
            successMessage: '',
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
            passwordError: false,
        };
    },

    created() {
        this.fetchProfile();
    },

    methods: {
        toggleEdit() {
            if (this.profile.length > 0) {
                const currentUser = this.profile[0]; 
                this.username = currentUser.username || '';
                this.email = currentUser.email || '';
                this.password = '';
                this.confirmPassword = '';
            }
            this.isEditing = !this.isEditing;
        },
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
        },
        toggleConfirmPasswordVisibility() {
            this.showConfirmPassword = !this.showConfirmPassword;
        },
        saveChanges() {
            this.isLoading = true; // Show loading indicator
            this.errorMessage = ''; // Clear previous errors
            const user_id = localStorage.getItem('user_id');

            // Validate name and email
            if (!this.username.trim()) {
                this.isLoading = false;
                this.errorMessage = 'Name cannot be empty.';
                this.passwordError = true;
                return;
            }

            if (!this.email.trim()) {
                this.isLoading = false;
                this.errorMessage = 'Email cannot be empty.';
                this.passwordError = true;
                return;
            }

            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(this.email)) {
                this.isLoading = false;
                this.errorMessage = 'Invalid email format.';
                this.passwordError = true;

                return;
            }

            // Validate passwords (if provided)
            if (this.password) {
                if (this.password !== this.confirmPassword) {
                    this.isLoading = false;
                    this.errorMessage = 'Password does not match.';
                    this.passwordError = true;
                    return;
                }

                const passwordLengthValid = this.password.length >= 8;
                const hasUppercase = /[A-Z]/.test(this.password);
                const hasLowercase = /[a-z]/.test(this.password);
                const hasDigit = /\d/.test(this.password);

                if (!(passwordLengthValid && hasUppercase && hasLowercase && hasDigit)) {
                    this.isLoading = false;
                    this.errorMessage = 'Password must be at least 8 characters long and contain at least 1 uppercase letter, 1 lowercase letter, and 1 number.';
                    return;
                }
            }

            // Prepare data for update
            const updateData = {
                user_id: user_id,
                name: this.username,
                email: this.email,
                password: this.password || undefined, // Avoid sending empty password
            };

            // Send request to update profile
            api.post('profile/update/', updateData)
                .then(() => {
                    this.successMessage = 'Profile updated successfully!';
                    this.isEditing = false;
                    this.fetchProfile();
                })
                .catch(error => {
                    this.errorMessage = 'Failed to update profile.';

                    if (error.response) {
                        console.error("⚠️ Server Response:", error.response.data);
                    } else {
                        console.error("❌ Network or other error:", error.message);
                    }
                })
                .finally(() => {
                    this.isLoading = false;
                });

            // Show success message for 2 seconds
            setTimeout(() => {
                this.successMessage = 'Changes Saved';
                console.log("Saving changes:", {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                });

                this.isEditing = false;
                this.isLoading = false;

                setTimeout(() => {
                    this.successMessage = '';
                }, 2000);
            }, 2000);
        },

        fetchProfile() {
            api.get('profile/')
                .then(response => {
                    console.log("Fetched Data:", response.data);
                    this.isLoading = true;
                    console.log("Fetched Data:", response.data);
                    console.log("Cookies in Response:", document.cookie);
                    this.profile = response.data.map(item => ({
                        id: item.id || '-',
                        username: item.name || '-',
                        email: item.email || 'N/A',
                        password: item.password ?? 'No Result',
                    }));

                    this.isLoading = false;
                })
                .catch(error => {
                    console.error('Error Fetching History: ', error);
                });
        }
    }
}
</script>
