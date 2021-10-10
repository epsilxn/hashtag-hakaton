<template>
    <div class="main_info">
        <Modal @showModal="showModal" v-if="show_modal">
            <table border>
              <thead>
                <tr>
                  <!--<td>Курс</td>-->
                  <th>Занятие</th>
                  <th>Посетил</th>
                  <th>Оплатить</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                <div v-for="item in parent.children_of_parent" :key="item.id">
                  <div v-if="item.id == childId">
                    <div v-for="att in item.attendance_child" :key="att.id">
                    <!--<td>{{att.id}}</td>-->
                      <td>{{att.lesson}}</td>
                      <td>{{att.attendance_confirmed}}</td>
                      <td><input type="checkbox"></td>

                    </div>
                  </div>
                </div>
                </tr>
              </tbody>
            </table>
          <button></button>
        </Modal>


        <p class="hello">Здравствуйте, родитель</p>
        <div class="line"></div>
        <div class="flex_info">
            <div class="parent_info">
              <p>Фамилия: {{parent.last_name}}</p>
              <p>Имя: {{parent.first_name}}</p>
              <p>Отчество: {{parent.patronymic}}</p>
            </div>
            <div class="child_info">
              <div :key="child.id" v-for="(child, index) in parent.children_of_parent">
                  <p>Ваш ребёнок: {{child.last_name}} {{child.first_name}} {{child.patronymic}}</p>
                  <p>Записан на курсы:</p>
                  <div :key="child_course" v-for="child_course in ids2[index]">
                      <p>{{child_course}}</p>
                  </div>
                  <button @click="showModal(child.id)">Подробнее</button>
              </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Modal from '@/components/main/Modal'
export default {
  name: "Parent",
  data() {
    return {
      parent: "",
      child_one: "",
      ids:[],
      ids2:[],
      show_modal:true,
      childId:0,
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
    },
  components:{
      Modal
    },
  methods: {
    showModal(id) {
      this.show_modal = !this.show_modal
      this.childId = id     
    },
  }
}
</script>

<style scoped>

</style>
