<template>
    <div class="page_container">
        <div class="main_page">
            <Parent/>
            <Teacher/>
        </div>
    </div>
</template>


<script>
import Parent from "@/components/lk/Parent" 
import Teacher from "@/components/lk/Teacher" 
import axios from 'axios'
export default {
  name: "parent",
  data() {
    return{
      Parent: {}
    }
  },
  components: {
    Parent,
    Teacher
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/parent").then((res)=>{
      console.log('parent',res)
    });
    
    
  }
}
</script>