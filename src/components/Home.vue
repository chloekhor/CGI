<template>
  <div>

    <div>
      <Navbar :logo="logo" />
    </div>

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
        <button @click="submitValues" 
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

    <!-- <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p>
    <p>test</p> -->

  </div>
</template>



<script>
import elements from '../images/elements.png';
import Navbar from '../fragments/Navbar.vue';
import Loader from '../fragments/loader.vue';
// import Sidebar from '../fragments/sidebar.vue';

export default { 
  name: 'Home',
  components: {
    Navbar, 
    Loader,

  },
  data() {
    return {
      elements,
      fileLabel: 'Please Enter your image',  
      validExtensions: ['jpg', 'jpeg', 'png'], 
      imagePreview: null,
      sliders: [0,0,0,0],
      isLoading: false,
      errorMessage: ''
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
        const maxSize = 5 * 1024 * 1024; 

        if (!isValid) {
          this.errorMessage = 'Invalid file format. Please upload a JPG or PNG image.';
          // alert("Invalid file format. Please upload a JPG or PNG image.");
          this.fileLabel = "Please Enter your image";
          fileInput.value = "";
          return;
        } else {
          this.errorMessage = '';
        }

        if (file.size > maxSize) {
          this.errorMessage = 'File size exceeds 5MB. Please upload a smaller file.';
          // alert("File size exceeds 5MB. Please upload a smaller file.");
          this.fileLabel = "Please Enter your image";
          fileInput.value = "";
          return;
        }

        this.fileLabel = fileName;
        this.previewImage(event);
      }
    },

    
    previewImage(event) { //to check if image was submitted
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();

        reader.onload = (e) => {
          console.log('FileReader result:', e.target.result);
          this.imagePreview = e.target.result; 
        };

        reader.readAsDataURL(file); 
      }
    },

    submitValues() {
      console.log("Slider Values: ", this.sliders);

      this.isLoading = true;

      setTimeout(() => {
        this.isLoading = false; 

        this.handleValuesTransfer(this.sliders); 

        
        setTimeout(() => {
          this.isLoading = true; 
          setTimeout(() => {
            this.$router.push({ path: '/home/result-page' }); 
          }, 2000); 
        }, 10); 
      }, 2000); 
    },


    handleValuesTransfer(values) {
      alert(`Transferred values: ${values.join(", ")}`);
    },



  }
};
</script>


<style>
@import '../assets/homepage-style.css';
</style>

