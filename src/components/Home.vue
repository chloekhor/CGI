<template>
  <div class="text-center">
    <h1>Welcome to the Home Page</h1>
    <p>This is the default page.</p>
    <router-link to="/login" class="text-indigo-500 hover:underline">Go to Login</router-link>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>
