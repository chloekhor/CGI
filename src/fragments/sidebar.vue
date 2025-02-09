<template>
  <div class="flex">
    <!-- Sidebar -->
    <div :class="{'w-64': isOpen, 'w-20': !isOpen}" class="bg-white-800 shadow-sm text-white h-screen transition-width duration-300 ease-in-out">
      <div class="flex justify-between p-4">
        <h2 v-if="isOpen" class="text-lg font-semibold">Sidebar</h2>
        <button @click="toggleSidebar" class="text-xl">
          <i :class="{'hidden': isOpen, 'block': !isOpen}">&#9776;</i>
          <i :class="{'hidden': !isOpen, 'block': isOpen}">&times;</i>
        </button>
      </div>
      <ul v-if="isOpen" class="space-y-4 px-4">
        <li><a href="#" class="hover:bg-gray-700 p-2 rounded">Home</a></li>
        <li><a href="#" class="hover:bg-gray-700 p-2 rounded">About</a></li>
        <li><a href="#" class="hover:bg-gray-700 p-2 rounded">Services</a></li>
      </ul>
    </div>
</div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: true, // Sidebar open/close state
    };
  },
  methods: {
    toggleSidebar() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

