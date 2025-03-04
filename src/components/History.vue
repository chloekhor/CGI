<template>
    <div class="container mx-auto p-6">
        <Navbar :logo="logo" class="bg-primary text-white py-4" />
        <div class="bg-white rounded-lg shadow-md">
            <div class="border border-gray-300">
                <table id="historyTable" class="display">
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
                            <td v-html="formatData(item.target)"></td>
                            <td v-html="formatData(item.result)"></td>
                            <td>{{ item.suggestion ?? 'No Suggestion' }}</td>
                          
                            
                            <td class="h-full text-center">
                                <div class="flex justify-center items-center space-x-2 h-full">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" 
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" 
                                        class="lucide lucide-eye cursor-pointer hover:stroke-blue-300 transition" @click="openModal(item)">
                                        <path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/>
                                        <circle cx="12" cy="12" r="3"/>
                                    </svg>
                                    
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" 
                                        stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" 
                                        class="lucide lucide-download cursor-pointer hover:stroke-blue-300 transition" @click="downloadReport(item)">
                                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                                        <polyline points="7 10 12 15 17 10"/>
                                        <line x1="12" x2="12" y1="15" y2="3"/>
                                    </svg>
                                </div>
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
                
                <div class="relative bg-white p-6 rounded-lg shadow-lg w-auto mx-auto">
                    <DialogTitle class="text-lg font-semibold">Details</DialogTitle>
                    
                    <div class="mt-4">
                        <p><strong>Date:</strong> {{ selectedItem?.date }}</p>
                        <p><strong>Target:</strong> {{ formatInline(selectedItem?.target) }}</p>
                        <p><strong>Suggestion:</strong> {{ selectedItem?.suggestion }}</p>
                        <p><strong>Result:</strong> {{ formatInline(selectedItem?.result) }}</p>
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
    <Loader :isLoading="isLoading" />

</template>

<script>
import Navbar from '../fragments/Navbar.vue';
import Loader from '../fragments/loader.vue';

import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue';
import { Dialog, DialogTitle, TransitionRoot } from '@headlessui/vue';
import $ from 'jquery';
import 'datatables.net-dt/css/dataTables.dataTables.min.css';
import 'datatables.net';
import api from '@/api/readApi';
// import { generatePDFReport } from "../utils/generateReport.js";

import { toRaw } from 'vue';

export default {
    name: 'Result',
    components: { Navbar, Dialog, DialogTitle, TransitionRoot, Loader },
    
    data() {
        return {
            history: [],
            isLoading: false,
            evaluationResult: '',
            target: '',
            photo: '',
            recommendation: ''

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
                if ($.fn.DataTable.isDataTable('#historyTable')) {
                    $('#historyTable').DataTable().destroy();
                }
                $('#historyTable').DataTable({
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
                    $('#historyTable').DataTable().columns.adjust();
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
            this.isLoading = true;
            api.get('history/')
                .then(response => {
                    this.history = response.data.map(item => ({
                        id: item.id || 0,
                        date: item.date || '-',
                        target: item.target || 'N/A',
                        result: item.result ?? 'No Result',
                        suggestion: item.summary ?? 'No Suggestion',
                        fullAnalysis: item.fullAnalysis ?? 'No Analysis',
                        photo: item.photo ?? 'Error Loading Photo'
                    }));

                    this.isLoading = false;
                    this.$nextTick(() => this.initDataTable());
                })
                .catch(error => {
                    console.error('Error Fetching History: ', error);
                    this.isLoading = false;
                });
        },

        formatData(data) {
            if (!data) return 'N/A'; // Handles null/undefined

            if (typeof data === 'object') {
                // Convert object to "key: value" format
                return Object.entries(data).map(([key, value]) => `${key}: ${value}`).join('<br>');
            }

            try {
                let obj = JSON.parse(data); 
                return Object.entries(obj).map(([key, value]) => `${key}: ${value}`).join('<br>');
            } catch (e) {
                return data.replace(/,/g, '<br>'); 
            }
        },

        formatInline(data) {
            if (!data) return 'N/A'; 
            
            if (typeof data === 'object') {
                // Convert object to "key: value" format, separating with commas
                return Object.entries(data).map(([key, value]) => `${key}: ${value}`).join(', ');
            }

            try {
                let obj = JSON.parse(data); // Convert JSON string to an object
                return Object.entries(obj).map(([key, value]) => `${key}: ${value}`).join(', ');
            } catch (e) {
                return data; 
            }
        },

        downloadReport(item) {
            console.log(item);

            const rawItem = toRaw(item);  // Convert Proxy to plain object
            console.log(Object.values(rawItem)[2]);

            let target = Object.values(Object.values(rawItem)[2]);  
            let result = Object.values(rawItem)[3];
            let recommendation = Object.values(rawItem)[5];
            let photo_url = Object.values(rawItem)[6];  
            
            console.log(recommendation);

            // Send the data using Vue Router's push
            this.$router.push({
                path: '/result-page',
                query: { 
                    result: JSON.stringify(result),  
                    target: JSON.stringify(target),  
                    recommendation: recommendation, 
                    photoUrl: photo_url
                }
            });
        },





    }
};
</script>


<style>
    @import 'vue3-easy-data-table/dist/style.css';

    @import '../assets/homepage-style.css';

</style>

