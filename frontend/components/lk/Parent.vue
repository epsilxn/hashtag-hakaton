<template>
    <div class="main_info">
        <p class="hello">Здравствуйте, родитель</p>
        <div class="line"></div>
        <div class="flex_info">
            <div class="parent_info">
              <p>Фамилия: {{parent.last_name}}</p>
              <p>Имя: {{parent.first_name}}</p>
              <p>Отчество: {{parent.patronymic}}</p>
            </div>
            <div class="child_info">
              <div :key="child.id" v-for="child in parent.children_of_parent">
                  <p>Ваш ребёнок: {{child.last_name}} {{child.first_name}} {{child.patronymic}}</p>
                  <p>Записан на курсы:</p>
                  <div :key="child_course" v-for="child_course in child.courses">
                      <p>{{child_course}}</p>
                  </div>
              </div>
            </div>
        </div>
      </div>
</template>

<script>
export default {
  name: "Parent",
  data() {
    return {
      parent: ""
    }
  },
    async mounted() {
    // Заменить на динамику, всё работает
    let parent = await (await fetch("http://127.0.0.1:8000/api/parent/2/")).json()
    console.log(parent)
    this.parent = parent
  }
}
</script>

<style scoped>

</style>
