<template>
  <div class="teacher_info">
    <div class="lk_header">Личный кабинет</div>
    <Modal @showModal="showModal" v-if="show_modal">
<!--      Как бы было классно вынести эту монотонную залупу в отдельный компонент, но это не реакт, я не знаю экспорты/импорты во вью....-->
      <div class="adding_course">
        <div class="adding_header">Добавление курса</div>
        <input class="input_primary" placeholder="Название курса" type="text" v-model="courseName">
        <input class="input_primary" placeholder="Описание курса" v-model="descCourse">
        <input class="input_primary" placeholder="Эмодзи" type="text" v-model="emoji">
        <input class="input_primary" placeholder="Kоличество часов" type="text" v-model="hours">
        <button class="btn_primary" @click="addCourse">Отправить</button>
      </div>
    </Modal>
    <div class="about_block">

      <div class="about_me">
        <div class="card">
          <div class="card_header">
            Информация обо мне
          </div>
          <div class="card_body">
            <label for="">ФИО</label>
            <p>{{ teacher.last_name }} {{ teacher.first_name }} {{ teacher.patronymic }} <span class="liryc">id: {{ teacher.id }}</span></p>
            <label for="">Почта</label>
            <p>{{ teacher.email }}</p>
            <label for="">Номер телефона</label>
            <p>{{ teacher.phone || "8 800 555 35 35" }}</p>
          </div>
        </div>
        <div></div>
      </div>

      <div class="about_me">
        <div class="card">
          <div class="card_header course_head">
            <p>Мои курсы</p>
            <button class="plus" @click="showModal">+</button>
          </div>
          <div v-for="item in course" :key="item.id" class="card_body">

              <label>{{ item.name }}</label>
              <div class="card_course_item">
                <nuxt-link :to="'/course/'+item.id">Страница курса</nuxt-link>
                <button class="btn_primary btn_warning">Редактировать</button>
                <button class="btn_primary btn_danger" @click="deleteCourse($event)" :data="item.id">Удалить</button>
              </div>


          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Modal from "@/components/main/Modal";
import axios from "axios";

export default {
  name: "Teacher",
  data() {
    return {
      course: "",
      teacher: "",
      show_modal: false,
      courseName: "",
      descCourse: "",
      emoji: "😀",
      hours: 10
    }
  },
  async mounted() {
    this.reload()
  },
  methods: {
    async reload(){
      let teacher = await (await fetch("http://127.0.0.1:8000/api/teacher/1/")).json();
      let course = await (await fetch(`http://127.0.0.1:8000/api/course?id=1`)).json();
      console.log(course);
      console.log(teacher);
      this.course = course;
      this.teacher = teacher;
    },
    deleteCourse(event) {
      let id = event.target.attributes.data.value;
      console.log('target', event.target.attributes.data.value)
      // с ивента подцепи
      // К кнопке "удалить" надо добавить event (или как это тут называется)
      axios.delete(`http://127.0.0.1:8000/api/course/${id}/`).then((res) => {})
      this.reload()
    },
    async addCourse() {
      let data = await fetch("http://127.0.0.1:8000/api/course/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8"
        },
        body: JSON.stringify({
          name: this.courseName,
          description: this.descCourse,
          teacher: this.teacher.id,
          emoji: this.emoji,
          number_of_hours: this.hours
        })
      });
      let res = await data.json();
      console.log(res);
      this.reload();
    },
    showModal() {
      this.show_modal = !this.show_modal;
    },
  },
  components: {
    Modal
  }
}
</script>

<style scoped>
button {
  padding: 0.125rem;
  border: 1px solid black;
}

.w-50 {
  width: 50% !important;
}

.justify-space-around {
  justify-content: space-around;
}

.justify-space-between {
  justify-content: space-between;
}

.top-4 {
  margin-top: 4rem;
}

.flex {
  display: flex;
}

.flex-column {
  flex-direction: column;
}

.flex-row {
  flex-direction: row;
}

.m-1 {
  margin: 0.725rem;
}

.ml-1 {
  margin-left: 0.725rem;
}

.mb-1 {
  margin-bottom: 0.725rem;
}

.p-1 {
  padding: 0.5rem;
}

.b-1 {
  border: 1px solid black;
}

.card {
  min-width: 100%;
  min-height: 10rem;
  border-radius: 5px !important;
  background-color: white !important;
  text-align: left;
  text-wrap: normal;
  z-index: 10;
}

.card-header {
  font-size: 1.1rem;
  border-bottom: 1px solid rgba(33, 32, 32, 0.77);
  width: 100%;
  padding: 0.4rem;
  margin-bottom: 0.4rem;
}

.card-body {
  width: 100%;
  padding: 0.4rem;
  margin-bottom: 0.4rem;
}

.card-footer {
  border-top: 1px solid black;
  margin-bottom: 0.4rem;
}
</style>
