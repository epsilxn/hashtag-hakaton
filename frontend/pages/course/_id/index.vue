<template>
    <div class="page_container">
        <Modal @showModal="showModal" v-if="show_modal" :id="this.lessonId">
            <table border>
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
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in course.children_of_courses" :key="item.id">
                  <td>{{item.id}}</td>
                  <td>{{item.first_name}}</td>
                  <td>{{item.last_name}}</td>
                  <td><input type="checkbox"></td>
                  <td><input type="checkbox"></td>
                  <td><input type="checkbox"></td>
                  <td>{{course.id}}</td>
                  <td>{{lessonId}}</td>
                </tr>
              </tbody>
            </table>
          <button></button>
        </Modal>
        <Modal2
        @showModal="showModal2"
            v-if="show_modal2">
            asdasdasd
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
            lessons: []
        }
    },
    mounted(){
        axios.get(`http://127.0.0.1:8000/api/course/${this.$route.params.id}/`).then((resp)=>{
            this.course = resp.data[0]
            console.log( resp.data[0])
            // console.log(this.course.lessons_in_course.length==0)
        });

    },
    components:{
        Lesson,
        Modal,
        Modal2
    },
    methods:{
        showModal(id){
            this.show_modal=!this.show_modal;
            this.lessonId = id
        },
        showModal2(){
            this.show_modal2=!this.show_modal2;
        },
      createAttendance() {
          // тут нужно в цикле реализовать логику по пингу на POST http://127.0.0.1:8000/api/att/
        // В цикле потому, что он не сможет обработать массив
        // for (let i = 0; i < tbody.tr.length; i++) {
        //     axios.post("http://127.0.0.1:8000/api/att/", {
        //         нумерация начинается с 1
        //         child: id ребёнка (1 td),
        //         lesson: ласт id в td,
        //         paid_confirmed_parent: td 5,
        //         paid_confirmed_teacher: td 6,
        //         attendance_confirmed: td 4
        //     })
        // }
      }
    }
}
</script>
