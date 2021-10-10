<template>
    <div class="page_container">
        <Modal @showModal="showModal" v-if="show_modal" :id="this.lessonId">
            <table class="table table-striped">
              <thead>
                <tr>
                  <td>id</td>
                  <td>Имя</td>
                  <td>Фамилия</td>
                  <td>Посетил</td>
                  <td>Оплатил</td>
                  <td>Принял оплату</td>
                  <td>Курс</td>
                  <td>Занятие</td>
                  <td>*</td>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in course.children_of_courses" :key="item.id">
                  <td class="our_id">{{item.id}}</td> <!---->
                  <td>{{item.first_name}}</td>
                  <td>{{item.last_name}}</td>
                  <td>
                    <input type="checkbox" class="our_posetil">
                  </td>
                  <td>
                    <input type="checkbox" class="our_oplatil">
                  </td>
                  <td>
                    <input type="checkbox" class="our_prinyal">
                  </td>
                  <td>{{course.id}}</td>
                  <td class="our_urok">{{lessonId}}</td>
                  <td>
                    <button class="btn btn-primary" @click="createAttendance(index)">Отправить</button>
                  </td>
                </tr>
              </tbody>
            </table>
          <button class="btn btn_primary">Отправить</button>
        </Modal>
        <Modal2 @showModal="showModal2" v-if="show_modal2">
            <div class="adding_course">
                <div class="adding_header">Добавление занятия</div>
                <input class="input_primary" placeholder="Название занятия" type="text" v-model="lessonName">
                <input class="input_primary" placeholder="Описание занятия" type="text" v-model="lessonDescription">
                <input class="input_primary" placeholder="Подробная информация" type="text" v-model="lessonInformation">
                <input class="input_primary" placeholder="Цена" type="text" v-model="lessonPrice">
                <input class="input_primary" placeholder="Длительность" type="text" v-model="lessonDuration">
                <label for="">Время</label>
                <input class="input_primary" type="time" v-model="lessonTime">
                <label for="">Дата</label>
                <input class="input_primary" type="date" v-model="lessonDate">
                <button @click="createLesson" class="btn btn_primary">Создать</button>
            </div>
        </Modal2>
        <section class="course_view">
            <div class="view_header">
                <div class="view_emoji">{{course.emoji}}</div>
                <div class="text_container">
                    <div class="container_header">{{course.name}}</div>
                    <div class="container_info">{{course.description}}</div>
                </div>
            </div>
            <div class="adding_info">
                <div class="hours"></div>
                <div class="adding info">
                    Преподаватель: <span class="violet">{{course.teacher}}</span>
                    <br/>
                    Количество часов: <span class="violet">{{course.number_of_hours}}</span>
                </div>
            </div>
            <div class="lessons_container">
                <div v-if="[...course.lessons_in_course].length==0" class="form_message msg">Занятия ещё не добавлены</div>
                <Lesson @showModal="showModal(ls.id)"
                    v-for="(ls, index) in course.lessons_in_course"
                    :key="ls.id"
                    :idx="index+1"
                    :lesson="ls"/>
                    <div @click="showModal2" v-if="$store.getters.getStaff" class="plus">
                        +
                    </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios'
import Lesson from '@/components/course/Lesson'
import Modal from '@/components/main/Modal'
import Modal2 from '@/components/main/Modal'
export default {
    data(){
        return{
            course:{},
            show_modal: false,
            show_modal2: false,
            lessonId: 0,
            lessons: [],
            kids: [],
            lessonName: "",
            lessonDescription: "",
            lessonDate: "",
            lessonTime: "",
            lessonInformation: "",
            lessonDuration: '',
            lessonPrice: ''
        }
    },
    mounted(){
        this.reload();

    },
    components:{
        Lesson,
        Modal,
        Modal2
    },
    methods:{
        reload() {
          axios.get(`http://127.0.0.1:8000/api/course/${this.$route.params.id}/`).then((resp)=>{
            this.course = resp.data[0];
            this.kids = resp.data[0].children_of_courses;
            // console.log(this.course.lessons_in_course.length==0)
          });
        },
        showModal(id){
            this.show_modal=!this.show_modal;
            this.lessonId = id
        },
        showModal2(){
            this.show_modal2=!this.show_modal2;
        },
        /**
         * создание записи в таблице посещаемости
         * @param {number} id - id пользователя
         */
        async createAttendance(id) {
          let our_id = document.querySelectorAll(".our_id")[id].innerHTML;
          let our_posetil = document.querySelectorAll(".our_posetil")[id].checked;
          let our_oplatil = document.querySelectorAll(".our_oplatil")[id].checked;
          let our_prinyal = document.querySelectorAll(".our_prinyal")[id].checked;
          let our_urok = document.querySelectorAll(".our_urok")[id].innerHTML;
          let data = await fetch("http://127.0.0.1:8000/api/att/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json;charset=utf-8"
            },
            body: JSON.stringify({
              paid_confirmed_parent: our_oplatil,
              paid_confirmed_teacher: our_prinyal,
              attendance_confirmed: our_posetil,
              lesson: our_urok,
              child: our_id
            })
          });
          let res = await data.json();
          console.log(res);
        },
        /**
         * создание записи в таблице занятий
         */
        async createLesson() {
          let body = {
            name: this.lessonName,
            description: this.lessonDescription,
            date: this.lessonDate,
            time: `${this.lessonTime}:00`,
            information: this.lessonInformation,
            course: this.course.id,
            duration: this.lessonDuration,
            price: this.lessonPrice
          }
          console.log(this.lessonTime)
          let data = await fetch("http://127.0.0.1:8000/api/lesson/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json;charset=utf-8"
            },
            body: JSON.stringify(body)
          });
          let res = await data.json();
          console.log(res);
          this.reload();
        }

    }
}
</script>
