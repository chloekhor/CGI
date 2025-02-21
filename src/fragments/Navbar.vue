<template>
    <div class="flex">
      <sideBar/>
      <div class="navbar fixed top-0 left-0 w-full bg-white shadow-md flex items-center px-4 z-20">
        <img class="logo h-16 cursor-pointer" style = "margin-left: 50px" :src="logo" alt="Logo" @click="returnHome">
      </div>

    </div>



  <Loader :isLoading="isLoading" />


  </template>

<script>
import logo from '../images/logo.png';
import Loader from '../fragments/loader.vue';
import sideBar from '../fragments/sidebar.vue';

export default {
    components: {
      sideBar,
      Loader
    },
    data() {
        return {
            logo,
            isOpen: false,
            isLoading: false,
        }
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
        }
        
    }
};
</script>

