<template>
    <div class="main_info">
        <p class="hello">Здравствуйте, родитель</p>
        <div class="line"></div>
        <div class="flex_info">
            <div class="parent_info">
              <p>Фамилия: {{parent.last_name}}</p>
              <p>Имя: {{parent.first_name}}</p>
              <p>Отчество: {{parent.patronymic}}</p>
            </div>
            <div class="child_info">
              <div :key="child.id" v-for="child in parent.children_of_parent">
                  <p>Ваш ребёнок: {{child.last_name}} {{child.first_name}} {{child.patronymic}}</p>
                  <p>Записан на курсы:</p>
                  <div :key="child_course" v-for="child_course in child.courses">
                      <p>{{child_course}}</p>
                  </div>
              </div>
            </div>
        </div>
      </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Parent",
  data() {
    return {
      parent: "",
      ids:[],
      ids2:[]
    }
  },
    mounted() {
    // Заменить на динамику, всё работает
      axios.get("http://127.0.0.1:8000/api/parent/2/").then((resp)=>{
        this.parent = resp.data
        
        for (let item of resp.data.children_of_parent){
          this.ids.push(item.courses)
        }
        console.log(this.ids)
        let to_push = []
        for (let i = 0; i < this.ids.length; i++){
          let to_push_inside = []
          for(let j=0; j < this.ids[i].length; j++){
            axios.get(`http://127.0.0.1:8000/api/course/${this.ids[i][j]}`).then((res)=>{
              to_push_inside.push(res.data[0].name)
            })
          }
          to_push.push(to_push_inside)
        }
        this.ids2 = to_push
      })
      
    }
}
</script>

<style scoped>

</style>
