<template>
    <div class="p-6">
        <Navbar :logo="logo" />

        <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
            {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="text-center py-2 px-4 text-sm font-medium bg-green-100 text-white-600 rounded-md">
            {{ successMessage }}
        </div>


        <div id="pfp"></div>
        <div style = "text-align: center" v-for="item in profile" :key="item.id">{{ item.username }}</div>

        <!-- Show Current Data -->
        <form v-for="item in profile" :key="item.id" class="border border-black p-4 mt-4 rounded-md w-100">
            <div v-if="!isEditing">
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
            <input v-model="username" type="text" id="uname" name="uname" class="w-full border rounded-md p-2 mt-1 mb-3">

            <label for="email" class="block font-semibold">Email:</label>
            <input v-model="email" type="text" id="email" name="email" class="w-full border rounded-md p-2 mt-1 mb-3">

            <!-- Password -->
            <div>
                <label for="password" class="block font-semibold">Password</label>
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
                    required
                    class="appearance-none rounded-lg relative block w-full px-3 py-2 border"
                    :class="passwordError ? 'border-red-500' : 'border-gray-300'"
                    placeholder="••••••••"
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
import api from '@/api';


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
            // username: "API...Username",
            // email: "API...Email",
            // password: "",
            // confirmPassword: "",
            isLoading: false,
            showPassword: false,
            showConfirmPassword: false,
            errorMessage: '',
            successMessage: ''
        };
    },

    created() {
        this.fetchProfile();
    },

    methods: {
        toggleEdit() {
            this.isEditing = !this.isEditing;
        },
        togglePasswordVisibility() {
            this.showPassword = !this.showPassword;
        },
        toggleConfirmPasswordVisibility() {
            this.showConfirmPassword = !this.showConfirmPassword;
        },
        saveChanges() {
            this.isLoading = true; // Set loading before the check

            if (this.password !== this.confirmPassword) {
                setTimeout(() => { 
                    this.isLoading = false; // Stop loading after showing alert
                    this.errorMessage = 'Password Does Not Match';
                }, 2000);
                return;
            }

            setTimeout(() => {
                this.successMessage = 'Changes Saved';
                console.log("Saving changes:", {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                });

                this.isEditing = false; // Switch back to view mode
                this.isLoading = false;
            }, 2000);   
        },
        fetchProfile() {
            api.get('profile/')
                .then(response => {
                    this.profile = response.data.map(item => ({
                        id: item.id || '-',
                        username: item.username || '-',
                        email: item.email || 'N/A',
                        password: item.password ?? 'No Result',

                        
                    }));

                    // this.$nextTick(() => this.initDataTable());
                })
                .catch(error => {
                    console.error('Error Fetching History: ', error);
                });
        }
    }
}
</script>
