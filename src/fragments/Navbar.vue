<template>
    <div class="flex">
      <sideBar/>
      <div class="navbar fixed top-0 left-0 w-full bg-white shadow-md flex items-center px-4">
        <img class="logo h-16" style = "margin-left: 50px" :src="logo" alt="Logo" @click="returnHome">
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
        }
    },
    methods: {
        toggleSidebar() {
            this.isOpen = !this.isOpen;
        },
        
    }
};
</script>

