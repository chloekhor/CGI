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
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 16 16" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5z"/>
          </svg>
          <a @click="returnHome">Home</a>
        </li>
        <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 16 16" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783"/>
          </svg>
          <a @click="historyPage">History</a>
        </li>
      </ul>
        <!-- Bottom Menu -->
      <div class="absolute bottom-0 w-full p-4 flex flex-col justify-between h-32">
        <ul class="space-y-4">
          <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 11c.04-.66-.16-1.32-.58-1.74m0 3.48c.66.04 1.32-.16 1.74-.58M12 11V8m0 6v3m0-15C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2z" />
            </svg>
            <a @click="toProfile">Profile</a>
          </li>
        </ul>

        <ul class="space-y-4">
          <li class="flex items-center space-x-2 text-black hover:text-white hover:bg-[#FF7823] cursor-pointer p-2 rounded flex-grow">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0z"/>
              <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708z"/>
            </svg>
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
      isOpen: false, // Sidebar open/close state
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

