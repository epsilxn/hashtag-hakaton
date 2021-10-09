<template>
  <div class="top-4">
    <Modal @showModal="showModal" v-if="show_modal">
<!--      Как бы было классно вынести эту монотонную залупу в отдельный компонент, но это не реакт, я не знаю экспорты/импорты во вью....-->
      <div class="flex flex-column">
        <div>
          <p>Название курса (снизу input)</p>
          <input type="text">
        </div>
        <div>
          <p>Описание курса(снизу input)</p>
          <textarea name="" id="" cols="30" rows="10"></textarea>
        </div>
        <div>
          <p>Преподаватель</p>
          ДОЛЖЕН ПОДСТАВИТЬСЯ ТЫ
        </div>
        <div>
          <p>Emoji</p>
          Список emoji
        </div>
        <div>
          <p>Количество часов(снизу input)</p>
          <input type="text">
        </div>
        <button>Отправить</button>
      </div>
    </Modal>
    <div class="flex flex-row justify-space-around">

      <div class="flex-column m-1 p-1 w-50">
        <div class="card">
          <div class="card-header">
            Информация обо мне
          </div>
          <div class="card-body">
            <p>{{ teacher.last_name }} {{ teacher.first_name }} {{ teacher.patronymic }}, id: {{ teacher.id }}</p>
            <p>{{ teacher.email }}</p>
            <p>{{ teacher.phone || "8 800 555 35 35" }}</p>
          </div>
        </div>
        <div></div>
      </div>

      <div class="flex-column m-1 p-1 w-50">
        <div class="card">
          <div class="card-header flex flex-row justify-space-between">
            <p>Мои курсы</p>
            <button @click="showModal">+</button>
          </div>
          <div class="card-body">
            <div v-for="item in course" :key="item.id">
              <div>{{ item.name }}</div>
              <nuxt-link :to="'/course/'+item.id">Страница курса</nuxt-link>
              <button @click="deleteCourse($event)" :data="item.id">Удалить</button>
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
      show_modal: false
    }
  },
  async mounted() {
    this.reload()
  },
  methods: {
    async reload(){
      let teacher = await (await fetch("http://127.0.0.1:8000/api/teacher/1/")).json();
      let course = await (await fetch(`http://127.0.0.1:8000/api/course?id=2`)).json();
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
