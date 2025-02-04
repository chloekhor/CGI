<template>
    <div>
        <Navbar :logo="logo" />
    </div>
    <h1>
        User Profile
    </h1>
</template>

<script>
import Navbar from '../fragments/Navbar.vue';

export default {
    name: 'Result',
    components: {
        Navbar,
    }
}
</script>