<template>
  <div>
    <Navbar :logo="logo" />
    <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
      {{ errorMessage }}
    </div>

    <!-- Upload Section -->
    <div class="photo-upload shadow-2xl flex justify-center items-center mx-auto border-2 border-dotted border-gradient-to-b from-red-500 to-orange-500 h-40 w-full max-w-[90%]">
      <label for="picture" 
        class="flex justify-center items-center h-40 w-full rounded-md border border-input bg-background px-3 py-1 
              text-sm shadow-sm transition-colors placeholder:text-muted-foreground text-center cursor-pointer">
        <p class="bg-orange-500 text-white font-bold py-4 px-6 text-xl sm:text-2xl md:text-3xl rounded-xl hover:bg-orange-600 w-full text-center max-w-[600px]">
          Upload Your CGI Poster Here
          <br/>
          <span class="text-sm sm:text-base">Format: JPEG, PNG; Size: 5MB or less</span>
        </p>
      </label>
      <input class="hidden" id="picture" name="picture" type="file" @change="validateFileFormat">
    </div>

    <div class="flex flex-col md:flex-row gap-6 items-start justify-start ml-6 pl-10 md:ml-12">
      <div class="w-full md:w-1/3">
        <h2 class="text-2xl font-semibold mt-4">Set Your Target</h2> 

        <br>

        <div class="flex flex-row gap-6 items-center">
          <img :src="elements" alt="Locked" class="w-auto h-auto max-w-[300px] max-h-[300px] sm:max-w-[350px] sm:max-h-[350px] object-contain">

          <!-- slider -->
          <div class="flex flex-col w-full">
            <div v-for="(label, index) in Object.values(sliderLabels)" :key="index" class="mb-10">
              <div class="flex items-center space-x-2">
                <label :for="'slider' + (index + 1)" class="block">
                  {{ label }}: <span :id="'value' + (index + 1)">{{ sliders[index] }}</span>
                </label>

                <!-- help tooltip -->
                <div class="relative flex items-center">
                  <span class="ml-2 cursor-pointer relative" @mouseenter="showTooltip = index" @mouseleave="showTooltip = null">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-circle-help stroke-gray-500">
                      <circle cx="12" cy="12" r="10"/>
                      <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/>
                      <path d="M12 17h.01"/>
                    </svg>

                    <div v-if="showTooltip === index" class="absolute left-1/2 -top-10 -translate-x-1/2 bg-black text-white text-xs py-1 px-2 rounded whitespace-nowrap z-50 shadow-lg">
                      {{ tooltips[index] }}
                    </div>
                  </span>
                </div>
              </div>

              <input
                type="range"
                :id="'slider' + (index + 1)"
                min="0"
                max="10"
                step="1"
                v-model.number="sliders[index]"
                class="w-full custom-slider"
                :style="{
                  background: `linear-gradient(to right, #FF7823 ${sliders[index] * 10}%, #D1D5DB ${sliders[index] * 10}%)`
                }"
                @input="updateSliderValue(index + 1, $event)"
              >

            </div>
          </div>



        </div>

      </div>
      
      <div class="w-full md:w-2/3 flex flex-col items-end ml-auto mr-10">
        <h4 class="text-2xl font-semibold mt-4 text-center self-right" style="margin-right: 120px;">Image Preview</h4>
        <div class="flex justify-end w-full pr-6">
          <img 
            :src="imagePreview" 
            class="border border-gray-300 max-w-[400px] h-auto max-h-[500px]"
          />
        </div>
        <Loader :isLoading="isLoading" />
      </div>
    </div>


    <div class="flex">
          <button 
            @click="submitValues" style = "margin-left: 100px;"
            class="w-40 h-12 bg-gray-300 text-black font-medium rounded-lg transition duration-300 overflow-hidden group relative">

            <span class="relative z-10">Submit</span>
            <span class="absolute inset-0 bg-[#FF7823] scale-0 group-hover:scale-100 cursor-pointer transition-transform duration-300 origin-center rounded-lg"></span>
          </button>
    </div>

    <TransitionRoot appear :show="isModalOpen" as="template">
      <Dialog as="div" static @close="closeModal" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="fixed inset-0 bg-black bg-opacity-30"></div>
        <div class="relative bg-white p-6 rounded-lg shadow-lg max-w-md w-full mx-auto">
          <DialogTitle class="text-lg font-semibold">Please Ensure Targetted Result and Image are Correct Before Analysis Begins</DialogTitle>
          <div class="mt-4">
            <p><strong>Informational:</strong> {{ modalValues.informational }}</p>
            <p><strong>Relational:</strong> {{ modalValues.relational }}</p>
            <p><strong>Entertainment:</strong> {{ modalValues.entertainment }}</p>
            <p><strong>Remunerative:</strong> {{ modalValues.remunerative }}</p>
          </div>
          <div class="mt-4 flex justify-end space-x-2">
            <button 
              @click="beginAnalyze" 
              class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-700">
              Analyze
            </button>
            <button 
              @click="closeModal" 
              class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-700">
              Close
            </button>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

  </div>
