<template>
    <div class="container mx-auto p-6">
        <Navbar :logo="logo" class="bg-primary text-white py-4" />
        <div class="bg-white rounded-lg shadow-md">
            <div class="border border-gray-300">
                <!-- <h1>History</h1> -->
                <table id="myTable" class="display">
                    <thead>
                        <tr style = "background-color: #FF7823">
                            <th></th>
                            <th>Date</th>
                            <th>Target</th>
                            <th>Result</th>
                            <th>Suggestion</th>
                       
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in history" :key="item.id">
                            <td><input type="checkbox" name="select"></td>
                            <td>{{ item.date || '-' }}</td>
                            <td>{{ item.target || 'N/A' }}</td>
                            <td>{{ item.result ?? 'No Result' }}</td>
                            <td>{{ item.suggestion ?? 'No Suggestion' }}</td>
                          
                            
                            <td>
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-eye text-blue-500 cursor-pointer hover:text-blue-700"
                                    viewBox="0 0 16 16" @click="openModal(item)">
                                    <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
                                    <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
                                </svg>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Modal -->
        <TransitionRoot appear :show="isModalOpen" as="template">
            <Dialog as="div" @close="closeModal" class="fixed inset-0 z-50 flex items-center justify-center">
                <div class="fixed inset-0 bg-black bg-opacity-30"></div>
                
                <div class="relative bg-white p-6 rounded-lg shadow-lg max-w-md w-full mx-auto">
                    <DialogTitle class="text-lg font-semibold">Details</DialogTitle>
                    
                    <div class="mt-4">
                        <p><strong>Date:</strong> {{ selectedItem?.date }}</p>
                        <p><strong>Target:</strong> {{ selectedItem?.target }}</p>
                        <p><strong>Suggestion:</strong> {{ selectedItem?.suggestion }}</p>
                        <p><strong>Result:</strong> {{ selectedItem?.result }}</p>
                    </div>

                    <div class="mt-4 flex justify-end">
                        <button @click="closeModal" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-700">
                            Close
                        </button>
                    </div>
                </div>
            </Dialog>
        </TransitionRoot>
    </div>
</template>

<script>
import Navbar from '../fragments/Navbar.vue';
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
import { Dialog, DialogTitle, TransitionRoot } from '@headlessui/vue';
import $ from 'jquery';
import 'datatables.net-dt/css/dataTables.dataTables.min.css';
import 'datatables.net';
import api from '@/api';

export default {
    name: 'Result',
    components: { Navbar, Dialog, DialogTitle, TransitionRoot },
    
    data() {
        return {
            history: []
        };
    },

    created() {
        this.fetchHistory();
    },

    setup() {
        const isModalOpen = ref(false);
        const selectedItem = ref(null);
        let dataTable = null;

        const openModal = (item) => {
            selectedItem.value = item;
            isModalOpen.value = true;
        };

        const closeModal = () => {
            isModalOpen.value = false;
            selectedItem.value = null;
        };

        const initDataTable = () => {
            nextTick(() => {
                if ($.fn.DataTable.isDataTable('#myTable')) {
                    $('#myTable').DataTable().destroy();
                }
                $('#myTable').DataTable({
                    stateSave: true,
                    responsive: true,
                    columnDefs: [{ width: 10, targets: 0 }],
                    pagingType: 'full_numbers',
                    autoWidth: false,
                    scrollY: '300px',
                    scrollCollapse: true,
                    pageLength: 5,
                    lengthMenu: [
                        [5, 10, 20, 30, -1],
                        [5, 10, 20, 30, 'All']
                    ],
                    language: {
                        search: '',
                        searchPlaceholder: "Search Here...",
                        paginate: {
                            previous: '&laquo;',
                            next: '&raquo;'
                        }
                    }
                });

                window.addEventListener("resize", () => {
                    $('#myTable').DataTable().columns.adjust();
                });
            });
        };

        onMounted(() => {
            if (dataTable) {
                dataTable.destroy();
            }
        });

        onBeforeUnmount(() => {
            if ($.fn.DataTable.isDataTable('#myTable')) {
                $('#myTable').DataTable().destroy();
            }
        });

        return {
            isModalOpen,
            selectedItem,
            openModal,
            closeModal,
            initDataTable
        };
    },

    methods: {
        fetchHistory() {
            api.get('history/')
                .then(response => {
                    this.history = response.data.map(item => ({
                        id: item.id || 0,
                        date: item.date || '-',
                        target: item.target || 'N/A',
                        result: item.result ?? 'No Result',
                        suggestion: item.suggestion ?? 'No Suggestion',
                        photo: item.photo ?? 'Error Loading Photo'
                    }));

                    this.$nextTick(() => this.initDataTable());
                })
                .catch(error => {
                    console.error('Error Fetching History: ', error);
                });
        }
    }
};
</script>


<style>
    @import 'vue3-easy-data-table/dist/style.css';

    @import '../assets/homepage-style.css';

</style>
