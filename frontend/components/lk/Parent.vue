<template>

    <div class="teacher_info">
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
      <Modal @showModal="showModal2" v-if="show_modal2">
        <div class="adding_course">
          <div class="adding_header">Добавление ребёнка</div>
          <input class="input_primary" placeholder="Фамилия" type="text">
          <input class="input_primary" placeholder="Имя" type="text">
          <input class="input_primary" placeholder="Отчество" type="text">
          <input class="input_primary" placeholder="Курс" type="text">
        <button class="btn_primary">Отправить</button>
      </div>
      </Modal>
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
              <div @click="showModal2" class="plus">+</div>
              <div :key="index" v-for="(child, index) in parent.children_of_parent" class="child_info">
                
                  <label for="">ФИО</label>
                  <p>{{child.last_name}} {{child.first_name}} {{child.patronymic}}</p>
                  <label for="">Записан на</label>
                  <div :key="idx" v-for="(child_course, idx) in ids2[index]">
                    <p @click="getAttendents(ids[index][idx], child.id)"> {{idx+1}}) {{child_course}}</p>
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
import Modal from '@/components/main/Modal'
import Modal2 from '@/components/main/Modal'
export default {
  name: "Parent",
  data() {
    return {
      parent: "",
      child_one: "",
      ids:[],
      ids2:[],
      show_modal: false,
      show_modal2: false,
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
      Modal,
      Modal2
    },
  methods: {
    showModal(id) {
      this.show_modal = !this.show_modal
      this.childId = id     
    },
    showModal2() {
      this.show_modal2 = !this.show_modal2
    },
    getAttendents(id, child_id){
      console.log(id, child_id)
      axios.get(`http://127.0.0.1:8000/api/course/${id}`).then((res)=>{
        console.log(res.data[0].children_of_courses)
      })
    }
  }
}
</script>

<style scoped>

</style>
