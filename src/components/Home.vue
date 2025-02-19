<template>
  <div>

    
    <Navbar :logo="logo" />
    

    <div v-if="errorMessage" class="text-center py-2 px-4 text-sm font-medium bg-red-100 text-red-600 rounded-md">
      {{ errorMessage }}
    </div>

    <div class="photo-upload shadow-2xl flex justify-center items-center mx-auto border-2 border-dotted border-gradient-to-b from-red-500 to-orange-500 h-40 w-[90%]">
      <label for="picture" 
        class="flex justify-center items-center h-40 w-full rounded-md border border-input bg-background px-3 py-1 
              text-sm shadow-sm transition-colors placeholder:text-muted-foreground text-center cursor-pointer">
        <p class="bg-orange-500 text-white font-bold py-6 px-10 text-4xl md:text-3xl lg:text-3xl rounded-xl hover:bg-orange-600 w-full text-center max-w-[600px]">
          Upload Your CGI Poster Here
          <br/>
          <span class="text-xl">Format: JPEG, PNG; Size: 5MB or less</span>
        </p>
      </label>
      <input class="hidden" id="picture" name="picture" type="file" @change="validateFileFormat">
    </div>

    <h2 class="set-target text-center text-2xl font-semibold mt-4">Set Your Target</h2>

    <div class="elements flex ml-12">
      <img :src="elements" alt="Locked" class="h-80">

      <div class="slider-preview-container flex justify-between items-start w-[90%] mx-auto">
        <div class="flex-col w-1/4">
          <div v-for="(value, index) in 4" :key="index" class="mb-9">
            <label :for="'slider' + (index + 1)" class="block mb-1 -mt-2">
              Value: <span :id="'value' + (index + 1)">0</span>
            </label>
            <input
              type="range"
              :id="'slider' + (index + 1)"
              min="0"
              max="100"
              v-model.number="sliders[index]"
              class="w-full -mt-4 custom-slider"
              :style="{'--slider-progress': sliders[index] + '%'}"
              @input="updateSliderValue(index + 1, $event)"
            >
          </div>
        </div>

        <div>
          <button 
            @click="submitValues" 
            class="relative w-20 h-20 bg-gray-300 text-black font-medium rounded-full transition duration-300 overflow-hidden group mt-4 -ml-2 flex justify-center items-center z-10">
            <span class="relative z-10">Submit</span>
            <span class="absolute inset-0 bg-[#FF7823] scale-0 group-hover:scale-100 cursor-pointer transition-transform duration-300 origin-center rounded-full"></span>
          </button>

         

          <Loader :isLoading="isLoading" />

          
        </div>

        <div class="image-preview-container w-1/3">
          <h4 class="text-lg font-semibold mb-2">Image Preview:</h4>
          <img 
            :src="imagePreview" 
            class="border border-gray-300 max-w-full max-h-60"
          />
        </div>
      </div>
      
    </div>
    <TransitionRoot appear :show="isModalOpen" as="template">
      <Dialog as="div" static @close="closeModal" class="fixed inset-0 z-50 flex items-center justify-center">
        <div class="fixed inset-0 bg-black bg-opacity-30"></div>
        <div class="relative bg-white p-6 rounded-lg shadow-lg max-w-md w-full mx-auto">
          <DialogTitle class="text-lg font-semibold">Please Ensure Targetted Result and Image are Correct Before Analysis Begins</DialogTitle>
          <div class="mt-4">
            <p><strong>Informational:</strong> {{ modalValues.informational }}</p>
            <p><strong>Remunerative:</strong> {{ modalValues.remunerative }}</p>
            <p><strong>Relational:</strong> {{ modalValues.relational }}</p>
            <p><strong>Entertainment:</strong> {{ modalValues.entertainment }}</p>
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
      sliders: [0, 0, 0, 0],
      isLoading: false,
      errorMessage: '',
      selectedFile: null,
      isModalOpen: false,
      modalValues: {
        remunerative: '',
        relational: '',
        entertainment: '',
        informational: ''
      },
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

    async submitValues() {
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

      try {
        this.isLoading = true;
        const response = await axios.post('http://localhost:8000/aiModel/api/upload/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.data.error) {
          console.error("Error:", response.data.error);
        } else {
          console.log("Success:", response.data.message, "Evaluation:", response.data.evaluation);
        }
      } catch (error) {
        console.error('Error uploading file:', error);
      }
      
      console.log("Slider Values: ", this.sliders);

      // Simulate some delays for further processing and navigation
      setTimeout(() => {
        this.isLoading = false; 
        // Optionally, you can handle value transfer or other logic here
        setTimeout(() => {
          this.isLoading = true; 
          setTimeout(() => {
            this.$router.push({ path: '/home/result-page' }); 
          }, 2000); 
        }, 10); 
      }, 2000); 
    },
  }
};
</script>

<style>
@import '../assets/homepage-style.css';
</style>
