<template>
    <div class="page_container">
        <div class="main_page">
            <Parent/>
        </div>
    </div>
</template>


<script>
import Parent from "@/components/lk/Parent" 
import Teacher from "@/components/lk/Teacher" 
import axios from 'axios'
export default {
  middleware: 'auth',
  name: "parent",
  data() {
    return{
      Parent: {},
      is_staff: null
    }
  },
  components: {
    Parent,
    Teacher
  },
  mounted() {
    /**
     * Подгрузка данных о родителе при загрузки компоента
     */
    axios.get("http://127.0.0.1:8000/api/parent").then((res)=>{
      console.log('parent',res)
    });  
    console.log('staff', this.$store.getters.getStaff)
  }
}
</script>