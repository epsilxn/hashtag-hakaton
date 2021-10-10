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
          <input class="input_primary" v-model="adding_child.last_name" placeholder="Фамилия" type="text">
          <input class="input_primary" v-model="adding_child.first_name" placeholder="Имя" type="text">
          <input class="input_primary" v-model="adding_child.patronymic" placeholder="Отчество" type="text">
          <input class="input_primary" v-for="(p, i) in adding_child.course" v-model="adding_child.course[i]" :key="i" placeholder="Курс" type="text">
          <div @click='addCourse' class="plus">+</div>
        <button @click="addChild" class="btn_primary">Отправить</button>
      </div>
      </Modal>
      <Modal @showModal="showModal3" v-if="show_modal3">
        <div class="adding_course">
          просмотр посещений
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
                    <p @click="getAttendents(ids[index][idx], child.id-1)"> {{idx+1}}) {{child_course}}</p>
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
      show_modal3: false,
      child_att: null,
      childId:0,
      adding_child: {
        first_name: '',
        last_name:'',
        patronymic: '',
        course: ['']
      }
    }
  },
  mounted() {
    // Заменить на динамику, всё работает
    this.mntd()
      
    },
  components:{
      Modal,
      Modal2
    },
  
  methods: {
    mntd(){
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
    showModal(id) {
      this.show_modal = !this.show_modal
      this.childId = id     
    },
    showModal2() {
      this.show_modal2 = !this.show_modal2
    },
    showModal3() {
      this.show_modal3 = !this.show_modal3
    },
    getAttendents(id, child_id){
      console.log(id, child_id)
      this.showModal3()
      axios.get(`http://127.0.0.1:8000/api/parent/2/`).then((res)=>{
        this.child_att=res.data.children_of_parent[child_id]
        console.log(this.child_att)
      })
    },
    addCourse(){
      this.adding_child.course.push('')
    },
    cast(){
      let fc =[]
      for(let i of this.adding_child.course){
        fc.push(Number(i))
      }
      this.adding_child.course = fc
    },
    addChild(){
      this.cast()
      axios.post("http://127.0.0.1:8000/api/children/",{
        last_name: this.adding_child.last_name,
        first_name: this.adding_child.first_name,
        patronymic: this.adding_child.patronymic,
        courses: 1,
        parent_of_child: 2
      }).then((resp)=>{
        console.log(resp)
        this.show_modal2=false
        this.mntd()
      })
      console.log(this.adding_child)
    }
  }
}
</script>

<style scoped>

</style>
