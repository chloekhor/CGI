<template>
  <!-- Sidebar -->
  <div
      :class="{'-translate-x-full': !isOpen}"
      
      class="bg-white shadow-2xl text-black h-screen fixed top-0 left-0 transition-transform duration-300 ease-in-out w-64 z-30"
    >

      <div class="flex justify-between p-4">
        <img class="h-8" :src="logo" alt="Logo" @click="returnHome">
        <h2 v-if="isOpen" class="text-lg font-semibold">CGI Matrix</h2>
        <button @click="toggleSidebar" class="text-xl">
          &times;
        </button>
      </div>
        <!-- Top Menu -->
      <ul v-if="isOpen" class="space-y-4 px-4">
        <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-house"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
          <a @click="returnHome">Home</a>
        </li>
        <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-history"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg>
          <a @click="historyPage">History</a>
        </li>
      </ul>
        <!-- Bottom Menu -->
      <div class="absolute bottom-0 w-full p-4 flex flex-col justify-between h-32">
        <ul class="space-y-4">
          <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            <a @click="toProfile">Profile</a>
          </li>
        </ul>

        <ul class="space-y-4">
          <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-log-out"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/></svg>
            <a @click="toLogin">Log Out</a>
          </li>
        </ul>
      </div>

  </div>
    
    <!-- Hamburger Menu -->
  <button
    v-if="!isOpen"
    @click="toggleSidebar"
    class="fixed top-4 left-4 z-40 text-gray-800 bg-white p-2 rounded shadow-lg"
  >
    &#9776;
  </button>

  <Loader :isLoading="isLoading" />
</template>

<script>
import logo from '../images/logo.png';
import Loader from '../fragments/loader.vue';

export default {
  components: {
    Loader
  },
  data() {
    return {
      logo,
      isOpen: false, // For Sidebar open/close state
      isLoading: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isOpen = !this.isOpen;
    },

    returnHome() {

      this.isLoading = true; // Show loader

      setTimeout(() => {
          this.isLoading = false; 
          this.$router.push('/home'); 
      }, 2000); 
    },

    historyPage() {
      this.isLoading = true; 

      setTimeout(() => {
        this.isLoading = false; 
        this.$router.push('/home/history');
      }, 2000)
    },

    planPage() {
      this.isLoading = true; 

      setTimeout(() => {
        this.isLoading = false; 
        this.$router.push('/home/Plan');
      }, 2000)
    },

    toProfile() {
        this.isLoading = true; 

        setTimeout(() => {
            this.isLoading = false; 
            this.$router.push('/home/profile'); 
        }, 2000); 
    },

    toLogin() {
      this.isLoading = true; 

      setTimeout(() => {
        this.isLoading = false;
        this.$router.push('/login');
      }, 2000);
    }

  },
};
</script>

