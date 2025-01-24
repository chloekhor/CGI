<template>
    
    <div class="navbar fixed top-0 left-0 w-full bg-white shadow-md flex items-center px-4">
        <img class="logo h-16" :src="logo" alt="Logo" @click="returnHome">
    </div>
</template>

<script>
import logo from '../images/logo.png';
export default {
    data() {
        return {
            logo
        }
    },
    methods: {
        returnHome() {
            this.$router.push('/home');
        }
    }
};
</script>

