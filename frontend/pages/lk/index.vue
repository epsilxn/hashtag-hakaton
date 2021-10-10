<template>
    <div class="page_container">
        <div class="main_page">
            <Parent v-if="!is_staff"/>
            <Teacher v-else/>
            <nuxt-link :to="'/auth'">
              <div class="btn_primary btn_danger">
                выйти
              </div>
            </nuxt-link>
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
      Parent: {},
      is_staff: null
    }
  },
  components: {
    Parent,
    Teacher
  },
  mounted() {
    // axios.get("http://127.0.0.1:8000/api/parent").then((res)=>{
    //   console.log('parent',res)
    // });  
    this.is_staff = this.$store.getters.getStaff
    console.log('staff',this.is_staff)
  }
}
</script>