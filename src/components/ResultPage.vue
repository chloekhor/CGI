<template>
  <div class="result-container">
    <div>
      <Navbar :logo="logo" />
    </div>
    
    <div class="content-wrapper">
      <!-- left area -->
      <div class="w-1/2">
        <h2 class="text-2xl font-bold text-center mb-6">Evaluation Results</h2>
        <div class="matrix-wrapper">
          <div class="axis-label top">Informative</div>
          <div class="axis-label left">Remunerative</div>
          <div class="axis-label right">Relational</div>
          <div class="axis-label bottom">Entertainment</div>

          <div class="matrix-container">
            <canvas ref="matrixCanvas" width="350" height="350"></canvas>
          </div>
        </div>

        <div class="flex justify-center space-x-5 mt-8">
          <p class="flex items-center text-gray-700">
            <span class="w-3 h-3 bg-black rounded-full inline-block mr-2"></span> 
            Target Values
          </p>
          <p class="flex items-center text-gray-700">
            <span class="w-3 h-3 bg-red-500 rounded-full inline-block mr-2"></span> 
            Evaluation Result
          </p>
        </div>
      </div>

      <!-- right area -->
      <div class="w-1/2 bg-gray-100 p-4 rounded-md">
        <h2 class="text-2xl font-bold text-center mb-6">Suggestions</h2>

        <!-- Summary -->
        <div v-if="recommendation" class="text-left">
          <p v-html="parsedRecommendation"></p>
        </div>
        <div v-else class="suggestion-box loading">Loading suggestions...</div>

        <!-- download report -->
        <div class="mt-6 text-center">
          <p class="text-gray-700 mb-2 text-sm">For a detailed report, please download the full report.</p>
          <button 
            @click="downloadReport" 
            class="px-4 py-2 bg-orange-600 text-white rounded-md shadow-md hover:bg-orange-700 transition w-full"
          >
            Download Report
          </button>
        </div>

        <!-- upload new image -->
        <div class="mt-4 text-center">
          <button 
            @click="goToHomePage" 
            class="px-4 py-2 bg-orange-600 text-white rounded-md shadow-md hover:bg-orange-700 transition w-full"
          >
            Upload Another Image
          </button>
        </div>
      </div>
    </div> 
  </div> 
</template>

  
  <script>
  import Navbar from '../fragments/Navbar.vue';
  import { drawMatrix } from '../utils/matrixDrawer.js';
  import { marked } from 'marked';
  import { generatePDFReport } from "../utils/generateReport.js";

  
  export default {
    components: {
      Navbar, 
    },
    data() {
      return {
        evaluationResult: null,
        targetValues: [0, 0, 0, 0],
        recommendation: "",
        parsedRecommendation: "",
        photoUrl: ""
      };
    },
    created() {
      const queryResult = this.$route.query.result;
      const queryTarget = this.$route.query.target;
      const queryRecommendation = this.$route.query.recommendation;
      const queryPhotoUrl = this.$route.query.photoUrl;
      console.log("Received photo URL:", queryPhotoUrl);
  
      if (queryResult) {
        this.evaluationResult = JSON.parse(queryResult);
        console.log("Received Evaluation Result:", this.evaluationResult);
      }
      if (queryTarget) {
        this.targetValues = JSON.parse(queryTarget);
        console.log("Received Target Values:", this.targetValues);
      }
      if (queryRecommendation) {
        //show only summary part
        this.recommendation = queryRecommendation;
        const summaryMatch = queryRecommendation.match(/### \*\*Summary\*\*([\s\S]*)/);
        if (summaryMatch) {
          this.parsedRecommendation = marked(summaryMatch[1].trim()); 
        } else {
          this.parsedRecommendation = "No summary found.";
        }
      }
      if (queryPhotoUrl) {
        if (!queryPhotoUrl.startsWith("http")) {
          this.photoUrl = "http://localhost:8000" + queryPhotoUrl;
        } else {
          this.photoUrl = queryPhotoUrl;
        }
      }
    },
    mounted() {
      drawMatrix(this.$refs.matrixCanvas, this.targetValues, this.evaluationResult);
    },

    methods: {
      downloadReport() {
        generatePDFReport(this.evaluationResult, this.targetValues, this.recommendation, 
        this.$refs.matrixCanvas,this.photoUrl);
      },

      goToHomePage() {
        this.$router.push({ path: "/home" });
      }
    }
  };
  </script>
  
  <style>
  @import '../assets/resultpage-style.css';
  </style>
  