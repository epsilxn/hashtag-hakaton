<template>
  <div class="page_container">
    <div class="main_page">
      <div class="main_description">
        <span class='violet'>GibCourses </span>
        предоставляет <span class='violet'>
          дополнительное образование</span>
        для вашего ребёнка по самым различным направлениям
        <br/>
        <br/>
        На данный момент, обучение проводится по <span class='violet'>{{this.course_list.length}}</span> образовательным программам
        <Search @onInput="onInput"/>
      </div>
<!--      <Courses :courses="courses_computed"/>-->
      <div v-if="!(this.course_list.length < to_show)" @click="to_show+=2" class="nbtn">
        <div class="btn">Показать больше</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Search from '@/components/main/Search'
import Courses from '@/components/main/Courses'

export default {
  data() {
    return {
      course_list: [],
      to_show: 4,
      search: null
    }
  },
  components: {
    Search,
    Courses
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/course/').then((resp) => {
      this.course_list = resp.data
      console.log(this.course_list)
    })
  },
  methods: {
    onInput(search) {
      this.search = search
      console.log(this.search)
    }
  },
<<<<<<< HEAD
  computed:{
    courses_computed(){
      if (this.search){
        return this.course_list.filter((el)=>{
          if (el.name.toLowerCase().indexOf(this.search.toLowerCase()) !== -1)
=======
  computed: {
    courses_computed() {
      if (this.search) {
        return this.course_list.filter((el) => {
          if (el.name.indexOf(this.search) !== -1)
>>>>>>> 8748d3f05c57c384c33dba577fb7d9bdd099b60a
            return el
        })
      }
      return this.course_list.slice(0, this.to_show)
    }
  }
}
</script>
