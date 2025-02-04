<template>
    <h1>Testing</h1>
    <div class="container mx-auto p-6">

      <Navbar :logo="logo" class="bg-primary text-white py-4" />
  

      <div class="mt-8 bg-white rounded-lg shadow-md p-4">
        <easy-data-table
          :headers="headers"
          :items="items"
          class="custom-table"
        />
      </div>
    </div>
</template>
  
<script>
    import Navbar from '../fragments/Navbar.vue';
    import EasyDataTable from 'vue3-easy-data-table';

    export default {
        name: 'Result',
        components: { EasyDataTable, Navbar },
        data() {
            return {
            headers: [
                { text: 'Name', value: 'name' },
                { text: 'Age', value: 'age' }
            ],
            items: [
                { name: 'John', age: 28 },
                { name: 'Jane', age: 34 }
            ]
            };
        }
    };
</script>
  
<style scoped>
/* Import Easy Data Table styles */
    @import 'vue3-easy-data-table/dist/style.css';
</style>