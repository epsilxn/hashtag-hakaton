<template>
    <div class="page_container">
        <Modal @showModal="showModal" v-if="show_modal" :id="this.lessonId">
            <table class="table table-striped">
              <thead>
                <tr>
                  <td>id</td>
                  <td>id ребёнка</td>
                  <td>Посетил</td>
                  <td>Оплатил</td>
                  <td>Принял оплату</td>
                  <td>Занятие</td>
                  <td>*</td>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in lessons[lessonId-1].attendance_lessons" :key="item.id">
                  <td class="our_id">{{item.id}}</td> <!-- -->
                  <td class="our_child_id">{{item.child}}</td>
                  <td>
                    <input type="checkbox" class="our_posetil" :checked="item.attendance_confirmed">
                  </td>
                  <td>
                    <input type="checkbox" class="our_oplatil" :checked="item.paid_confirmed_parent">
                  </td>
                  <td>
                    <input type="checkbox" class="our_prinyal" :checked="item.paid_confirmed_teacher">
                  </td>
                  <td class="our_urok">{{lessonId}}</td>
                  <td>
                    <button class="btn btn-primary" @click="updateAttendance(index)">Отправить</button>
                  </td>
                </tr>
              </tbody>
            </table>
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
            lessonPrice: '',
            paid: false,
            accept: false,
            attend: false
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
            this.lessons = resp.data[0].lessons_in_course;
            console.log(resp.data[0].children_of_courses)
          });
        },
        showModal(id){
            this.show_modal=!this.show_modal;
            this.lessonId = id
        },
        showModal2(){
            this.show_modal2=!this.show_modal2;
        },

        async updateAttendance(id) {
          console.log(document.querySelectorAll(".our_id")[id])
          let our_id = document.querySelectorAll(".our_id")[id].innerHTML;
          let attend = document.querySelectorAll(".our_posetil")[id].checked;
          let paid = document.querySelectorAll(".our_oplatil")[id].checked;
          let accept = document.querySelectorAll(".our_prinyal")[id].checked;
          let our_urok = document.querySelectorAll(".our_urok")[id].innerHTML;
          let our_child_id = document.querySelectorAll(".our_child_id")[id].innerHTML;
          axios.put(`http://127.0.0.1:8000/api/att/${our_id}/`, {
            // id: our_id,
            paid_confirmed_parent: paid,
            paid_confirmed_teacher: accept,
            attendance_confirmed: attend,
            lesson: our_urok,
            child: our_child_id
          }).then((res) => {
            console.log(res)
          })
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
            price: this.lessonPrice++
          }
          let data = await fetch("http://127.0.0.1:8000/api/lesson/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json;charset=utf-8"
            },
            body: JSON.stringify(body)
          });
          let res = await data.json();
          this.reload();
        }

    }
}
</script>
