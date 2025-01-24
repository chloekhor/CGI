<template>
    <div v-if="isLoading && loaderGif" class="loader-container">
        <img 
            v-if="loaderGif" 
            :src="loaderGif" 
            alt="Loading..." 
            class="loader-image" 
            @error="handleBrokenImage" 
        />
    </div>
</template>


<script>
import preloaderGif from '../assets/preloader.gif';

export default {
    props: {
        isLoading: {
            type: Boolean,
            required: true,
        },
        loaderGif: {
            type: String,
            default: preloaderGif, 
        },
    },
    
};

</script>


<style scoped>
    .loader-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    .loader-image {
        width: 100px; 
        height: auto;
    }
</style>
