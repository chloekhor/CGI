<template>
    <div>
        <Navbar :logo="logo" />
    </div>
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