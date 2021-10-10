<template>
    <div class="teacher_info">
      <p class="lk_header">Личный кабинет</p>
      <div class="about_block">
        
        <div class="about_me">
          <div class="card">
            <div class="card_header">
              Родитель
            </div>
            <div class="card_body">
              <label for="">ФИО</label>
              <p>{{ parent.last_name }} {{ parent.first_name }} {{ parent.patronymic }} <span class="liryc">id: {{ parent.id }}</span></p>
              <label for="">Почта</label>
              <p>{{ parent.mail || 'не указана'}}</p>
              <label for="">Номер телефона</label>
              <p>{{ parent.phone || "8 800 555 35 35" }}</p>
            </div>
          </div>
        </div>
        <div class="about_me">
          <div class="card">
            <div class="card_header">
              Дети
            </div>
            <div class="card_body">
              <div :key="index" v-for="(child, index) in parent.children_of_parent" class="child_info">
                
                  <label for="">ФИО</label>
                  <p>{{child.last_name}} {{child.first_name}} {{child.patronymic}}</p>
                  <label for="">Записан на</label>
                  <div :key="idx" v-for="(child_course, idx) in ids2[index]">
                     <p> {{idx+1}}) {{child_course}}</p>
                  </div>
                </div>
              </div>
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
      axios.get("http://127.0.0.1:8000/api/parent/2/").then((resp)=>{
        this.parent = resp.data
        console.log(this.parent)
        for (let item of resp.data.children_of_parent){
          this.ids.push(item.courses)
        }
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
