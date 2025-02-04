<template>
  <div>

    <div>
      <Navbar :logo="logo" />
    </div>

    <div class="photo-upload flex justify-center items-center mx-auto border-2 border-dotted border-gradient-to-b from-red-500 to-orange-500 h-40 w-[90%]">
      <label 
        for="picture" 
        class="flex justify-center items-center h-40 w-full rounded-md border border-input bg-background px-3 py-1 
              text-sm shadow-sm transition-colors placeholder:text-muted-foreground text-center cursor-pointer"
      >
        <span id="file-label">Upload Your CGI Poster Here</span>
      </label>
      <input 
        class="hidden" 
        id="picture" 
        name="picture" 
        type="file" 
        @change="validateFileFormat"
      
      >
      
    </div>

    <h2 class="set-target text-center text-2xl font-semibold mt-4">Set Your Target</h2>

    <div class="elements flex ml-12 mt-2">
      <img :src="elements" alt="Locked" class="h-80">
    

      <div class="slider-preview-container flex justify-between items-start w-[90%] mx-auto mt-4">
      <div class="flex-col w-1/4" style = "accent-color: #EF4748;">
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
        <button @click="submitValues" class="bg-gray-300 hover:bg-red-300 text-black font-medium rounded-full px-4 py-2 transition duration-300">
          Submit
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
      isLoading: false
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
        
        if (isValid) {
          this.fileLabel = fileName;  
          this.previewImage(event); 
        } else {
          alert("Invalid file format. Please upload a JPG or PNG image.");
          this.fileLabel = 'Please Enter your image';  
          fileInput.value = '';  
        }
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

