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
        
      </div>
      <Search @onInput="onInput"/>
      <Courses :courses="courses_computed"/>
      <div v-if="!(this.course_list.length <= to_show)" @click="to_show+=2" class="nbtn">
        <div class="btn">ЕЩЁ</div>
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
      to_show: 6,
      search: null
    }
  },
  components: {
    Search,
    Courses
  },
  mounted() {
    window.addEventListener('resize', e=>{
      if (window.screen.width < 600){
        this.to_show = 3
      }
      else{
        this.to_show = 6
      }
    })
      
    axios.get('http://127.0.0.1:8000/api/course/').then((resp) => {
      this.course_list = resp.data
      console.log(this.course_list)
    })
  },
  methods: {
    /**
     * @param {String} search - подстрока для запроса
     */
    onInput(search) {
      this.search = search
      console.log(this.search)
    }
  },
  computed:{
    /**
     * @return массив элементов, содержащих в себе подстроку search
     */
    courses_computed(){
      if (this.search){
        return this.course_list.filter((el)=>{
          if (el.name.toLowerCase().indexOf(this.search.toLowerCase()) !== -1)
            return el
        })
      }
      return this.course_list.slice(0, this.to_show)
    }
  }
}
</script>
