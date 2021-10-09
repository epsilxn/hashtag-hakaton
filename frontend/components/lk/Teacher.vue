<template>
  <div class="top-4">
    <div class="flex flex-row justify-space-around">

      <div class="flex-column m-1 p-1 w-50">
        <div class="card">
          <div class="card-header">
            Информация обо мне
          </div>
          <div class="card-body">
            <div class="flex flex-column mb-1">
              <p>ID</p>
              <p v-text="teacher.id" />
            </div>
            <div class="flex flex-column mb-1">
              <p>Почта</p>
              <p v-text="teacher.email"/>
            </div>
            <div class="flex flex-column mb-1">
              <p>Фамилия</p>
              <p v-text="teacher.last_name"/>
            </div>
            <div class="flex flex-column mb-1">
              <p>Имя</p>
              <p v-text="teacher.first_name"/>
            </div >
            <div class="flex flex-column mb-1">
              <p>Отчество</p>
              <p v-text="teacher.patronymic"/>
            </div>
            <div class="flex flex-column mb-1">
              <p>Телефон</p>
              <p v-text="teacher.phone"/>
            </div>
          </div>
        </div>
        <div></div>
      </div>

      <div class="flex-column m-1 p-1 w-50">
        <div class="card">
          <div class="card-header">
            Мои курсы
          </div>
          <div class="card-body">
            <div v-for="item in course">
              <div v-text="item.name" />
              <nuxt-link :to="'/course/'+item.id">Страница курса</nuxt-link>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "Teacher",
  data() {
    return {
      course: "",
      teacher: ""
    }
  },
  async mounted() {
    // Заменить на динамику, всё работает
    let teacher = await (await fetch("http://127.0.0.1:8000/api/teacher/1/")).json();
    let course = await (await fetch(`http://127.0.0.1:8000/api/course?id=${teacher.id}`)).json();
    console.log(course);
    console.log(teacher);
    this.course = course;
    this.teacher = teacher;
  }
}
</script>

<style scoped>
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