</template>

<script>
import elements from '../images/elements.png';
import Navbar from '../fragments/Navbar.vue';
import Loader from '../fragments/loader.vue';
import axios from 'axios';
import api from '@/api/createApi'; 
import { Dialog, DialogTitle, TransitionRoot } from '@headlessui/vue';

export default { 
  name: 'Home',
  components: {
    Navbar, 
    Loader,
    Dialog,
    DialogTitle,
    TransitionRoot
  },
  data() {
    return {
      elements,
      fileLabel: 'Please Enter your image',  
      validExtensions: ['jpg', 'jpeg', 'png'], 
      imagePreview: null,
      sliderLabels: {
        informational: 'Informational Value',
        relational: 'Relational Value',
        entertainment: 'Entertainment Value',
        remunerative: 'Remunerative Value'
      },
      sliders: [0, 0, 0, 0], // This is still an array
      tooltips: {
        informational: 'The poster contains product information, descriptions, or details about the product or service.',
        relational: 'The poster highlights relationships, such as friends, family, gatherings, or social interactions.',
        entertainment: 'The poster includes entertaining elements, such as exaggerated facial expressions, humor, or playful visuals.',
        remunerative: 'The poster emphasizes offers, promotions, discounts, or other financial incentives.'
      },
      showTooltip: null,
      isLoading: false,
      errorMessage: '',
      selectedFile: null,
      isModalOpen: false,
      modalValues: {
        remunerative: '',
        relational: '',
        entertainment: '',
        informational: ''
      }
    };
  },



  methods: {
    updateSliderValue(index, event) {
      document.getElementById(`value${index}`).innerHTML = event.target.value;
    },

    validateFileFormat(event) {
      const fileInput = event.target;
      const file = fileInput.files[0];

      if (file) {
        const fileName = file.name.toLowerCase();
        const isValid = this.validExtensions.some(ext => fileName.endsWith(ext));
        const maxSize = 5 * 1024 * 1024; // 5MB

        if (!isValid) {
          this.errorMessage = 'Invalid file format. Please upload a JPG or PNG image.';
          this.fileLabel = "Please Enter your image";
          fileInput.value = "";
          return;
        } else {
          this.errorMessage = '';
        }

        if (file.size > maxSize) {
          this.errorMessage = 'File size exceeds 5MB. Please upload a smaller file.';
          this.fileLabel = "Please Enter your image";
          fileInput.value = "";
          return;
        }

        this.fileLabel = fileName;
        this.selectedFile = file;
        this.previewImage(event);
      }
    },
    
    previewImage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          // console.log('FileReader result:', e.target.result);
          this.imagePreview = e.target.result; 
        };
        reader.readAsDataURL(file); 
      }
    },
    submitValues() {
      this.isLoading = true;
      if (!this.selectedFile) {
        this.errorMessage = 'Please select a file first.';
        this.isLoading = false;
        return;
      }

      // Set the modalValues based on the current slider values
      this.modalValues = {
        remunerative: this.sliders[0],
        relational: this.sliders[1],
        entertainment: this.sliders[2],
        informational: this.sliders[3]
      };

      this.isModalOpen = true;
      this.isLoading = false;
    },

    closeModal() {
      this.isModalOpen = false;
    },


    async beginAnalyze() {
      const formData = new FormData();
      formData.append('photo', this.selectedFile); 
      formData.append('target', JSON.stringify(this.sliders));

      try {
        this.isLoading = true;
        const response = await axios.post('http://localhost:8000/aiModel/api/upload/', formData, {
          headers: { 'Content-Type': 'multipart/form-data' },
          withCredentials: true  // Ensures session cookies are sent
        });

        if (response.data.error) {
          console.error("Error:", response.data.error);
          this.isLoading = false;
          return;
        }

        const evaluationResult = response.data.evaluation;
        const recommendation = response.data.recommendation; 
        const photoUrl = response.data.photo_url;

        console.log(evaluationResult);

        const response2 = await api.post('/save/', {
          evaluation: evaluationResult,
          recommendation: recommendation,
          target: this.modalValues,
          photo_url: photoUrl
        }, {
          headers: { 'Content-Type': 'application/json' }, 
          withCredentials: true 
        });


        if (response2.data.error) {
          console.error("Error in saving:", response2.data.error);
          this.isLoading = false;
          return;
        }

        this.$router.push({
          path: '/home/result-page',
          query: { 
            result: JSON.stringify(evaluationResult),
            target: JSON.stringify(this.sliders), 
            recommendation: recommendation,
            photoUrl: photoUrl
          }
        });

      } catch (error) {
        console.error('Error uploading file:', error);
      }

      // Simulate some delays for further processing and navigation
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);
    },
  }
};
</script>

<style>
@import '../assets/homepage-style.css';
</style>
